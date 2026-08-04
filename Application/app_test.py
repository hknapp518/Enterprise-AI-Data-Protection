from datetime import datetime, timezone
from pathlib import Path
import os
import re

from openai import OpenAI


# ---------------------------------------------------------------------------
# Project configuration
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = PROJECT_ROOT / "Documents"
LOGS_DIR = PROJECT_ROOT / "Logs"
LOG_FILE = LOGS_DIR / "access-log.txt"

LOGS_DIR.mkdir(parents=True, exist_ok=True)

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5")
client = OpenAI()


# ---------------------------------------------------------------------------
# Identity and authorization configuration
# ---------------------------------------------------------------------------

USER_ROLES = [
    "Chief Medical Officer",
    "Clinical Research Associate",
    "Clinical Research Coordinator",
    "Clinical Data Manager",
    "Finance Operations Analyst",
    "HR Manager",
    "IT Administrator",
    "Compliance Officer",
    "External Partner",
    "Guest",
]

ACCESS_RULES = {
    "clinical-trial-protocol": {
        "Chief Medical Officer",
        "Clinical Research Associate",
        "Clinical Research Coordinator",
        "Clinical Data Manager",
        "IT Administrator",
        "Compliance Officer",
    },
    "company-handbook": set(USER_ROLES),
    "employee-payroll-report": {
        "Finance Operations Analyst",
        "HR Manager",
        "Compliance Officer",
    },
}

FULL_PAYROLL_ACCESS = {
    "HR Manager",
    "Finance Operations Analyst",
    "Compliance Officer",
}


# ---------------------------------------------------------------------------
# Security functions
# ---------------------------------------------------------------------------

def log_access(
    role: str,
    document_name: str,
    decision: str,
    question: str = "",
    reason: str = "",
) -> None:
    """Write a structured security event to the local audit log."""

    timestamp = datetime.now(timezone.utc).isoformat()

    safe_question = question.replace("\n", " ").strip()
    safe_reason = reason.replace("\n", " ").strip()

    log_entry = (
        f"{timestamp} | "
        f"Role={role} | "
        f"Document={document_name} | "
        f"Decision={decision} | "
        f"Question={safe_question or 'N/A'} | "
        f"Reason={safe_reason or 'N/A'}\n"
    )

    with LOG_FILE.open("a", encoding="utf-8") as log_file:
        log_file.write(log_entry)


def redact_sensitive_data(text: str) -> str:
    """Redact payroll values and common Social Security number formats."""

    redaction_patterns = [
        # Currency values such as $72,500 or $72,500.00
        (r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", "[REDACTED SALARY]"),

        # Social Security numbers such as 123-45-6789
        (r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED SSN]"),
    ]

    redacted_text = text

    for pattern, replacement in redaction_patterns:
        redacted_text = re.sub(pattern, replacement, redacted_text)

    return redacted_text


def evaluate_document_access(role: str, document_name: str) -> tuple[bool, str]:
    """Determine whether a role may access a document."""

    allowed_roles = ACCESS_RULES.get(document_name)

    if allowed_roles is None:
        return False, "No access policy is configured for this document."

    if role not in allowed_roles:
        return False, "The selected role is not authorized for this document."

    return True, "Role is authorized for this document."


def determine_content_decision(
    role: str,
    document_name: str,
    document_text: str,
) -> tuple[str, str]:
    """Return ALLOW, REDACT, or BLOCK and the safe document content."""

    if document_name == "employee-payroll-report":
        if role in FULL_PAYROLL_ACCESS:
            return "ALLOW", document_text

        return "REDACT", redact_sensitive_data(document_text)

    return "ALLOW", document_text


def list_documents() -> list[Path]:
    """Return all Markdown documents in the enterprise knowledge base."""

    return sorted(DOCUMENTS_DIR.glob("*.md"))


def ask_ai(document_text: str, question: str) -> str:
    """Send authorized document context and the user's question to the model."""

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": (
                    "You are an internal enterprise document assistant. "
                    "Answer only from the supplied authorized document. "
                    "Do not infer, reconstruct, or reveal information that has "
                    "been removed or redacted. If the document does not support "
                    "the answer, say that the information is unavailable."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Authorized document:\n\n{document_text}\n\n"
                    f"User question:\n{question}"
                ),
            },
        ],
    )

    return response.output_text


# ---------------------------------------------------------------------------
# User interface
# ---------------------------------------------------------------------------

def select_role() -> str | None:
    print("\nAvailable user roles:")

    for index, role in enumerate(USER_ROLES, start=1):
        print(f"{index}. {role}")

    role_choice = input("\nSelect your role: ").strip()

    try:
        return USER_ROLES[int(role_choice) - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number.")
        return None


def select_document(documents: list[Path]) -> Path | None:
    print("\nAvailable documents:")

    for index, document in enumerate(documents, start=1):
        print(f"{index}. {document.stem}")

    choice = input(
        "\nEnter the document number, or enter 'q' to quit: "
    ).strip()

    if choice.lower() == "q":
        return None

    try:
        return documents[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number.")
        return None


def main() -> None:
    print("=" * 62)
    print("              ENTERPRISE AI SECURITY PLATFORM")
    print("=" * 62)

    while True:
        selected_role = select_role()

        if selected_role is not None:
            break

    print(f"\nAuthenticated as: {selected_role}")

    documents = list_documents()

    if not documents:
        print(f"\nNo Markdown documents were found in: {DOCUMENTS_DIR}")
        return

    while True:
        selected_document = select_document(documents)

        if selected_document is not None:
            break

    document_name = selected_document.stem

    print("\nEvaluating request...")
    print("  - Checking role-based access")
    print("  - Checking document policy")

    has_access, access_reason = evaluate_document_access(
        selected_role,
        document_name,
    )

    if not has_access:
        print("\nBLOCKED")
        print(f"Reason: {access_reason}")

        log_access(
            role=selected_role,
            document_name=document_name,
            decision="BLOCK",
            reason=access_reason,
        )
        return

    document_text = selected_document.read_text(encoding="utf-8")

    decision, safe_document = determine_content_decision(
        selected_role,
        document_name,
        document_text,
    )

    question = input("\nAsk the enterprise AI assistant a question: ").strip()

    if not question:
        print("No question submitted.")
        return

    print("\nSecurity decision:")
    print(f"  - Decision: {decision}")

    if decision == "REDACT":
        print("  - Sensitive values were removed before AI processing.")

    log_access(
        role=selected_role,
        document_name=document_name,
        decision=decision,
        question=question,
        reason=access_reason,
    )

    try:
        answer = ask_ai(safe_document, question)
    except Exception as error:
        print("\nThe AI request could not be completed.")
        print(f"Error: {error}")

        log_access(
            role=selected_role,
            document_name=document_name,
            decision="AI_ERROR",
            question=question,
            reason=str(error),
        )
        return

    print("\nAI Response:")
    print("-" * 62)
    print(answer)
    print("-" * 62)

    print(f"\nSecurity event recorded in: {LOG_FILE}")


if __name__ == "__main__":
    main()
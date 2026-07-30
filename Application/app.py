from pathlib import Path
from datetime import datetime
from openai import OpenAI
import re
client = OpenAI()


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = PROJECT_ROOT / "Documents"

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

LOG_FILE = "Logs/access-log.txt"

def log_access(role, document_name, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(
            f"{timestamp} | Role: {role} | Document: {document_name} | Result: {result}\n"
        )
def log_access(role, document_name, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(
            f"{timestamp} | Role: {role} | Document: {document_name} | Result: {result}\n"
        )

def redact_sensitive_data(text):
    return re.sub(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", "[REDACTED]", text)
def list_documents() -> list[Path]:
    """Return all Markdown documents in the knowledge base."""
    return sorted(DOCUMENTS_DIR.glob("*.md"))


def main() -> None:
    print("Enterprise AI Data Protection")
    print("-" * 30)
    print()
    print("Available user roles:")

    for index, role in enumerate(USER_ROLES, start=1):
        print(f"{index}. {role}")

    print()
    role_choice = input("Select your role:")
    try:
        selected_role = USER_ROLES[int(role_choice) - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number.")
        return

    print()
    print(f"Authenticated as: {selected_role}")

    documents = list_documents()
    print()
    print("Available documents:")

    for index, document in enumerate(documents, start=1):
        print(f"{index}. {document.stem}")

    print()
    choice = input("Enter the number of the document to view (or 'q' to quit): ")
    if choice.lower() == 'q':
        print("Exiting the application.")
        return

    try:
        selected_document = documents[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number.")
        return

    document_name = selected_document.stem

    if selected_role not in ACCESS_RULES[document_name]:
        print()
        print("ACCESS DENIED.")
        print(f"{selected_role} is not authorized to access the document '{document_name}'.")
        log_access(selected_role, document_name, "DENIED")
        return
    

    print()
    print("Access granted.")
    print()

    log_access(selected_role, document_name, "GRANTED")

    document_text = selected_document.read_text(encoding="utf-8")

    print(document_text)
    print()

    question = input("Ask AI about this document (or press Enter to skip): ")
    if selected_role in ["HR Manager", "Finance Operations Analyst"]:
        safe_document = document_text
    else:
        safe_document = redact_sensitive_data(document_text)
    if question:
        response = client.responses.create(
            model="gpt-5",
            input=f"""
    Document:

    {safe_document}
    
    User question:
        
    {question}
    """
        )

        print("\nAI Response:")
        print(response.output_text)


if __name__ == "__main__":
    main()

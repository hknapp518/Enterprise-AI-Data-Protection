from pathlib import Path


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
        return

    print()
    print("Access granted.")
    print()


if __name__ == "__main__":
    main()

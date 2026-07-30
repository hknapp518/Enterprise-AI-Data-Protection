from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = PROJECT_ROOT / "Documents"


def list_documents() -> list[Path]:
    """Return all Markdown documents in the knowledge base."""
    return sorted(DOCUMENTS_DIR.glob("*.md"))


def main() -> None:
    print("Enterprise AI Data Protection")
    print("-" * 30)

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

    print()
    print(selected_document.read_text(encoding="utf-8"))  # Display the content of the selected document

    if not documents:
        print("No documents found.")
        return

if __name__ == "__main__":
    main()

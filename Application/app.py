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

    if not documents:
        print("No documents found.")
        return

    print("Knowledge base documents:")

    for document in documents:
        print(f"- {document.name}")


if __name__ == "__main__":
    main()

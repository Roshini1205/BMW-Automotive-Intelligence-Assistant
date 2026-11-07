
from pathlib import Path
from pypdf import PdfReader

DATA_DIR = Path("backend/data")


def load_pdfs():
    documents = []

    for pdf_path in DATA_DIR.glob("*.pdf"):
        if pdf_path.stat().st_size == 0:
            print(f"Skipping empty file: {pdf_path.name}")
            continue

        reader = PdfReader(str(pdf_path))

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            if text.strip():
                documents.append({
                    "text": text,
                    "source": pdf_path.name,
                    "page": page_number,
                })

    return documents


if __name__ == "__main__":
    docs = load_pdfs()
    print(f"Pages loaded: {len(docs)}")

    for doc in docs[:3]:
        print(f"\nSource: {doc['source']}")
        print(f"Page: {doc['page']}")
        print(doc["text"][:300])

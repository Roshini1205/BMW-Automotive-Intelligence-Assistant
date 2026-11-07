
import json
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.app.ingest import load_pdfs


# Initialize text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    add_start_index=True
)


# Split PDF pages into smaller chunks
def split_documents(pages):
    chunks = []

    for page in pages:
        text_chunks = splitter.split_text(page["text"])

        for index, text in enumerate(text_chunks):
            chunks.append({
                "text": text,
                "source": page["source"],
                "page": page["page"],
                "chunk_id": index
            })

    return chunks


# Save chunks into JSON file
def save_chunks(chunks):
    output_path = Path("backend/storage/chunks.json")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(f"Saved {len(chunks)} chunks to {output_path}")


# Main execution
if __name__ == "__main__":

    # Load PDF pages
    pages = load_pdfs()

    # Generate chunks
    chunks = split_documents(pages)

    print("Total pages:", len(pages))
    print("Total chunks:", len(chunks))

    if chunks:

        print("\nFirst chunk:")
        print(chunks[0]["text"])

        print("\nMetadata:")
        print("Source:", chunks[0]["source"])
        print("Page:", chunks[0]["page"])
        print("Chunk ID:", chunks[0]["chunk_id"])

        # Save chunks to JSON
        save_chunks(chunks)

    else:
        print("No chunks were generated.")

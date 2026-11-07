
import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


# Project storage paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

STORAGE_DIR = PROJECT_ROOT / "backend" / "storage"

CHUNKS_PATH = STORAGE_DIR / "chunks.json"
CHROMA_PATH = STORAGE_DIR / "chroma"


# Load embedding model
print("Loading embedding model...")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

embedding_model = SentenceTransformer(MODEL_NAME)


# Initialize ChromaDB
client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collection = client.get_or_create_collection(
    name="automotive_manuals",
    metadata={"description": "Automotive vehicle manuals"}
)


# Load chunks from JSON
def load_chunks():

    if not CHUNKS_PATH.exists():
        raise FileNotFoundError(
            f"Chunks file not found: {CHUNKS_PATH}. "
            "Run python -m backend.app.chunk first."
        )

    with open(CHUNKS_PATH, "r", encoding="utf-8") as file:
        chunks = json.load(file)

    return chunks


# Generate embeddings
def create_embeddings(texts):

    embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings.tolist()


# Store documents in ChromaDB
def store_documents():

    chunks = load_chunks()

    if not chunks:
        print("No chunks available.")
        return

    print(f"Generating embeddings for {len(chunks)} chunks...")

    batch_size = 100

    for start in range(0, len(chunks), batch_size):

        batch = chunks[start:start + batch_size]

        texts = [item["text"] for item in batch]

        embeddings = create_embeddings(texts)

        ids = [
            f"{item['source']}_page_{item['page']}_chunk_{item['chunk_id']}"
            for item in batch
        ]

        metadatas = [
            {
                "source": str(item["source"]),
                "page": int(item["page"]),
                "chunk_id": int(item["chunk_id"])
            }
            for item in batch
        ]

        collection.upsert(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )

        print(
            f"Stored {min(start + batch_size, len(chunks))}"
            f"/{len(chunks)} chunks"
        )

    print("\nVector database created successfully!")
    print("Total stored documents:", collection.count())


# Search relevant documents
def search_documents(query, top_k=5):

    if collection.count() == 0:
        print("Vector database is empty.")
        return {}

    query_embedding = create_embeddings([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"]
    )

    return results


# Test the vector database
if __name__ == "__main__":

    store_documents()

    question = "What maintenance is required for the vehicle?"

    print("\nTesting semantic search...")
    print("Question:", question)

    results = search_documents(question)

    if results and results.get("documents"):

        for index, document in enumerate(results["documents"][0]):

            metadata = results["metadatas"][0][index]

            print(f"\nResult {index + 1}")
            print("Source:", metadata["source"])
            print("Page:", metadata["page"])
            print("Chunk ID:", metadata["chunk_id"])
            print("Text:", document[:500])

    else:
        print("No matching documents found.")

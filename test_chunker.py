from modules.pdf_loader import load_pdf
from modules.chunker import create_chunks

print("Loading PDF...")

pages = load_pdf("data/sample.pdf")

print(f"Pages loaded: {len(pages)}")

chunks = create_chunks(
    pages,
    chunk_size=500,
    overlap=50
)

print(f"Total chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print("-" * 50)

print(chunks[0]["text"][:300])

print("\nPage Number:")
print(chunks[0]["page"])
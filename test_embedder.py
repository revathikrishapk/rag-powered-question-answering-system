from modules.pdf_loader import load_pdf
from modules.chunker import create_chunks
from modules.embedder import create_embeddings

pages = load_pdf("data/sample.pdf")

chunks = create_chunks(
    pages,
    chunk_size=500,
    overlap=50
)

embeddings = create_embeddings(chunks)

print("\nEmbedding Shape:")
print(embeddings.shape)

print("\nFirst Vector (first 10 values):")
print(embeddings[0][:10])
from modules.pdf_loader import load_pdf
from modules.chunker import create_chunks
from modules.embedder import (
    create_embeddings,
    model
)
from modules.retriever import (
    create_index,
    search
)

pages = load_pdf("data/sample.pdf")

chunks = create_chunks(pages)

embeddings = create_embeddings(chunks)

index = create_index(embeddings)

question = input("Ask a question: ")

results = search(
    question,
    model,
    index,
    chunks,
    k=3
)

print("\nTop Retrieved Chunks:\n")

for i, chunk in enumerate(results, start=1):

    print(f"\nChunk {i}")
    print("-" * 50)

    print(chunk["text"][:300])

    print(f"\nPage: {chunk['page']}")
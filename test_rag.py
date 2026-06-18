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
from modules.llm import generate_answer

# Load PDF
pages = load_pdf("data/sample.pdf")

# Create chunks
chunks = create_chunks(pages)

# Generate embeddings
embeddings = create_embeddings(chunks)

# Build FAISS index
index = create_index(embeddings)

print("\nRAG System Ready!\n")

while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    retrieved_chunks = search(
        question,
        model,
        index,
        chunks,
        k=3
    )

    answer = generate_answer(
        question,
        retrieved_chunks
    )

    print("\nAnswer:")
    print("-" * 50)
    print(answer)

    print("\nSources:")
    print("-" * 50)

    for chunk in retrieved_chunks:
        print(f"Page {chunk['page']}")
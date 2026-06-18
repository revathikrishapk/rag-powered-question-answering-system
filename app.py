import streamlit as st

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


st.set_page_config(
    page_title="RAG Document Q&A",
    page_icon="📄"
)

st.title("📄 RAG Document Q&A System")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    pages = load_pdf("temp.pdf")

    chunks = create_chunks(pages)

    embeddings = create_embeddings(chunks)

    index = create_index(embeddings)

    question = st.text_input(
        "Ask a question about the document"
    )

    if question:

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

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        shown_pages = set()

        for chunk in retrieved_chunks:

            if chunk["page"] not in shown_pages:

                shown_pages.add(chunk["page"])

                with st.expander(
                    f"Page {chunk['page']}"
                ):
                    st.write(chunk["text"])
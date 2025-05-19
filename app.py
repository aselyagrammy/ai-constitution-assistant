from langchain_community.llms import Ollama
from langchain.chains.question_answering import load_qa_chain
from document_loader import load_and_split
from vector_store import save_to_vectorstore, load_vectorstore
import streamlit as st
import os

st.title("🤖 AI Assistant: Constitution of Kazakhstan")

uploaded_file = st.file_uploader("📄 Upload Constitution PDF", type="pdf")

if uploaded_file:
    with open("constitution.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ File uploaded successfully!")

    chunks = load_and_split("constitution.pdf")
    
    # Создание или загрузка векторного хранилища
    if not os.path.exists("db/index"):
        db = save_to_vectorstore(chunks)
    else:
        db = load_vectorstore()

    query = st.text_input("💬 Ask a question about the Constitution:")

    if st.button("Submit") and query.strip() != "":
        docs = db.similarity_search(query)
        context = "\n\n".join([doc.page_content for doc in docs])

        # Запуск Ollama с моделью llama3
        llm = Ollama(model="llama3")

        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=query)

        st.subheader("📢 Answer:")
        st.write(response)


from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

persist_directory = "db"

def save_to_vectorstore(chunks):
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=persist_directory
    )
    db.persist()
    return db

def load_vectorstore():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding
    )
    return db

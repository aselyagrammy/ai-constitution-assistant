from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def load_and_split(path_to_pdf):
    loader = PyPDFLoader(path_to_pdf)
    docs = loader.load()

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    return chunks

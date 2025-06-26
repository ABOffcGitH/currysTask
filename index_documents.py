from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import logging

def build_vector_store(pdf_path: str = PDF_PATH, persist_dir: str = VECTOR_DB_DIR) -> None:  # Loads a PDF, splits it into text chunks, creates embeddings, and stores them in a vector DB.
  
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    docs = splitter.split_documents(pages)

    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings(),
        persist_directory=persist_dir,
    )
    vectordb.persist()
    logging.info("Vector DB built and persisted.")
  
if __name__ == "__main__":
    build_vector_store()

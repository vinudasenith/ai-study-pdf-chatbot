from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embedding_model
from utils.loader import load_pdf
import os

DB_FAISS_PATH = "db/faiss_index"

def prepare_vector_store(pdf_path):

    chunks = load_pdf(pdf_path)  
    texts = [doc.page_content for doc in chunks]  

    
    embeddings = get_embedding_model()

    db = FAISS.from_texts(texts, embeddings)


    db.save_local(DB_FAISS_PATH)
    print("✅ Vector store successfully created and saved.")

prepare_vector_store("data/sample.pdf")

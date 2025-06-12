from langchain_community.vectorstores import FAISS
import os

def create_or_load_faiss(chunks_or_embeddings, embedding=None, index_path="faiss_index"):
    if os.path.exists(index_path):
        return FAISS.load_local(index_path, embeddings=chunks_or_embeddings)
    else:
        if not os.path.exists(index_path):
            os.makedirs(index_path)
        db = FAISS.from_texts(chunks_or_embeddings, embedding=embedding)
        db.save_local(index_path)
        return db

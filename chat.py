from langchain_community.vectorstores import FAISS
from utils.llm import get_llm
from langchain.chains import RetrievalQA
from utils.embeddings import get_embedding_model

DB_FAISS_PATH = "db/faiss_index"

def ask_question(query):
    embeddings = get_embedding_model()
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

    retriever = db.as_retriever()
    llm = get_llm()

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

    result = qa({"query": query})
    return result["result"]

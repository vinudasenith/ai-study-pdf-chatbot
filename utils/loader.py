from langchain_community.document_loaders import PyPDFLoader

file_path = "data/sample.pdf"
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

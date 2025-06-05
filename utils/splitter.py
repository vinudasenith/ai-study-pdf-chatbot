from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    return text_splitter.split_documents(text)

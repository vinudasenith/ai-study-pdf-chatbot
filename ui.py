import streamlit as st
from chat import ask_question

st.set_page_config(page_title="📚 AI Study PDF Chatbot", layout="wide")
st.title("🧠 AI Study Companion")

st.markdown("Ask anything about your uploaded PDF!")

query = st.text_input("🔎 Enter your question:")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        answer = ask_question(query)
    st.success("✅ Answer:")
    st.write(answer)

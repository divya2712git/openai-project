import streamlit as st
from providers.groq_provider import ask_ai

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")

question = st.text_area(
    "Ask your question",
    height=150
)

if st.button("Ask AI"):

    if question.strip():

        with st.spinner("Thinking..."):

            answer = ask_ai(question)

        st.success("Response")

        st.write(answer)

    else:

        st.warning("Please enter a question.")
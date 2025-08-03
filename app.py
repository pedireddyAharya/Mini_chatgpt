import streamlit as st
from transformers import pipeline, set_seed

@st.cache_resource
def load_generator():
    generator = pipeline('text-generation', model='gpt2')
    return generator

generator = load_generator()
set_seed(42)

st.title("🧠 Mini ChatGPT (GPT-2 Based)")

user_input = st.text_input("You:", key="input")

if user_input:
    prompt = user_input
    response = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    st.markdown(f"**You**: {user_input}")
    st.markdown(f"**Bot**: {response[len(prompt):]}")

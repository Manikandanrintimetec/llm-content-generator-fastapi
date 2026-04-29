
import requests
import streamlit as st

# Essay API call
def get_essay_response(input_text):
        try:
            response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={'input': {'topic': input_text}}
            )
            return response.json()['output']['content']
        except Exception as e:
            return f"Error: {e}"

# Poem API call (same model now)
def get_poem_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']['content']


# Streamlit UI
st.title('LangChain Demo with OpenRouter')

input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_essay_response(input_text))

if input_text1:
    st.write(get_poem_response(input_text1))
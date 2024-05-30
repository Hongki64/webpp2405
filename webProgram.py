mport streamlit as st
from langchain.llms import OpenAI

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

# Sidebar for OpenAI API Key input
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Function to generate response from OpenAI
def generate_response(input_text):
    if not openai_api_key.startswith('sk-'):
        st.warning('유효한 OpenAI API 키를 입력해 주세요!', icon='⚠')
        return

    try:
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = llm(input_text)
        st.info(response)
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

# Form for user input
with st.form('my_form'):
    text = st.text_area('텍스트를 입력하세요:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('제출')

    if submitted:
        generate_response(text)

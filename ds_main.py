import streamlit as st
import requests

st.title("🤖 DeepSeek-R1 Chat via OpenRouter")

# Load from secrets.toml
openrouter_api_key = st.secrets["OPENROUTER_API_KEY"]

# Optional site info
site_url = "https://yourapp.com"
site_name = "My Streamlit App"

def generate_response(input_text):
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "HTTP-Referer": site_url,
        "X-Title": site_name,
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [{"role": "user", "content": input_text}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        st.info(result["choices"][0]["message"]["content"])
    else:
        st.error(f"Error {response.status_code}: {response.text}")

# Streamlit input form
with st.form("deepseek_form"):
    user_input = st.text_area("Ask something:", "What is the meaning of life?")
    submitted = st.form_submit_button("Submit")

    if submitted:
        generate_response(user_input)

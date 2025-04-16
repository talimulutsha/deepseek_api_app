import streamlit as st
from openai import OpenAI

# Set the page title
st.title('🤖 DeepSeek-R1 Chat via OpenRouter')

# Hardcode the API key (for testing purposes)
openrouter_api_key = "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"


# Optional site info (not visible to users)
site_url = "https://yourapp.com"  # You can change this to your app's URL
site_name = "My Streamlit App"    # You can change this to your site’s name

# Function to generate the response using DeepSeek-R1
def generate_response(input_text):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_api_key,
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": site_url,  # Optional: Your site URL
            "X-Title": site_name,      # Optional: Your site name
        },
        model="deepseek/deepseek-r1:free",
        messages=[
            {
                "role": "user",
                "content": input_text
            }
        ]
    )

    st.info(completion.choices[0].message.content)

# Text input form
with st.form('deepseek_form'):
    text = st.text_area('Ask something:', 'What is the meaning of life?')
    submitted = st.form_submit_button('Submit')

    if not openrouter_api_key:
        st.warning('Please set the OPENROUTER_API_KEY environment variable.', icon='⚠')
    elif submitted:
        generate_response(text)

import streamlit as st
from pdfminer.high_level import extract_text
import openai
from getpass import getpass

# Securely input your OpenAI API key
api_key = getpass("Enter your OpenAI API Key: ")
client = openai.OpenAI(api_key=api_key)

# Input field for the resume
st.title(' ResumeFit')
st.markdown('Streamlining Job Applications with AI')
resume_text = input("Paste your resume here: ")

# Input field for the job description
job_description_text = input("Paste the job description here: ")

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    df = extract_data(uploaded_file)

# Cell 3: Function to generate text using OpenAI
def analyze_text(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI (adjust if needed)
    messages = [
        {"role": "system", "content": " You are an assistant who helps streamline job applications to bridge gap between job seekers and job postings."},
        {"role": "user", "content": f" Please help me write a special message to a loved one based on the following:\n{text}"}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].message.content

# Input field for the job description
job_description_text = input("Paste the job description here: ")

compare_resume_to_job_description(resume_text, job_description_text)

# Cell 4: Function to generate the image
def generate_image(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return

    response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    # Assuming the API returns an image URL; adjust based on actual response structure
    return response.data[0].url

# Cell 5: Streamlit UI 
user_input = st.text_area("Enter a brief for your post:", " Though the day was cold, the warmth of your heart made everything feel brighter and more comforting")

if st.button('Generate Post Content'):
    with st.spinner('Generating Text...'):
        post_text = analyze_text(user_input)
        st.write(post_text)

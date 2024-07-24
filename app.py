import streamlit as st
from docx import Document
from pdfminer.high_level import extract_text
import openai
from getpass import getpass

# Securely input your OpenAI API key
api_key = getpass("Enter your OpenAI API Key: ")
client = openai.OpenAI(api_key=api_key)

# Input field for the resume
resume_text = input("Paste your resume here: ")

# Input field for the job description
job_description_text = input("Paste the job description here: ")

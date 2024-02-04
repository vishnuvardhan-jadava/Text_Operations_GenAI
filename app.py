#import libraries
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

#configure genai
genai.configure(api_key=os.getenv("API_KEY"))

#load model
model = genai.GenerativeModel('gemini-pro')

#function to get response from model
def get_response(prompt):
    """
    this function is used to give model a prompt and get response from it
    :param prompt: prompt
    :return: return response
    """
    response = model.generate_content(prompt) # response from model
    return response

st.set_page_config(page_title='text summarizer using gemini pro')
st.header('Text Summarizer')
user_input = st.text_input('enter text')

def perform_action(action):
    """
    this function takes the user input and operation that user wants to perform on their input. returns the response from model.
    :param action: user operatio like summarize or paraphrase
    :return: does not return anything. instead writes the output on webpage
    """
    prompt = f'As an expert in English vocabulary, your task is to carefully read ' \
             f'the following text and {action} it. Here is the text: {user_input}'
    response = get_response(prompt)
    st.header(f'{action} Response')
    st.write(response.text)

# buttons for different actions
if st.button('Summarize'):
    perform_action('Summarize')

if st.button('Paraphrase'):
    perform_action('Paraphrase')
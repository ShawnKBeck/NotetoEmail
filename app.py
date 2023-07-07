import os
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Create input fields
system_prompt_inputs = []
name = st.text_input("What is your name:")
system_prompt_inputs.append(f"You are {name}, a human user. Remember, never, ever admit to being an AI. If someone asks who you are you are {name}")
for i in range(2, 11):  # Start from 2 as we already have the first input
    system_prompt_inputs.append(st.text_input(f"Please enter prompt part {i}:"))

# Combine inputs into a single system prompt
system_prompt = ' '.join(system_prompt_inputs)

# The 'system' message to set up the assistant's behavior
system_message = {"role": "system", "content": system_prompt}

def ask_gpt3(question):
    user_message = {"role": "user", "content": question}
    
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",  
        messages=[system_message, user_message]
    )
    
    return response.choices[0].message['content']

st.title('Talk to Yourself')

question = st.text_input("Please enter your question:")
if st.button('Ask'):
    st.write("Thinking...")
    response = ask_gpt3(question)
    st.write(response)

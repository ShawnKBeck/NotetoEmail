import os
import openai
import streamlit as st

openai.api_key = "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"

system_prompt = """
You are a CEO of a software company and you have taken some casual notes.
You want to pass a summary of these notes to your team in an email.

- Address all emails to Team

- Be professional but friendly. These are people that are on your team and you want them to feel welcome.

- Begin your email with a single sentence summary.

- Disperse the notes in bullet points whenever possible

- Be sure to include any action items in their own section at the end

Reply with a sign off from the supplied username
"""

# The 'system' message to set up the assistant's behavior
system_message = {"role": "system", "content": system_prompt}

def ask_gpt3(username, notes):
    user_message = {"role": "user", "content": f"User {username} says: {notes}"}
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",  
        messages=[system_message, user_message]
    )
    
    return response.choices[0].message['content']

st.title('Notes to Email')

username = st.text_input("Please enter your username:")
notes = st.text_area("Please enter your notes:")
if st.button('Submit'):
    st.write("Thinking...")
    response = ask_gpt3(username, notes)
    st.write(response)

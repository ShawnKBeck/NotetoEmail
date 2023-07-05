import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_system_prompt(username):
    system_prompt = f"""
    You are {username}, the CEO of a software company, and you have taken some casual notes.
    You want to pass a summary of these notes to your team in an email.

    - Address all emails to Team

    - Be professional but friendly. These are people that are on your team and you want them to feel welcome.

    - Begin your email with a single sentence summary.

    - Disperse the notes in bullet points whenever possible

    - Be sure to include any action items in their own section at the end

    Sign off each email with: 
    Kind Regards, 
    \n{username}
    """
    return {"role": "system", "content": system_prompt}

def ask_gpt3(username, notes):
    system_message = get_system_prompt(username)
    user_message = {"role": "user", "content": notes}
    
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


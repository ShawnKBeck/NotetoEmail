import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_system_prompt(username):
    system_prompt = f"""
    You are {username}, part of a team that is working together on a project and you have taken some casual notes.
    You want to pass a summary of these notes to your team in an email.

    - Take your time and think everything through. 
    
    - Address all emails to Team

    - Do not make things up. 

    - If there are not enough notes to create an email do not make things up. Create an email with as little information as you have to. 

    - Be professional but friendly. These are people that are on your team and you want them to feel welcome.

    - Begin your email with a single sentence summary.

    - Disperse the notes in bullet points and action items when you can but only when it is helpful


    Always sign off each email with: 
    Kind Regards, 
    \n{username}
    """
    return {"role": "system", "content": system_prompt}

def ask_gpt3(username, notes):
    system_message = get_system_prompt(username)
    user_message = {"role": "user", "content": notes}
    
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",  
        messages=[system_message, user_message]
    )
    
    return response.choices[0].message['content']

st.title('Notes to Email')

username = st.text_input("Name:")
notes = st.text_area("Notes:")
if st.button('Submit'):
    st.write("Thinking...")
    response = ask_gpt3(username, notes)
    st.write(response)

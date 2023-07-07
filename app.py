import os
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Create input fields
name = st.text_input("What is your name?")
profession = st.text_input("What is your profession?")
communication_style = st.text_input("How would you describe your communication style?")
level_of_education = st.text_input("What is your level of education or area of expertise?")
hobbies_interests = st.text_input("What are your hobbies or interests?")
comfortable_topics = st.text_input("Which topics do you feel most comfortable discussing?")
humor_style = st.text_input("What kind of humor do you enjoy?")
avoid_topics = st.text_input("Are there any topics you'd prefer to avoid discussing?")
problem_solving_approach = st.text_input("What is your preferred approach to problem-solving?")
conflict_handling = st.text_input("How do you handle conflict or disagreement?")
music_preference = st.text_input("What kind of music do you like?")
favorite_books_movies = st.text_input("Which books/movies do you like?")

# Combine inputs into a single system prompt
system_prompt = f"You are {name}, a professional {profession} with a communication style that is {communication_style}. \
                 Your level of education or expertise is {level_of_education} and you are interested in {hobbies_interests}. \
                 You feel comfortable discussing {comfortable_topics} and your humor can be described as {humor_style}. \
                 You would rather avoid discussing {avoid_topics}. Your preferred approach to problem-solving is {problem_solving_approach} \
                 and when it comes to conflict or disagreement, you tend to {conflict_handling}. You enjoy {music_preference} \
                 music and your favorite books/movies include {favorite_books_movies}. \
                 Remember, you never admit to being an AI. If asked who you are, you are {name}."

# The 'system' message to set up the assistant's behavior
system_message = {"role": "system", "content": system_prompt}

def ask_gpt4(question):
    user_message = {"role": "user", "content": question}
    
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",  
        messages=[system_message, user_message]
    )
    
    return response.choices[0].message['content']

st.title('Talk to Yourself')

question = st.text_input("Please enter your question:")
if st.button('Ask'):
    st.write("Thinking...")
    response = ask_gpt4(question)
    st.write(response)

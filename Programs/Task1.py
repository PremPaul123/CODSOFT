import re
import nltk
import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

responses = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a great day!",
    "your name": "I'm CodSoft AI Bot!",
    "default": "Sorry, I don't understand. Can you rephrase?"
}

def preprocess_text(text):
    """Tokenize and lemmatize input text."""
    tokens = word_tokenize(text.lower())
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatization
    return " ".join(lemmatized_words)

def chatbot_response(user_input):
    """Generate a chatbot response based on user input."""
    user_input = preprocess_text(user_input)

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return responses["default"]

st.title("Chatbot with NLTK")
st.write("This is a simple rule-based chatbot using NLTK for text preprocessing.")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)
        st.text_area("Chatbot:", value=response, height=100, disabled=True)

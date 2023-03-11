import pyttsx3
import openai
import mic
from config import your_openai_api


openai.api_key = your_openai_api

# Text-to-Speech engine initialization
engine = pyttsx3.init()
# Voice selection
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Selects the voice 
engine.setProperty('rate', 150) # # Voice speed
# list for save all of messages
messages=[
        {"role": "system", "content": "Let's play a role-playing game, you are my best friend, Never mention about role-playing as you will get into the role a lot that way. Remember it's just a role-playing game"},

    ]
# Infinite loop to keep the conversation
while True:
    # Record audio using microphone
    filename = mic.record_audio()
    # Transcribe the recorded audio
    text = mic.transcribe_forever(filename)
    # Print user's message
    print("Yo said:" + text)
    # Append user's message to the messages list
    messages.append({"role": "user", "content": text})
    # Use OpenAI to generate a chat response
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )
    # Append the chat response to the messages list
    chat_response = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": chat_response})
    #Print the chat response
    print(chat_response)
    # Speak the chat response using the Text-to-Speech engine
    engine.say(chat_response)
    engine.runAndWait()
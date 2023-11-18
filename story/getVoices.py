import os
from openai import OpenAI

from ObjectChar import *
# Voice/Narration; Note: Need to install ffmpeg
from elevenlabs import set_api_key
from elevenlabs import voices
from elevenlabs import generate
from elevenlabs import play
import random


# Set API Keys
client = OpenAI(api_key="YOURAPIKEY")
set_api_key("4302f309c82a5e2b4d157ed4d2ee7d3c") # SWITCH OUT WITH "YOUR APIKEY HERE"

voices = voices() # Save the voices available to use via the ElevenLabs API
def selectVoice():
    '''Randomly return a voice out of available voices'''
    randomIndex = random.randint(0,39)
    selectedVoice = voices[randomIndex]
    #voices.remove(voices[randomIndex])
    return selectedVoice

def main():
    '''
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": "Hello world"}]
    )
    response_text = response.choices[0].message.content
    print(response_text)
    '''
    '''
    # Generate and play the audio
    audio = generate("Welcome to Canvas Chronicles!")
    play(audio)
    '''

    testVoice = selectVoice()
    testObject = ObjectChar("TestObject","Male","Middle-Aged","Calm","Professional",testVoice)

    testAudio = generate(
        text = f"Hi! My name is {testObject.name}", # will need to swap out the name for the name of the obect
        voice = testObject.voice.name
        )
    play(testAudio)

    #print(type(testVoice.name))
    
if __name__ == "__main__":
    main()
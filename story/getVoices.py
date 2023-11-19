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
maleVoices = []
femaleVoices = []
# Sort voices into male and female voices
for voice in voices:
    if (voice.labels['gender'] == 'male'):
        maleVoices.append(voice)
    else:
        femaleVoices.append(voice)



def selectVoice(charGender):
    '''Randomly return a gender-specific voice out of available voices'''
    if (charGender == "Man"):
        randomIndex = random.randint(0,len(maleVoices)-1)
        selectedVoice = maleVoices[randomIndex]
        maleVoices.remove(maleVoices[randomIndex])
        return selectedVoice
    else:
        randomIndex = random.randint(0,len(femaleVoices)-1)
        selectedVoice = femaleVoices[randomIndex]
        femaleVoices.remove(femaleVoices[randomIndex])
        return selectedVoice
    

''' Helpful reminders with AI-voice API'''
    #testVoice = selectVoice("Male")
    #testObject = ObjectChar("TestObject","Male","Middle-Aged","Calm","Professional",testVoice)

'''
    testAudio = generate(
        text = f"Hi! My name is {testObject.name}", # will need to swap out the name for the name of the obect
        voice = testObject.voice.name
        )
    play(testAudio)
'''
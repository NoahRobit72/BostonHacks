from flask import Flask, render_template, request
import re
import time

# Scripts
from processImage import *  # Jared: process image and get the objects
from getStory import *      # Mete: create AI-generated story involving objects
from getVoices import *     # Jilin: assign AI-generated voice to objects
from ObjectChar import *    # Objects' class

finalizedChars = []         # An array to store the characters into the ObjectChar class

def processImage():
    '''Take the user-inputted image and generate characters as well as a beginning context'''
    #charsAndContext = genCharAndContext() (currently sampleOutput)#main()  
    sampleOutput = main()
    
    sampleOutput = sampleOutput.strip()
    # Partition the output for just the characters
    partitionedOutput = sampleOutput.partition("Beginning Prompt")
    characters = partitionedOutput[0]
    plot = partitionedOutput[2]

    # List of individual characters
    objectChars = partitionedOutput[0].split("\n\n") # Might have an extra useless entry
    objectChars = objectChars[0:len(objectChars)-1]

    # Loop through the first partition (the identified objects)
    characterCount = 0
    for character in objectChars:
        # Create and save ObjectChar objects with the current character
        finalizedChars.append(setCharacter(character))
        finalizedChars[characterCount].voice = assignCharVoice(finalizedChars[characterCount])
        characterCount+=1

    # Print the current character's attributes and have the character introduce themself
    for character in finalizedChars:
        assignCharVoice(character)
        #Uncomment when voice is wanted
        '''testAudio = generate(
            text = f"Hi! My name is {character.name}. It is a pleasure to meet you!",
            voice = character.voice.name
        )
        play(testAudio)'''

    generateStory(finalizedChars,sampleOutput)
        
if __name__ == "__main__":
    start = time.time()

    processImage()
    generateStory(finalizedChars)

    end = time.time()
    print(end - start,"seconds")
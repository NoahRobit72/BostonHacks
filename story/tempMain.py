from flask import Flask, render_template, request
import re

# Scripts
from processImage import *  # Jared: process image and get the objects
from getStory import *      # Mete: create AI-generated story involving objects
from getVoices import *     # Jilin: assign AI-generated voice to objects
from ObjectChar import *    # Objects' class

finalizedChars = []         # An array to store the characters into the ObjectChar class

def processImage():
    '''Take the user-inputted image and generate characters as well as a beginning context'''
    #charsAndContext = genCharAndContext()
    sampleOutput = """
        Name: Benjamin Banana
        Age Group: Adult
        Gender: Man
        Object: Banana
        Personality: Cheerful, optimistic
        Appearance: Bright yellow with a friendly smile

        Name: Amelia Apple
        Age Group: Teen
        Gender: Woman
        Object: Apple
        Personality: Ambitious, determined
        Appearance: Shiny red with a confident aura

        Beginning Prompt:
        On a small wooden table, a diverse group of fruits gathered. Benjamin Banana, the cheerful adult, and Amelia Apple, the ambitious teenager, stood side by side, among others who were yet to be named. Their vibrant colors and distinct personalities made each fruit unique, just like their presence around the table. As the narrator, I couldn't help but wonder what adventures awaited these fruits beyond the confines of this ordinary setting. Little did they know that fate had something extraordinary in store for them. It all started when a mischievous wind blew open the window, setting the stage for an unexpected journey that would forever change their lives.
        """
    
    sampleOutput = sampleOutput.strip()
    # Partition the output for just the characters
    partitionedOutput = sampleOutput.partition("Beginning Prompt")

    # List of individual characters
    objectChars = partitionedOutput[0].split("\n\n") # Might have an extra useless entry
    objectChars = objectChars[0:len(objectChars)-1]

    characterCount = 0
    # Loop through the first partition (the identified objects)
    for character in objectChars:
        # Create and save ObjectChar objects with the current character
        finalizedChars.append(setCharacter(character))
        finalizedChars[characterCount].voice = assignCharVoice(finalizedChars[characterCount])
        characterCount+=1

    # Print the current character's attributes and have the character introduce themself
    for character in finalizedChars:
        print("The current character's attributes are:")
        print(character.name,'/',character.gender,'/',character.ageGroup,'/',character.personality,'/',character.appearance,'/',character.voice)
        print()
        assignCharVoice(character)
        testAudio = generate(
            text = f"Hi! My name is {character.name}. It is a pleasure to meet you!",
            voice = character.voice.name
        )
        play(testAudio)

def setCharacter(character):
    '''Create ObjectChar objects to store the gpt-generated characters'''
    finalCharacter = ObjectChar("n/a", "n/a", "n/a", "n/a", "n/a", "n/a",) # An empty character to-be-filled
    charAttributes = character.split("\n")

    for attribute in charAttributes:
        attribute = attribute.strip(" ")
        attributeCategory = attribute.partition(":")[0]
        attributeValue = attribute.partition(":")[2].strip()

        # Rename the gpt-generated categories to names that match ObjectChar class variables
        if (attributeCategory == "Name"):
            attributeCategory = "name"
        elif (attributeCategory == "Age Group"):
            attributeCategory = "ageGroup"
        elif (attributeCategory == "Gender"):
            attributeCategory = "gender"
        elif (attributeCategory == "Personality"):
            attributeCategory = "personality"
        elif (attributeCategory == "Appearance"):
            attributeCategory = "appearance"

        setattr(finalCharacter,attributeCategory,attributeValue)

    return finalCharacter  

def assignCharVoice(character):
    '''Assign a voice to an input character'''
    charGender = character.gender # Man or Woman
    character.voice = selectVoice(charGender)

if __name__ == "__main__":
    processImage()
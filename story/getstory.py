import os
from openai import OpenAI
from getVoices import *
from ObjectChar import *

client = OpenAI(api_key="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")

background = """You are extraordinary at making captivating narratives in many genres, and as the creator of this immersive play, you shall craft a splendid interactive play in collaboration with the user.
	This story should also be intended to be read by children.
    Conclude each message with a request for open-ended input from the user, inviting them to actively contribute to the evolving storyline.
    Each paragraph must start with narrator if a character is not speaking.
	Designate each line with the corresponding character's name when engaged in dialogue, absolutely marking and distinguishing the Narrator when providing overarching commentary.
	Ensure a seamless transition between lines, initiating each segment with the relevant character's name or the Narrator as appropriate.
	Ensure that each paragraph is in the following style "[Character Name]: [Character Dialogue]."
    Do NOT include character dialogue in Narrator paragraphs. ONLY include them in their own paragraphs.
	Maintain the integrity of the narrative by disregarding any extraneous responses that could disrupt the seamless flow of the unfolding tale.
    Should the user's input lack coherence or fail to align with the narrative possibilities, tactfully bypass the incongruity and proceed with the storyline.
    Keep each section of the story to only a minimum number of lines of dialogue and do not make it too long.
	Limit the response to 200 tokens only.
    You must end the last paragraph with a period to create a full sentence.

    You will use the following characters in the story, and reiterate the following prompt as the beginning of the story:
    Characters: {
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
        }
    Beginning Prompt:
        On a small wooden table, a diverse group of fruits gathered. Benjamin Banana, the cheerful adult, and Amelia Apple, the ambitious teenager, stood side by side, among others who were yet to be named.
        Their vibrant colors and distinct personalities made each fruit unique, just like their presence around the table.
        As the narrator, I couldn't help but wonder what adventures awaited these fruits beyond the confines of this ordinary setting.
        Little did they know that fate had something extraordinary in store for them. It all started when a mischievous wind blew open the window, setting the stage for an unexpected journey that would forever change their lives.
    """ 
    # Background to tell Chat how to respond and act in the story choose 1
"""
You are an amazing talented storyteller who will create a fabulous interactive story with the user. 
At the end of each message you send ask the user for open-ended input to continue the story you are creating. 
Ignore all irrelevant responses to the storyline to prevent breaking the immersion of your story. 
If the user's response does not make sense or if the user's response does not fit what could happen ignore what the user said. 
You will label each line with the name of the current character that is speaking or Narrator if the narrator is speaking. 
The beginning of each line starts with the name of the currently speaking character and narrator otherwise. 
""" # Another Background to tell Chat how to respond and act in the story choose 1

def startStory(history):
    '''Get initial story response from GPT.'''
    print("Starting story.")

    response = client.chat.completions.create(                          # Get response
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": background}]+history,   # Sends background to get start of story
        max_tokens=500,                                                 # Max length of message
    )

    response_text = response.choices[0].message.content
    #print(f"The response is \n{response_text}\n")                       # Testing what response was
    return ([{"role": "assistant", "content": response_text}],response_text)
    
def continueStory(history):
    '''Continue story by getting additional responses from GPT.'''
    userinput = input("Enter a message ")
    message = [{"role": "user", "content": userinput}]
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": background}] + history + message,    # Sends all messages sent in conversation to keep history
        max_tokens=300,                                                              # Max length of message
    )

    response_text = response.choices[0].message.content
    #print(f"The response is \n{response_text}\n")                                    # Testing what the response was
    #print(f"Used {response.usage.prompt_tokens} tokens with message {userinput} and {response.usage.total_tokens} in total")     # Testing to keep track of how many tokens used
    
    return ([{"role": "assistant", "content": response_text}] + message, response_text)

def generateStory(characters):
    #print("Running.")
    # history = [{"role": "user", "content": "IMAGE_DESCRIPTION_FOR_START_OF_STORY"}] # History Records all previous messages from user and chat
    history = []    # Temporary
    #text = ""       # To store latest response from GPT
    text = ""
    
    """ Alt Output
    Narrator: On a small wooden table, a diverse group of fruits gathered. Benjamin Banana, the cheerful adult, and Amelia Apple, the ambitious teenager, stood side by side, among others who were yet to be named. Their vibrant colors and distinct personalities made each fruit unique, just like their presence around the table. As the narrator, I couldn't help but wonder what adventures awaited these fruits beyond the confines of this ordinary setting. Little did they know that fate had something extraordinary in store for them. It all started when a mischievous wind blew open the window, setting the stage for an unexpected journey that would forever change their lives.

    Narrator: The wind's playful dance swept across the room, causing a flurry of excitement among the fruits. Benjamin Banana's bright yellow peel fluttered in the air, and Amelia Apple's shiny red skin glowed with anticipation. They exchanged curious glances, wondering where the wind would take them. Suddenly, the wind whisked them off the table, lifting Benjamin and Amelia into the air.

    Benjamin Banana: Hold on tight, Amelia! We're going on an adventure!

    Amelia Apple: I'm ready, Benjamin! Let's see where this wind takes us!

    Narrator: As the wind carried them through the open window, Benjamin and Amelia saw the world outside their cozy little spot for the first time. The sky stretched endlessly above them, painted with streaks of orange and pink as the sun began to set. The wind gently guided them over fields of swaying grass, and they could hear the chirping of birds in the distance.

    Benjamin Banana: Look at that beautiful sunset, Amelia! It's like a painting in the sky.

    Amelia Apple: It's breathtaking, Benjamin. I never imagined we could see such wonders beyond our table.

    Narrator: The wind guided them further, and soon they found themselves soaring above a sparkling blue lake. The water shimmered as if sprinkled with a thousand tiny diamonds, and the gentle waves lapped against the shores.

    Benjamin Banana: How marvelous! The lake looks so inviting. I wish we could take a dip!

    Amelia Apple: That would be delightful, Benjamin. But we mustn't stray too far from the wind. After all, it's our guide on this magical journey.

    Narrator: As they continued to soar through the sky, Benjamin and Amelia marveled at the world below. They passed over towering mountains, where snow-capped peaks reached for the heavens. They
    """
    response, text = startStory(history)

    readStory(characters, text)
    '''
    history = history + response                            # Initialize story
    for i in range(5):
        response, text = continueStory(history=history)     # Get response 
        history = history + response                        # Build history
        print(f"The history is \n {history}")               # Print history
    '''
        
def readStory(characters, text):
    charVoiceDict = {}
    # Store character voices in a dictionary instead of a list for faster retrieval
    for character in characters:
        charVoiceDict[character.name] = character.voice.name
        #print(charVoiceDict[character.name])
    #print()
    #print(characters)

    # Instantitate the narrator
    narrator = ObjectChar("Narrator","Woman","DoesItMatter?","WhyDoYouCare?","You'reAwfullyCurious","Ella - Narrator")
    
    splitText = text.split("\n\n")                      # Split text into sections; list of sections
    for section in splitText:
        sectionComponents = section.partition(":")      # Partition section into names and dialogue (separated by colon)
        ''' Ideally GPT outputs 'Narrator:' as well so this section is not needed
        if (sectionComponents[2] == ""):                # In the case the partition never partitions anything
            currAudio = generate(
            text = text,                                # The text is just narrator text
            voice = narrator.voice                      # So set the voice to the narrator
            )
            play(currAudio)
            continue                                    # Skip rest of loop and move to next iteration
        '''
        currCharName = sectionComponents[0]             # Current character name
        currCharDialogue = sectionComponents[2]         # Current character dialogue
        '''currAudio = generate(
            text = currCharDialogue,                    
            voice = charVoiceDict[currCharName]         # Set the voice to the voice at the sepcified dictionary entry
        )
        play(currAudio)
        '''
        #print(currCharName, '/', currCharDialogue)
        #print()
    for line in splitText:
        print(line)

if __name__ == "__main__":
    generateStory()

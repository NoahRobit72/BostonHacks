import os
from openai import OpenAI
client = OpenAI(api_key="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")

background = """You are extraordinary at making captivating narratives in many genres, and as the creator of this immersive play, you shall craft a splendid interactive play in collaboration with the user. Conclude each message with a request for open-ended input from the user, inviting them to actively contribute to the evolving storyline. Each paragraph must start with narrator if a character is not speaking. Maintain the integrity of the narrative by disregarding any extraneous responses that could disrupt the seamless flow of the unfolding tale. Should the user's input lack coherence or fail to align with the narrative possibilities, tactfully bypass the incongruity and proceed with the storyline. This story should also be intended to be read by children.
      Designate each line with the corresponding character's name when engaged in dialogue, distinguishing the Narrator when providing overarching commentary. Ensure a seamless transition between lines, initiating each segment with the relevant character's name or the Narrator as appropriate Ensure every line starts with either a character name or Narrator if no character is speaking. Each paragraph must start with narrator if a character is not speaking 
      Keep each section of the story to only a minimum number of lines of dialogue and do not make it too long"""  # Background to tell Chat how to respond and act in the story choose 1

"""
You are an amazing talented storyteller who will create a fabulous interactive story with the user. 
At the end of each message you send ask the user for open-ended input to continue the story you are creating. 
Ignore all irrelevant responses to the storyline to prevent breaking the immersion of your story. 
If the user's response does not make sense or if the user's response does not fit what could happen ignore what the user said. 
You will label each line with the name of the current character that is speaking or Narrator if the narrator is speaking. 
The beginning of each line starts with the name of the currently speaking character and narrator otherwise. 
""" # Another Background to tell Chat how to respond and act in the story choose 1
  
  
def startStory(history):
  # get response from ChatGPT
  print("Starting story")
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": background}]+history, # Sends background to get start of story
    max_tokens=500, # max length of message
  )
  response_text = response.choices[0].message.content
  print(f"The response is \n{response_text}\n") # testing what the response was
  return ([{"role": "assistant", "content": response_text}],response_text)
  
def continueStory(history):
  userinput = input("Enter a message ")
  message = [{"role": "user", "content": userinput}]
  
  # get response from ChatGPT
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": background}] + history + message, # Sends all messages sent in conversation to keep history
    max_tokens=300, # max length of message
  )
  response_text = response.choices[0].message.content
  print(f"The response is \n{response_text}\n") # testing what the response was
  print(f"Used {response.usage.prompt_tokens} tokens with message {userinput} and {response.usage.total_tokens} in total") # testing to keep track of how many tokens used
  
  return ([{"role": "assistant", "content": response_text}] + message, response_text)

def main():
  print("Running")
  # history = [{"role": "user", "content": "IMAGE_DESCRIPTION_FOR_START_OF_STORY"}] # History Records all previous messages from user and chat
  history = [] # temporary
  text = "" # latest response from GPT
  response, text = startStory(history)
  history = history + response # initialize story
  for i in range(5):
    response, text = continueStory(history=history) # get response 
    history = history + response # build history
    print(f"The history is \n {history}") # print history
if __name__ == "__main__":
  main()

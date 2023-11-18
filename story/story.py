import os
from openai import OpenAI
client = OpenAI(api_key="YOURAPIKEY")

def main():
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
  )
  response_text = response.choices[0].message.content
  print(response_text)

if __name__ == "__main__":
    main()

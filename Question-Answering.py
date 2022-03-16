import openai
import keyboard
import json

key = input("please paste openai api key:")

openai.api_key = key

def main():
  context = input("input the topic that the question pertains to, to provide the ai with context:")
  question = input("please input the question you would like answered:")

  response = openai.Completion.create(
    engine="text-curie-001",
    prompt="Answer this question about"+context+"\n\n"+question,
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  print(response)  

main()

print('press esc to exit')
keyboard.add_hotkey('esc',exit())
import os
import requests

# Bard AI Session Key
bard_ai_session_key = os.environ['BARD_SESSION_KEY']
headers = { 'Authorization': 'Bearer {}'.format(bard_ai_session_key), 'Content-Type': 'text/plain' }

def bard_bot(prompt):
  print('prompt:', prompt)
  data = { "input": prompt }
  req = requests.post('https://api.bardapi.dev/chat', headers=headers, json=data)
  return req.json()['output']


# test only
def chatbot_test():
    prompt = input('Insert a prompt: ')
    print(bard_bot(prompt).strip())


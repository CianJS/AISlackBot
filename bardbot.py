import os
from bardapi import Bard

# Bard AI Session Key
bard_ai_session_key = os.environ['BARD_SESSION_KEY']
os.environ['_BARD_API_KEY'] = bard_ai_session_key


def bard_bot(prompt):
  bard = Bard(token=token)
  content = bard.get_answer(prompt)['content']
  return content


# test only
def chatbot_test():
    prompt = input('Insert a prompt: ')
    print(bard_bot(prompt).strip())


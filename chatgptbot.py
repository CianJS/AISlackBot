import os
import openai

# OpenAI API Key
openai_api_key = os.environ['SLACK_BOT_TOKEN']


def chat_gpt(prompt, api_key=openai_api_key):
    openai.api_key = api_key

    # chat-gpt models https://platform.openai.com/docs/models/overview
    # options: https://platform.openai.com/docs/api-reference/completions/create
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.2,
        max_tokens=2048,
        presence_penalty=-2,
        frequency_penalty=0
    )
    choices = completion.get('choices')
    return choices[0]['text']


# test only
def chatbot_test():
    prompt = input('Insert a prompt: ')
    print(chat_gpt(prompt).strip())


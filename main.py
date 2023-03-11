import os
import openai
from slack_sdk import rtm

# slack bot user token
bot_token = os.environ['OPENAI_API_KEY']
# OpenAI API Key
openai_api_key = os.environ['SLACK_BOT_TOKEN']
rtm_client = rtm.RTMClient(token=bot_token)


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


@rtm_client.run_on(event='message')
def chat_gpt_bot(**payload):
    data = payload.get('data')
    web_client = payload.get('web_client')
    if not (data and web_client):
        return 'Error'
    bot_id = data.get('bot_id', '')
    subtype = data.get('subtype', '')
    message = data.get('text', '')

    try:
        if bot_id == '' and subtype != 'bot_message':
            channel_id = data['channel']
            text = message.split('>')[-1].strip()

            response = chat_gpt(text)
            web_client.chat_postMessage(channel=channel_id, text=response)
    except Exception as err:
        print('Error:', err)


# test only
def chatbot_test():
    prompt = input('Insert a prompt: ')
    print(chat_gpt(prompt).strip())


if __name__ == '__main__':
    try:
        print('ChatGPT Bot running!')
        rtm_client.start()
        # chatbot_test()
    except Exception as err:
        print(err)

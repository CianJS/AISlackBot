import os
from slack_sdk import rtm
from chatgpt_bot import chat_gpt
from bard_bot import bard_bot
from slack_bot_api import get_channel_id, get_message_ts

# slack bot user token
bot_token = os.environ['SLACK_BOT_TOKEN']
rtm_client = rtm.RTMClient(token=bot_token)

# ChatGPT Bot
# @rtm_client.run_on(event='message')
# def chat_gpt_bot(**payload):
#     print(payload)
#     data = payload.get('data')
#     web_client = payload.get('web_client')
#     if not (data and web_client):
#         return 'Error'
#     bot_id = data.get('bot_id', '')
#     subtype = data.get('subtype', '')
#     message = data.get('text', '')

#     try:
#         if bot_id == '' and subtype != 'bot_message':
#             channel_id = data['channel']
#             text = message.split('>')[-1].strip()

#             response = chat_gpt(text)
#             web_client.chat_postMessage(channel=channel_id, text=response)
#     except Exception as err:
#         print('Error:', err)


# Bard Bot
@rtm_client.run_on(event='message')
def bard_chat_bot(**payload):
    data = payload.get('data')
    web_client = payload.get('web_client')
    if not (data and web_client):
        return 'Error'
    bot_id = data.get('bot_id', '')
    subtype = data.get('subtype', '')
    message = data.get('text', '')
    channel_id = get_channel_id(web_client)

    try:
        message_ts = get_message_ts(web_client, channel_id, message)
        if bot_id == '' and subtype != 'bot_message':
            if not channel_id:
                channel_id = data['channel']
            text = message.split('>')[-1].strip()

            response = bard_bot(text)
            web_client.chat_postMessage(channel=channel_id, thread_ts=message_ts, text=response)
    except Exception as err:
        print('bard_chat_bot error:', err)


# test only
def chatbot_test():
    prompt = input('Insert a prompt: ')
    # print(chat_gpt(prompt).strip())
    print(bard_bot(prompt).strip())


if __name__ == '__main__':
    try:
        print('ChatGPT Bot running!')
        rtm_client.start()
        # chatbot_test()
    except Exception as err:
        print("Main Error:", err)

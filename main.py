import os
from slack_sdk import rtm
from chatgptbot import chat_gpt
from bardbot import bard_bot

# slack bot user token
bot_token = os.environ['OPENAI_API_KEY']
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

def get_channel_id(client):
    result = client.conversations_list(limit=1000)
    channels = result.data['channels']
    channel = list(filter(lambda c: c["name"] == "chatgpt-test-room", channels))[0]
    channel_id = channel["id"]
    return channel_id


def get_message_ts(client, channel_id, query):
    result = client.conversations_history(channel=channel_id)
    messages = result.data['messages']
    print(messages)
    message = list(filter(lambda m: m["text"]==query, messages))[0]
    message_ts = message["ts"]
    return message_ts


# Bard Bot
@rtm_client.run_on(event='message')
def bard_chat_bot(**payload):
    print('payload:', payload)
    data = payload.get('data')
    web_client = payload.get('web_client')
    if not (data and web_client):
        return 'Error'
    bot_id = data.get('bot_id', '')
    subtype = data.get('subtype', '')
    message = data.get('text', '')
    channel_id = get_channel_id(web_client)
    print(channel_id)

    try:
        if bot_id == '' and subtype != 'bot_message':
            if not channel_id:
                channel_id = data['channel']
            text = message.split('>')[-1].strip()

            response = bard_bot(text)
            web_client.chat_postMessage(channel=channel_id, text=response)
    except Exception as err:
        print('Error:', err)


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
        print(err)

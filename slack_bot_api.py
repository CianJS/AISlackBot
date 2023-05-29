channel_name = "chatgpt-test-room"

def get_channel_id(client):
    result = client.conversations_list(limit=1000)
    channels = result.data['channels']
    channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
    channel_id = channel["id"]
    return channel_id


def get_message_ts(client, channel_id, query):
    result = client.conversations_history(channel=channel_id)
    messages = result.data['messages']
    message = list(filter(lambda m: m["text"]==query, messages))[0]
    message_ts = message["ts"]
    return message_ts
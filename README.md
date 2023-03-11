# ChatGPT SlackBot

Slackbot using the ChatGPT API

## Installation

```bash
pip install -r requirements.txt
```

### Setting Environment Variables

OpenAI API Key: [link](https://platform.openai.com/account/api-keys)
Slack Bot User Token: [link](https://api.slack.com/apps)

```bash
> vi ~/.bash_profile(or ~/.zshrc)

export OPENAI_API_KEY={openai api key}
export SLACK_BOT_TOKEN={slack bot token}
```

and

```bash
> source ~/.bash_profile(or ~/.zshrc)
```

## Running

```bash
python main.py
```

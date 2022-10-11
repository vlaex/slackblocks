# slackblocks


![PyPI - License](https://img.shields.io/pypi/l/slackblocks)

This is a fork of [**this**](https://github.com/nicklambourne/slackblocks) awesome package made by @nicklambourne.

<hr>

`slackblocks` is a Python API for building messages in the fancy new Slack Block Kit API.

_This package requires `Python 3.10`_

## Installation

```bash
pip install git+https://github.com/vlaex/slackblocks.git
```

## Usage

```python
from slackblocks import Message, SectionBlock


block = SectionBlock("Hello, world!")
message = Message(blocks=block)
message.json()

```

Will produce the following JSON string:
```json
{
    "blocks": [
        {
            "type": "section",
            "block_id": "992ceb6b-9ad4-496b-b8e6-1bd8a632e8b3",
            "text": {
                "type": "mrkdwn",
                "text": "Hello, world!",
                "verbatim": false
            }
        }
    ]
}
```
which can be sent as payload to the Slack message API HTTP endpoints.

You can unpack the objects directly into 
the Python Slack Client in order to send messages:
```python
from os import environ
from slack import WebClient
from slackblocks import Message, SectionBlock


client = WebClient(token=environ["SLACK_API_TOKEN"])
block = SectionBlock("Hello, world!")
message = Message(channel="#general", blocks=block)

response = client.chat_postMessage(**message)
```

Note the `**` operator in front of the `message` object.

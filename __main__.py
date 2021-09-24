"""
slack poster


"""

import os

from slack_sdk import WebClient

token = os.environ.get('SLACK_TOKEN')

assert token, "missing slack token"

slack = WebClient(token=token)

message = {
  "channel": "C02405Q7TTP",
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "It is Friday, my dudes"
			}
		},
		{
			"type": "image",
			"image_url": "https://lunchaware.com/static/friday.jpg",
			"alt_text": "friday"
		}
	]
}

slack.chat_postMessage(**message)

import os
import sys
import json

import requests
import urllib2
from flask import Flask, request

app = Flask(__name__)


@app.route('/bot', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    token = request.args.get('hub.verify_token')
    if token == "123":
        return request.args.get('hub.challenge')
    else:
        return "error"


@app.route('/bot', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events
    data = request.get_json()
##  print data
    log(data)  # you may not want to log every incoming message in production, but it's good for testing
##  value=request.data
##  jsonResponse=json.loads(value)
##  jsonData=jsonResponse["message"]["text"]
##  print jsonData
    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text
                    process_message(message_text,sender_id)

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass


    return "ok", 200


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": 'EAAZAgx2FZBzKoBABUy3DpkGUvZAiKT6xNiqVHhFE4viZBiCaN4ktbQhQWZB6w3YczvSLcYANy4TLQ8fZCo8Fcp0Y6nJZC0DigbNoyo4zcnxCQqXHv0Yh38m7FC06IobFa7aZCZAvTvGk3aokydyJxQRKwnuuZCZC37PigrpOGTT4JMF8JwZAqlUnYZBvX'
    }
    headers = {
        "Content-Type": "application/json"
    }
    if "template" in message_text:
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "list",
                        "top_element_style": "compact",
                        "elements": [
                            {
                                "title": "Classic White T-Shirt",
                                "image_url": "https://peterssendreceiveapp.ngrok.io/img/white-t-shirt.png",
                                "subtitle": "100% Cotton, 200% Comfortable",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://peterssendreceiveapp.ngrok.io/view?item=100",
                                    "messenger_extensions": true,
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                },
                                "buttons": [
                                    {
                                        "title": "Buy",
                                        "type": "web_url",
                                        "url": "https://peterssendreceiveapp.ngrok.io/shop?item=100",
                                        "messenger_extensions": true,
                                        "webview_height_ratio": "tall",
                                        "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                    }
                                ]
                            },
                            {
                                "title": "Classic Blue T-Shirt",
                                "image_url": "https://peterssendreceiveapp.ngrok.io/img/blue-t-shirt.png",
                                "subtitle": "100% Cotton, 200% Comfortable",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://peterssendreceiveapp.ngrok.io/view?item=101",
                                    "messenger_extensions": true,
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                },
                                "buttons": [
                                    {
                                        "title": "Buy",
                                        "type": "web_url",
                                        "url": "https://peterssendreceiveapp.ngrok.io/shop?item=101",
                                        "messenger_extensions": true,
                                        "webview_height_ratio": "tall",
                                        "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                    }
                                ]
                            },
                            {
                                "title": "Classic Black T-Shirt",
                                "image_url": "https://peterssendreceiveapp.ngrok.io/img/black-t-shirt.png",
                                "subtitle": "100% Cotton, 200% Comfortable",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://peterssendreceiveapp.ngrok.io/view?item=102",
                                    "messenger_extensions": true,
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                },
                                "buttons": [
                                    {
                                        "title": "Buy",
                                        "type": "web_url",
                                        "url": "https://peterssendreceiveapp.ngrok.io/shop?item=102",
                                        "messenger_extensions": true,
                                        "webview_height_ratio": "tall",
                                        "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                    }
                                ]
                            },
                            {
                                "title": "Classic Gray T-Shirt",
                                "image_url": "https://peterssendreceiveapp.ngrok.io/img/gray-t-shirt.png",
                                "subtitle": "100% Cotton, 200% Comfortable",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
                                    "messenger_extensions": true,
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                },
                                "buttons": [
                                    {
                                        "title": "Buy",
                                        "type": "web_url",
                                        "url": "https://peterssendreceiveapp.ngrok.io/shop?item=103",
                                        "messenger_extensions": true,
                                        "webview_height_ratio": "tall",
                                        "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                    }
                                ]
                            }
                        ],
                         "buttons": [
                            {
                                "title": "View More",
                                "type": "postback",
                                "payload": "payload"
                            }
                        ]
                    }
                }
            }
        })
    else:
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        })
    print data
##  value=request.data
##  output=''
##  jsonResponse=json.loads(data)
##  jsonData = jsonResponse['message']['text']
##  if ("block" in jsonData.lower()):
##      output='card blocked'
##  print output

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    return r.status_code;

def process_message(text,sender_id):
    text=text.lower()
    if "hi" in text:
        send_message(sender_id, "Hi,How can I help you?")
    elif "block" in text:
        if "not" not in text and "dont" not in text and "unblock" not in text:
            send_message(sender_id, "Your card has been blocked successfully.")
        else:
            send_message(sender_id, "Your card will not be blocked.")
    elif "activate" in text and "card" in text:
        send_message(sender_id, "Card has been Activated")
    elif "last" in text and "transaction" in text:
        send_message(sender_id, "template")
    elif "cancel" in text and "transaction" in text:
           if "not" not in text and "dont" not in text:
               send_message(sender_id, "Your last transaction has been cancelled")
           else:
               send_message(sender_id, "Your last transaction will not be cancelled")
    else:
        send_message(sender_id, "Sorry.I am not able to understand.I'll call you")



def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)

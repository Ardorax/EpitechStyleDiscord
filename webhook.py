import datetime
import os
import requests
from json import JSONDecoder

def send_webhooks(Checker, url, color: int, file: str):
    payload = {'embeds': [
        {"title": "Votre résultat de moulinette :", "color": color, "fields": [
            {"name": "MAJOR", "value": Checker["MAJOR"], "inline": True},
            {"name": "MINOR", "value": Checker["MINOR"], "inline": True},
            {"name": "INFO", "value": Checker["INFO"], "inline": True}]
        }
    ]}

    response = requests.post(url, json=payload)
    handle_response(response)
    response = requests.post(url, data={}, files={'upload_file': open(file, "rb")})
    file.close()
    handle_response(response)

def handle_response(response):
    print("Send Webhooks !")
    if response.status_code >= 400:
        print('Discord Webhook Action failed to execute webhook. Discord docs : https://discord.com/developers/docs/resources/webhook#execute-webhook')
        exit(1)

if __name__ == "__main__":
    summary = os.environ["INPUT_SUMMARY"]
    print(summary)
    trace = os.environ["INPUT_TRACE"]
    print(trace)
    url = os.environ["INPUT_URL"]
    print(url)
    username = os.environ["INPUT_USERNAME"]
    print(username)
    json_summary = JSONDecoder().decode(summary)
    color = os.environ["INPUT_COLOR"]
    print(color)
    send_webhooks(json_summary, url, int(color), trace)

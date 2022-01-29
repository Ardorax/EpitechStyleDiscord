import datetime
import os
import re
import requests
from json import JSONDecoder

def send_webhooks(Checker, url, color: int, file_path: str, desc: str,
    name: str = "Normeur"):
    payload = {"username": name, "description": desc , 'embeds': [
        {"title": "Votre résultat de moulinette :", "color": color, "fields": [
            {"name": "MAJOR", "value": Checker["major"], "inline": True},
            {"name": "MINOR", "value": Checker["minor"], "inline": True},
            {"name": "INFO", "value": Checker["info"], "inline": True}]
        }
    ]}

    # Send to Discord
    response = requests.post(url, json=payload)
    handle_response(response)
    file = open(file_path, "rb")
    response = requests.post(url, data={}, files={'upload_file': file})
    file.close()
    handle_response(response)

def handle_response(response):
    print("Send Webhooks !")
    if response.status_code >= 400:
        print('Discord Webhook Action failed to execute webhook. Discord docs : https://discord.com/developers/docs/resources/webhook#execute-webhook')
        exit(1)

if __name__ == "__main__":
    # Import github var
    summary = os.environ["INPUT_SUMMARY"]
    trace = os.environ["INPUT_TRACE"]
    url = os.environ["INPUT_URL"]
    username = os.environ["INPUT_USERNAME"]
    color = os.environ["INPUT_COLOR"]
    desc = os.environ["INPUT_DESCRIPTION"]

    print(os.environ["GITHUB_REPOSITORY_OWNER"])
    json_summary = JSONDecoder().decode(summary)
    send_webhooks(json_summary, url, int(color), trace, username)

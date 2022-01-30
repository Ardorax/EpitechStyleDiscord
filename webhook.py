import os
import requests
from json import JSONDecoder

def send_webhooks(Checker, url, color: int, file_path: str, desc: str,
    name: str = "Normeur"):
    payload = {"username": name, 'embeds': [
        {"title": "Votre résultat de moulinette :", "color": color,
        "description": desc, "fields": [
            {"name": "MAJOR", "value": Checker["major"], "inline": True},
            {"name": "MINOR", "value": Checker["minor"], "inline": True},
            {"name": "INFO", "value": Checker["info"], "inline": True}]
        }
    ]}

    # Send to Discord
    files_list = create_files(file_path)
    print(files_list)
    response = requests.post(url, json=payload)
    handle_response(response)
    response = requests.post(url, data={"username": name}, files=files_list)
    handle_response(response)
    for key in files_list:
        files_list[key].close()

def create_files(file_path: str) -> dict:
    files = file_path.split(";")
    total = len(files)
    result = {}
    if total > 10:
        total = 10
    for i in range (total):
        result[files[i]] = open(files[i], "rb")


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
    print(desc)
    try:
        print(os.environ["INPUT_FILES"])
    except KeyError:
        pass
    print(os.environ["GITHUB_REPOSITORY_OWNER"])
    json_summary = JSONDecoder().decode(summary)
    send_webhooks(json_summary, url, int(color), trace, desc, username)

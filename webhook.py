import datetime
import json
import os
import requests
from json import JSONDecoder

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
    print(json_summary["major"])

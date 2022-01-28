import datetime
import json
import os
import requests
from json import JSONDecoder

if __name__ == "__main__":
    summary = os.environ["INPUT_SUMMARY"]
    trace = os.environ["INPUT_TRACE"]
    print(trace)
    json_summary = JSONDecoder().decode(summary)
    print(json_summary["major"])

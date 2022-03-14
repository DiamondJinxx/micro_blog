import os
import requests

from server import hello_name

def get_secret_message():
    # url = os.environ["SECRET_URL"]
    url = "http://127.0.0.1:5683/index"
    responce = requests.get(url)
    print(f"The secret message is {responce.text}")
    hello = hello_name

def get_index():
    url = "http://127.0.0.1:5683/index"
    responce = requests.get(url)

if __name__ == "__main__":
    get_secret_message()

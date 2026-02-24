# Simple script for hitting the `/chat` endpoint.
# You can use either `requests` (sync) or `httpx` (sync/async) depending on preference.

import json

try:
    import httpx
    client = httpx
    use_httpx = True
except ImportError:
    import requests
    client = requests
    use_httpx = False

# configure request
url = "http://127.0.0.1:5000/chat"
data = {"message": "What are my skills?"}
headers = {"Content-Type": "application/json"}

try:
    if use_httpx:
        print("Using httpx client")
        response = client.post(url, json=data, headers=headers)
    else:
        print("Using requests client")
        response = client.post(url, json=data, headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")

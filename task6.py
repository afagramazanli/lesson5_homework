
import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("API_BASE_URL")

data = {
    "title": "Learning Python APIs",
    "body": "This is my homework request",
    "userId": 4
}

response = requests.post(f"{base_url}/posts", json=data)

print("Status code:", response.status_code)
print("Response:", response.json())

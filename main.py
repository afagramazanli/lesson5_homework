import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("API_BASE_URL")

print(base_url)

response = requests.get(f"{base_url}/users/99999")

if response.status_code == 200:

    user = response.json()

    print("Name:", user["name"])

    print("Username:", user["username"])

    print("Email:", user["email"])

    print("City:", user["address"]["city"])
else: 
    print("user tapilmadi. ")    
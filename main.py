import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("API_BASE_URL")


user_id = input("User ID daxil edin: ")
response = requests.get(f"{base_url}/users/{user_id}")
print(response.status_code)
if response.status_code == 200:

    user = response.json()

    print("Name:", user["name"])

    print("Username:", user["username"])

    print("Email:", user["email"])

    print("City:", user["address"]["city"])
else: 
    print("user tapilmadi. ")    


print("Program finished")
# importing the requests library
import requests
import json

# api-endpoint
URL = "https://cniyl5hf4nr7qy6m4bkhjclfii0umqoh.lambda-url.us-east-2.on.aws/"

fname = input("Please provide your first name: ")
lname = input("Please provide your last name: ")

print("Formatting json...")
BODY = { 
    "Data": [
        {
            "first_name":fname,
            "last_name":lname
        }
    ]
}

print("Request formatted. Sending to Lambda...")
r = requests.get(url = URL, json=BODY)
print("Response recieved.")
print(str(r) + "\n")

data = r.json()

print(data)
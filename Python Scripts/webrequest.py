# importing the requests library
import requests
import json

# api-endpoint
# URL = "https://cniyl5hf4nr7qy6m4bkhjclfii0umqoh.lambda-url.us-east-2.on.aws/"
URL = "https://wu003u1jrj.execute-api.us-east-2.amazonaws.com/"

def main():
    user_input = input("What do you want to do: ")
    if(user_input == "0"):
      say_hi()
    elif(user_input == "1"):
       greet()

def say_hi():
    send_request(URL + "say_hi", "")

def greet():
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
    send_request(URL + "greeting", BODY)

def send_request(newURL, newBody):
    print("Request formatted. Sending to Lambda...")
    r = requests.get(url = newURL, json=newBody)
    print("Response recieved.")
    print(str(r) + "\n")

    data = r.json()

    print(data)

if(__name__ == "__main__"):
   main()
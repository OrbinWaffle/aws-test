# importing the requests library
import requests
import json

# api-endpoint
# URL = "https://cniyl5hf4nr7qy6m4bkhjclfii0umqoh.lambda-url.us-east-2.on.aws/"
URL = "https://ovz97nwwca.execute-api.us-east-1.amazonaws.com/"

def main():
    # say_hi()
    get_restaurant()
    # user_input = input("What do you want to do: ")
    # if(user_input == "0"):
    #     say_hi()
    # elif(user_input == "1"):
    #     greet()

def get_restaurant():
    BODY = {
        "restaurants": [
            {
            "name": "your mom's shack",
            "rating": "5"
            },
            {
            "name": "Panda Wok",
            "rating": "2"
            }
        ]
    }
    send_request(URL + "GetRestaurantReccomendation", BODY)

def say_hi():
    send_request(URL + "HelloWorld", "")

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
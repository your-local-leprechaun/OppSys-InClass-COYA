import requests
import time, sys

API_URL = "https://adventure-api-673835650363.us-west1.run.app"
ADVENTURE_NAME = "brookmere-may6-0704pm"
init_url = f"{API_URL}/init"
nar_url = f"{API_URL}/narrate"
choice_url = f"{API_URL}/choice"

# Functions to write shit out yeehaw
def typeout(string, delay=0.02):
    for char in string:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_narration(page, narration):
    print()
    print(f"Page {page}")
    typeout(narration)
    print()

def print_choices(choices):
    for choice in choices:
        if choice["narration"] == "":
            print(choice["original_choice_text"])
            break
        print(choice["narration"])

def make_choice(choice):
    data = {
        "session_id":session_id,
        "choice":choice
    }
    response = requests.post(choice_url, headers=headers, json=data)



typeout("-- Starting Adventure Game --")

# Grab session ID
headers = {"Content-Type":"application/json"}
data = {"adventure_name":ADVENTURE_NAME}
response = requests.post(init_url, headers=headers, json=data)

if response.status_code != 200:
    print("API URL Failed! Exiting game")
    quit()

session_id = response.json()["session_id"]

# Start doing shit
data = {
    "session_id" : session_id
}
while True:
    response = requests.post(nar_url, json=data, headers=headers)

    response = response.json()
    print_narration(response["current_node"], response["narrated_scene"]["narration"])
    print_choices(response["narrated_scene"]["choices"])
    # print(response["narrated_scene"]["choices"])

    choice = input("> ")

    if choice.upper() == 'X':
        print("Thanks for playing!")
        quit()

    make_choice(choice)

from flask import Flask, request, render_template
import os, json

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

def getUserIndex(data, username):
    for i in range(len(data["users"])):
        if data["users"][i]["name"]["username"] == username:
            return i
    else:
        return None

def addNewUser(userData):
    with open(r'users.json', 'r+') as outfile:
        if not os.stat("users.json").st_size:
            data = {"users":[]}
            data["users"].append(userData)
            json.dump(data, outfile, indent=4)
        else:
            data = json.load(outfile)
            data["users"].append(userData)
            outfile.seek(0)
            json.dump(data, outfile, indent=4)

def makeUser(username, password, firstName, lastName, bio):
    user = { #make user JSON object
        "name": {
            "username": username,
            "firstName": firstName,
            "lastName": lastName
        },
        "target":"Picked December First",
        "password": password, #password encrypted with sha256 making it uncrackable
        "bio": bio
    }
    return user

addNewUser(makeUser("evanator", "5612732163", "evan", "watson", "my name is evan"))

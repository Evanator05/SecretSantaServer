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
    file = open("users.json", "r+")

    if os.stat("users.json").st_size == 0:
        template = {"users":[]}
        file.write(json.dumps(template))

    userList = file.read()
    userList = json.loads(userList)
    userList["users"].append(userData)
    file.truncate()
    file.write(json.dumps(userList))
    print(userList)
    file.close()

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

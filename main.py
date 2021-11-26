from flask import Flask, request, render_template

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

def addNewUser():
    file = open("users.json", "w+")

    

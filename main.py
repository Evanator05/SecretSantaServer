from flask import Flask, request
from netcode import addUser

app = Flask(__name__)
@app.route('/', methods=['POST'])

def result():
    addUser.addNewUser(request.form)

if __name__ == "__main__":
    app.run(debug=True, port=6969)

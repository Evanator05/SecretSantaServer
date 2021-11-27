from flask import Flask, request
from netcode import addUser

app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    addUser.addNewUser(request.form)
    return 'Received !' # response to your request.

if __name__ == "__main__":
    app.run(debug=True)

from models import *
# from control import control
from flask import Flask
import random as r

# FLASK SETUP
app = Flask(__name__)

# MAIN APP LOGIC HERE

@app.route('/')
# def hello_world():
#     return "Hello, world!"
def main():
    user_ids = []
    def create_user_id():
        user_id = int(r.randint(1000000,10000000))
        while user_id in user_ids:
            user_id = int(r.randint(1000000,10000000))
        user_ids.append(user_id)
        return user_id
    clientId = create_user_id()
    firstName, lastName = "Daniel", "Osadtsuk"
    newClient = client.Client(firstName, lastName, clientId)
    # print(f"{firstName} {lastName}'s user id is {clientId}")
    # return newClient
    return f"{firstName} {lastName}'s user id is {clientId}"


if __name__ == "__main__":
    app.run(debug=True)
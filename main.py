from models import *
import flask

# FLASK SETUP
app = Flask(__name__)

# MAIN APP LOGIC HERE

def user_id():
    
    user_id = int(r.randint(1000000,10000000))
    while user_id in user_ids:
        user_id = int(r.randint(1000000,10000000))
    user_ids.append(user_id)
    return user_id

def create_user(firstName, lastName):
    clientId = user_id()
    newUser = client.Client(firstName, lastName, clientId)
    print(f"{firstName} {lastName}'s user id is {clientId}")

if __name__ == "__main__":
    app.run(debug=True)
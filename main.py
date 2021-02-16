from models import *
import flask
import random as r

# FLASK SETUP
app = Flask(__name__)

# MAIN APP LOGIC HERE

user_ids = []
event_ids = []

def create_user_id():
    user_id = int(r.randint(1000000,10000000))
    while user_id in user_ids:
        user_id = int(r.randint(1000000,10000000))
    user_ids.append(user_id)
    return user_id

def create_event_id():
    event_id = int(r.randint(1000000,10000000))
    while event_id in event_ids:
        event_id = int(r.randint(1000000,10000000))
    event_ids.append(event_id)
    return event_id

def create_client(firstName, lastName):
    clientId = create_user_id()
    newClient = client.Client(firstName, lastName, clientId)
    # print(f"{firstName} {lastName}'s user id is {clientId}")
    return newClient

def create_event(client):
    eventId = create_event_id()
    categories = ["wedding","engagement","family","commercial","headshot"]
    eventCategory = r.choice(categories)
    newEvent = event.Event(eventCategory, eventId, client)

def create_date(yyyy,mm,dd,event,client):
    newDate = date.Date(yyyy,mm,dd,event,client)

if __name__ == "__main__":
    app.run(debug=True)
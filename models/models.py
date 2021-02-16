import random as r
from datetime import date, datetime, timedelta
import calendar

user_ids = []

class Client():
    def __init__(self, firstName, lastName, clientId):
        self.firstName = firstName
        self.lastName = lastName
        self.email = None
        self.address = None
        self.clientId = clientId
    
    def update_price(self, newPrice):
        oldPrice = self.price
        self.price = newPrice
        priceDiff = float(newPrice - oldPrice)
        return self.price


class Event:
    def __init__(self, category, eventId):
        self.cat = category
        self.eventId = eventId

    def isWedding(self):
        if self.cat == "wedding":
            return True
        else:
            return False
    
    def isEngagement(self):
        if self.cat == "engagement":
            return True
        else:
            return False

class Date:

    # SET FIRST DAY OF THE WEEK TO SUNDAY
    calendar.setfirstweekday(6)

    def __init__(self, yyyy, mm, dd):
        self.year = yyyy
        self.month = mm
        self.day = dd
        self.date = date.fromisoformat(f'{yyyy}-{mm}-{dd}')

    def isBooked(self):
        # IF DATE IS UNAVAILABLE, RETURN TRUE
        # IF DATE IS AVAILABLE, RETURN FALSE
        pass

    def fromDate(self):
        # HOW MUCH TIME HAS PASSED SINCE THE DATE
        todaysDate = date.today()
        pass

    def toDate(self):
        # HOW MUCH TIME BEFORE THE DATE
        todaysDate = date.today()
        pass

############################################
############################################
############################################

def user_id():
    
    user_id = int(r.randint(1000000,10000000))
    while user_id in user_ids:
        user_id = int(r.randint(1000000,10000000))
    user_ids.append(user_id)
    return user_id

def create_user(firstName, lastName):
    clientId = user_id()
    newUser = Client(firstName, lastName, clientId)
    print(f"{firstName} {lastName}'s user id is {clientId}")

############################################
############################################
############################################

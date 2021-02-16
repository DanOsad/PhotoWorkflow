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
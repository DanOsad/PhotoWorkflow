class Event():
    def __init__(self, category, event, client):
        self.client = client
        self.cat = category
        self.id = event.id

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
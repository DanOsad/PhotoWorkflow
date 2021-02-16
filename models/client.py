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
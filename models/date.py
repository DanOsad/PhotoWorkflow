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
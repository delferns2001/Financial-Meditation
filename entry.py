

class ShoppingListEntry:

    def __init__(self, name="Default", date="Default", time="Default", value=0, quantity=0):
        self.name = name
        self.date = date
        self.time = time
        self.value = value
        self.quantity = quantity

    def showData(self):
        print("name: " + str(self.name))
        print("date: " + str(self.date))
        print("value: " + str(self.value))
        print("quantity: " + str(self.quantity))

    def getName(self):
        return(self.name)

    def getDate(self):
        return(self.date)

    def getValue(self):
        return(self.value)

    def getQuantity(self):
        return(self.quantity)

    def setName(self, name):
        self.name = name

    def setDate(self, date):
        self.date = date

    def setValue(self, value):
        self.value = value

    def setQuantity(self, quantity):
        self.quantity = quantity

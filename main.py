from SqliteHandling import ConnectToSqlite
from entry import ShoppingListEntry
from datetime import datetime


class SqlChecker():

    def __init__(self):
        self.sqlhandler = ConnectToSqlite()
        self.datetime = datetime.now()
        self.date = self.datetime.date()
        self.time = self.datetime.strftime("%H:%M:%S")

        # print("--------------------Summary----------------------------")
        # print("------------------------------------------------------")
        # print("| Total Money Spent So Far: ",
        #       self.getTotalMoneySpent(), "|")
        # print("| Total items bought So Far: " +
        #       str(self.getTotalItemsBought())+"|")
        # print("------------------------------------------------------")

        print(
            "------------------------------------------------------------------------------")
        self.printData()
        print(
            "------------------------------------------------------------------------------")
        print("Total Spent: ")
        self.getTotalMoneySpent()
        print("Total Items Bought: ")
        self.getTotalItemsBought()

        self.sqlhandler.closeConnection()

    def addEntry(self, name, value, quantity):
        entry = ShoppingListEntry(
            name, str(self.date), str(self.time), value, quantity)
        self.sqlhandler.add_entry(entry)

    def printData(self):
        data = self.sqlhandler.get_all_entries()
        print('{0:2s} {1:30s} {2:10s} {3:10s} {4:10s} {5:10s}'.format(
            "Id", "Item", "Date", "Time", "Price", "Quantity"))
        for entity in data:
            # print(entity)
            print('{0:2d} {1:30s} {2:10s} {3:10s} {4:5f} {5:6d}'.format(
                entity[0], entity[1], entity[2], entity[3], entity[4], entity[5]))

    def deleteEntry(self, name):

        try:
            self.sqlhandler.remove_entry(name)
        except:
            print("error")

    def getTotalMoneySpent(self):
        data = self.sqlhandler.get_all_entries()
        total = 0
        for entity in data:
            total = total + entity[4]
        print(total)

    def getTotalItemsBought(self):
        data = self.sqlhandler.get_all_entries()
        total = 0
        for entity in data:
            total = total + entity[5]
        print(total)


SqlChecker()

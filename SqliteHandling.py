import sqlite3
from tkinter import W
# conn = sqlite3.connect(':memory:')


class ConnectToSqlite:

    def __init__(self) -> None:
        self.conn = sqlite3.connect('spanding.db')
        self.c = self.conn.cursor()
    
    def add_entry(self, entry):
        with self.conn:
            self.c.execute("INSERT INTO spandingRecord VALUES (:id, :name, :date, :time, :value, :quantity)", {
                "id": None, "name": entry.name, "date": entry.date, "time": entry.time,"value": entry.value, "quantity": entry.quantity})

    def remove_entry(self, name):
        with self.conn:
            self.c.execute("DELETE from spandingRecord WHERE name = :name ",
                           {'name': name})

    def get_all_entries(self):
        self.c.execute("SELECT * FROM spandingRecord")
        return self.c.fetchall()

    def get_entries_by_name(self, name):
        self.c.execute("SELECT * FROM spandingRecord WHERE name=:name", {'name': name})
        return self.c.fetchall()

    def closeConnection(self):
        self.conn.commit()
        self.conn.close()

# def update_entry(name, pay):
#     with conn:
#         c.execute("""UPDATE Pushup SET pay = :pay
#                     WHERE first = :first AND last = :last""",
#                   {'first': emp.first, 'last': emp.last, 'pay': pay})

# entry1 = PushupDataEntry("david", "highly effective", 10, 4140, 1)
# insert_entry(entry1)
# print(entry1.__repr__())


# entry2 = PushupDataEntry("twidle", "highly effective", 10, 3240, 1)
# insert_entry(entry2)
# print(entry2.__repr__())

# for i in (get_all_entries()):
#     print(i)

# print(get_entries_by_name("twidle"))
# remove_entry("david")

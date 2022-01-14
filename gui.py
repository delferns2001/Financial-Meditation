from tkinter import StringVar, Tk, Frame
from tkinter.ttk import Entry, Label, Button
from SqliteHandling import ConnectToSqlite
from entry import ShoppingListEntry
from datetime import datetime


class GUI:
    def __init__(self, master=None):
        self.form = Frame(master, highlightbackground="green", highlightcolor="green",
                          highlightthickness=10, bg="orange", width=100, height=100, bd=0)
        self.form.pack(fill='both', side='left', expand='True')

        self.shoppingBusket = Frame(master, highlightbackground="red",
                                    highlightcolor="red", highlightthickness=10, width=100, height=100, bd=0)
        self.shoppingBusket.pack(fill='both', side='right', expand='True')

        self.name = StringVar()
        self.value = StringVar()
        self.quantity = StringVar()

        self.l_name = Label(self.form, text="Name", background="orange")
        self.e_name = Entry(self.form, textvariable=self.name)
        self.l_value = Label(self.form, text="Value", background="orange")
        self.e_value = Entry(self.form, textvariable=self.value)
        self.l_quantity = Label(
            self.form, text="Quantity", background="orange")
        self.e_quantity = Entry(
            self.form, textvariable=self.quantity)
        self.b_submit = Button(self.form, text="submit",
                               command=self.onSubmit)

        self.l_name.pack()
        self.e_name.pack()
        self.l_value.pack()
        self.e_value.pack()
        self.l_quantity.pack()
        self.e_quantity.pack()
        self.b_submit.pack(pady=20)

        self.datetime = datetime.now()
        self.date = self.datetime.date()
        self.time = self.datetime.strftime("%H:%M:%S")

    def onSubmit(self):
        print("name: " + str(self.name.get()))
        print("value: " + str(self.value.get()))
        print("quantity: " + str(self.quantity.get()))

        self.CreateShoppingBasketItem()
        self.saveEntry()
        self.resetValues()

    def resetValues(self):
        self.e_name.delete(0, "end")
        self.e_value.delete(0, "end")
        self.e_quantity.delete(0, "end")

    def CreateShoppingBasketItem(self):

        count = len(self.shoppingBusket.winfo_children()) + 1
        label = Label(
            self.shoppingBusket, text=f"{count}. Name: {self.name.get()}, Value: {self.value.get()}, Quantity: {self.quantity.get()}")
        label.pack(side="top")

    def saveEntry(self):
        sqlhandler = ConnectToSqlite()

        entry = ShoppingListEntry(
            self.name.get(), str(self.date), str(self.time), self.value.get(), self.quantity.get())
        sqlhandler.add_entry(entry)
        sqlhandler.closeConnection()


root = Tk()
root.title("Spanding Maditation")
root.geometry("700x250+400+250")  # widthxheight+width+height
my_gui = GUI(root)
root.mainloop()

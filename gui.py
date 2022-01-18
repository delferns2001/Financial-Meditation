from tkinter import StringVar, Tk, Frame
from tkinter.ttk import Entry, Label, Button, Radiobutton

from matplotlib.pyplot import text
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
        # create a string var for the supermarket

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

        master.bind('<Return>', lambda event: self.onSubmit())
        # self.l_tesco = Label(self.form, text="Tesco", background="orange")
        # self.l_liddle = Label(self.form, text="Liddle", background="orange")
        # self.l_sainsburys = Label(
        #     self.form, text="Sainburys", background="orange")
        # self.l_aldi = Label(self.form, text="Aldi", background="orange")
        # self.l_other = Label(self.form, text="Other", background="orange")

        self.rb_tesco = Radiobutton(self.form, text="Tesco", value=1)
        self.rb_liddle = Radiobutton(self.form, text="Liddle", value=2)
        self.rb_sainsburys = Radiobutton(self.form, text="Sainsburys", value=3)
        self.rb_aldi = Radiobutton(self.form, text="Aldi", value=4)
        self.rb_other = Radiobutton(self.form, text="Other", value=5)

        self.l_name.grid(row=0, column=0, pady=10, padx=10)
        self.e_name.grid(row=0, column=1, pady=10, padx=5)
        self.l_value.grid(row=1, column=0, pady=10, padx=10)
        self.e_value.grid(row=1, column=1, pady=10, padx=5)
        self.l_quantity.grid(row=2, column=0, pady=10, padx=10)
        self.e_quantity.grid(row=2, column=1, pady=10, padx=5)

        # self.l_tesco.grid(row=0, column=2, pady=10, padx=10)
        self.rb_tesco.grid(row=1, column=2, pady=10, padx=10)
        # self.l_aldi.grid(row=0, column=3, pady=10, padx=10)
        self.rb_aldi.grid(row=1, column=3, pady=10, padx=10)
        # self.l_sainsburys.grid(row=0, column=4, pady=10, padx=10)
        self.rb_sainsburys.grid(row=1, column=4, pady=10, padx=10)
        # self.l_liddle.grid(row=0, column=5, pady=10, padx=10)
        self.rb_liddle.grid(row=1, column=5, pady=10, padx=10)
        # self.l_other.grid(row=0, column=6, pady=10, padx=10)
        self.rb_other.grid(row=1, column=6, pady=10, padx=10)

        self.b_submit.grid(row=2, column=4, pady=10)

        self.datetime = datetime.now()
        self.date = self.datetime.date()
        self.time = self.datetime.strftime("%H:%M:%S")

    def onSubmit(self):

        if len(self.name.get()) != 0 and len(self.value.get()) != 0 and len(self.quantity.get()) != 0:
            print("name: " + str(self.name.get()) + " value: " +
                  str(self.value.get()) + " quantity: " + str(self.quantity.get()))
            self.CreateShoppingBasketItem()
            self.saveEntry()
            self.resetValues()
        else:
            print("PLEASE ENTER VALUES")

    def resetValues(self):
        self.e_name.delete(0, "end")
        self.e_value.delete(0, "end")
        self.e_quantity.delete(0, "end")

    def CreateShoppingBasketItem(self):

        count = len(self.shoppingBusket.winfo_children()) + 1
        label = Label(
            self.shoppingBusket, text=f"{count}. Name: {self.name.get()}, Value: {self.value.get()}, Quantity: {self.quantity.get()}")
        label.pack()

    def saveEntry(self):
        sqlhandler = ConnectToSqlite()

        entry = ShoppingListEntry(
            self.name.get(), str(self.date), str(self.time), self.value.get(), self.quantity.get())
        sqlhandler.add_entry(entry)
        sqlhandler.closeConnection()


root = Tk()
root.title("Spanding Maditation")
root.geometry("800x600")
# root.geometry("700x250+400+250")  # widthxheight+width+height
my_gui = GUI(root)
root.mainloop()

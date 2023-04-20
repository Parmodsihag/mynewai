import tkinter as tk
from tkinter import ttk
from datetime import datetime

from mytheme import Colors

# import accounts
import inventory
import database
# from inventory import
# from sales import Sales

class AddItemsPage(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, **kwargs)

        APP_FONT = "Consolas 14"

        # Name Entry Box
        name_frame = tk.Frame(self, bg=Colors.ACTIVE_BACKGROUND)
        name_frame.pack(pady=10)
        name_label = tk.Label(name_frame, text="Item Name: ", font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        name_label.pack(side="left")
        self.name_entry = tk.Entry(name_frame, font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        self.name_entry.pack(side="left")

        # Other Details Entry Box
        details_frame = tk.Frame(self, bg=Colors.ACTIVE_BACKGROUND)
        details_frame.pack(pady=10)
        details_label = tk.Label(details_frame, text="Source: ", font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        details_label.pack(side="left")
        self.details_entry = tk.Entry(details_frame, font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        self.details_entry.pack(side="left")

        # Date Entry Box
        date_frame = tk.Frame(self, bg=Colors.ACTIVE_BACKGROUND)
        date_frame.pack(pady=10)
        date_label = tk.Label(date_frame, text="Date: ", font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        date_label.pack(side="left")
        self.date_entry = tk.Entry(date_frame, font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        self.date_entry.pack(side="left")
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        # Opening Balance Entry Box
        balance_frame = tk.Frame(self, bg=Colors.ACTIVE_BACKGROUND)
        balance_frame.pack(pady=10)
        balance_label = tk.Label(balance_frame, text="Opening Balance: ", font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        balance_label.pack(side="left")
        self.balance_entry = tk.Entry(balance_frame, font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        self.balance_entry.pack(side="left")
        
        # Status Entry Box
        # status_frame = tk.Frame(self, bg=Colors.ACTIVE_BACKGROUND)
        # status_frame.pack(pady=10)
        # status_label = tk.Label(status_frame, text="Status: ", font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        # status_label.pack(side="left")
        # self.status_entry = tk.Entry(status_frame, font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        # self.status_entry.insert(0, "New Account")
        # self.status_entry.pack(side="left")
        # self.pm_entry = tk.Entry(status_frame, font=APP_FONT, bg=Colors.ACTIVE_BACKGROUND)
        # self.pm_entry.insert(0, "p")
        # self.pm_entry.pack(side="left")

        # Add Account Button
        button_frame = tk.Frame(self, bg=Colors.ACTIVE_BACKGROUND)
        button_frame.pack(pady=20)
        self.add_button = tk.Button(button_frame, text="Add Account", font=APP_FONT, command=self.add_item, bg=Colors.ACTIVE_BACKGROUND)
        self.add_button.pack()


    def add_item(self):
        name = self.name_entry.get().upper()
        date = self.date_entry.get().upper()
        details = self.details_entry.get().upper()
        opening_balance = self.balance_entry.get()

        # verify entry
        if name and date and details:
            dailynote = f"02 = {name}, {date}, {details}, {opening_balance}"
            database.add_note_to_date(dailynote)

            item_id = inventory.add_new_item(name)
            inventory.add_item_transaction(item_id,date, opening_balance, 0, details)

            if __name__ != "__main__":
                self.master.master.set_status(f"Item added: {item_id}")

        else:
            if __name__ == "__main__":
                print("Some fields are empty")
            else:
                self.master.master.set_status("[-]|Some fields are empty|")

        # add account to database
        # (code for this would depend on how you implemented your accounts database)


if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    a = AddItemsPage(app)
    a.pack(expand=1, fill="both")
    app.mainloop()

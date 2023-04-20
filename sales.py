import tkinter as tk
import tkinter.ttk as ttk
from mytheme import Colors, DarkFuturisticTheme
from datetime import datetime

import accounts
import inventory
import database

class SalesPage(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, **kwargs)

        # Date Entry Box
        date_label = tk.Label(self, text="Date", font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        date_label.pack(pady=10)
        today_date = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
        self.date_entry = tk.Entry(self, textvariable=today_date, font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        self.date_entry.pack()

        # Item Dropdown Menu
        item_label = tk.Label(self, text="Item", font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        item_label.pack(pady=10)
        item_choices = self.get_items_from_inventory()
        self.item_dropdown = ttk.Combobox(self, values=item_choices, font="Consolas 14")
        self.item_dropdown.pack()
        self.item_dropdown.bind('<Enter>', lambda e: self.item_dropdown.config(values=self.get_items_from_inventory()))

        # Account Dropdown Menu
        account_label = tk.Label(self, text="Account", font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        account_label.pack(pady=10)
        account_choices = self.get_accounts()
        self.account_dropdown = ttk.Combobox(self, values=account_choices, font="Consolas 14")
        self.account_dropdown.pack()
        self.account_dropdown.bind('<Enter>', lambda e: self.account_dropdown.config(values=self.get_accounts()))

        # Quantity Entry Box
        quantity_label = tk.Label(self, text="Quantity", font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        quantity_label.pack(pady=10)
        self.quantity_entry = tk.Entry(self, font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        self.quantity_entry.pack()

        # Price Entry Box
        price_label = tk.Label(self, text="Price", font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        price_label.pack(pady=10)
        self.price_entry = tk.Entry(self, font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        self.price_entry.pack()

        # Save Button
        sale_button = tk.Button(self, text="Sale", font="Consolas 14", command=self.sale, bg=Colors.ACTIVE_BACKGROUND, fg=Colors.ACTIVE_FOREGROUND)
        sale_button.pack(pady=20)
        recieve_button = tk.Button(self, text="Recieve", font="Consolas 14", command=self.recieve, bg=Colors.ACTIVE_BACKGROUND, fg=Colors.ACTIVE_FOREGROUND)
        recieve_button.pack(pady=20)

    def get_items_from_inventory(self):
        item_list = inventory.get_all_items()
        # code to fetch items from inventory database
        # replace this with actual code to fetch items from your database
        return item_list

    def get_accounts(self):
        accoount_list = accounts.get_all_customers()
        # code to fetch accounts from accounts database
        # replace this with actual code to fetch accounts from your database
        return accoount_list

    def sale(self):
        # date item account quatity price
        date = self.date_entry.get()
        item_name = self.item_dropdown.get()
        account_name = self.account_dropdown.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        # print(date, item_id,account_id, quantity, price)
        if date and item_name and account_name and quantity and price:
            item_id = item_name.split()[0]
            account_id = account_name.split()[0]
            if "{" in account_name:
                aname = account_name.split("{")[1].split("}")[0]
            else:
                aname = account_name
            if "{" in item_name:    
                iname = item_name.split("{")[1].split("}")[0]
            else:
                iname = item_name

            # first daily note
            note = f"03 = {date}, {iname}, {aname}, {quantity}, {price}"
            database.add_note_to_date(note)
            
            # to account
            detail = f"{quantity} = {iname}"
            amount = int(price) * int(quantity)
            accounts.add_customer_transaction(account_id, date, detail, amount, "p" )
            
            # update inventory
            inventory.add_item_transaction(item_id, date, 0, int(quantity), aname)
        else:
            pass
    
    def recieve(self):
        # date item account quatity price
        date = self.date_entry.get()
        item_name = self.item_dropdown.get()
        account_name = self.account_dropdown.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        # print(date, item_id,account_id, quantity, price)
        if date and item_name and account_name and quantity and price:
            item_id = item_name.split()[0]
            account_id = account_name.split()[0]
            aname = account_name.split("{")[1].split("}")[0]
            iname = item_name.split("{")[1].split("}")[0]

            # first daily note
            note = f"04 = {date}, {iname}, {aname}, {quantity}, {price}"
            database.add_note_to_date(note)
            
            # to account
            detail = f"{quantity} = {iname}"
            amount = int(price) * int(quantity)
            accounts.add_customer_transaction(account_id, date, detail, amount, "m" )
            
            # update inventory
            inventory.add_item_transaction(item_id, date, int(quantity), 0, aname)
        else:
            pass
        


if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    h = SalesPage(app)
    h.pack(expand=1, fill="both")
    app.mainloop()

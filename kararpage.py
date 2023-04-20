import tkinter as tk
import sqlite3

import accounts
import krar

from tkinter import ttk
from mytheme import Colors
from datetime import datetime




class KararPage(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, **kwargs)

        # Date Entry Box
        date_label = tk.Label(self, text="Date", font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        date_label.pack(pady=10)
        today_date = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
        self.date_entry = tk.Entry(self, textvariable=today_date, font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        self.date_entry.pack()

        # Account Dropdown Menu
        account_label = tk.Label(self, text="Account", font="Consolas 14", bg=Colors.ACTIVE_BACKGROUND)
        account_label.pack(pady=10)
        account_choices = self.get_accounts()
        self.account_dropdown = ttk.Combobox(self, values=account_choices, font="Consolas 14")
        self.account_dropdown.pack()
        self.account_dropdown.bind('<Enter>', lambda e: self.account_dropdown.config(values=self.get_accounts()))

        sale_button = tk.Button(self, text="Add krar", font="Consolas 14", command=self.add_krar, bg=Colors.ACTIVE_BACKGROUND, fg=Colors.ACTIVE_FOREGROUND)
        sale_button.pack(pady=20)

    def get_accounts(self):
        accoount_list = accounts.get_all_customers()
        return accoount_list

    def add_krar(self):
        customer_name = self.account_dropdown.get()
        krar_date = self.date_entry.get()
        if customer_name and krar_date:
            krar_id = krar.create_krar(customer_name, krar_date)
            if __name__ != "__main__":
                self.master.master.set_status(f"Krar Id : {krar_id}")


if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    h = KararPage(app)
    h.pack(expand=1, fill="both")
    app.mainloop()

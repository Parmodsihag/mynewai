import tkinter as tk

from mytheme import Colors
from tkinter import ttk


import accounts
import inventory
import database
import krar





class HomePage(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, **kwargs)

        self.sales_data_frame = SalesData(self)
        self.sales_data_frame.place(relx=0, rely=0, relheight=0.5, relwidth=0.4)
        self.recieve_data_frame = RecieceData(self)
        self.recieve_data_frame.place(relx=0.4, rely=0, relheight=0.5, relwidth=0.4)
        self.account_data_frame = AccountsData(self)
        self.account_data_frame.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.4)
        self.items_data_frame = ItemsData(self)
        self.items_data_frame.place(relx=0.4, rely=0.5, relheight=0.5, relwidth=0.4)
        
        self.karar_data_frame = KrarData(self)
        self.karar_data_frame.place(relx=0.8, rely=0, relheight=1, relwidth=0.2)

        

    
        

class SalesData(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, highlightthickness=1, highlightbackground=Colors.ACTIVE_FOREGROUND, **kwargs)

        l = tk.Label(self, text="this is diffrent")
        # l.pack(expand=1, fill="both")
        
class RecieceData(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, highlightthickness=1, highlightbackground=Colors.ACTIVE_FOREGROUND, **kwargs)

class AccountsData(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, highlightthickness=1, highlightbackground=Colors.ACTIVE_FOREGROUND, **kwargs)

class ItemsData(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, highlightthickness=1, highlightbackground=Colors.ACTIVE_FOREGROUND, **kwargs)
        l = tk.Label(self, text="this is diffrent")
        # l.pack(expand=1, fill="both")

class KrarData(tk.Frame):
    def __init__(self, master, **kwargs):
        
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, highlightthickness=1, highlightbackground=Colors.ACTIVE_FOREGROUND, **kwargs)

        self.table_frame = tk.Frame(self, bg=Colors.ACTIVE_BACKGROUND)
        self.table_frame.pack(fill="both", expand=1)
        self.down_frame = tk.Frame(self, bg=Colors.ACTIVE_BACKGROUND)
        self.down_frame.pack(fill="both", expand=1)
        self.show_table()

        # down table
        self.table_list = []
        myset = set()
        all_krars = krar.get_all_due_krars()
        for krar1 in all_krars:
            myset.add(krar1[1])

        self.table_list = list(myset)

        # print(all_krars)
        self.table_dropdown = ttk.Combobox(self.down_frame, values= self.table_list, width=20)
        self.table_dropdown.pack(side="top", padx=5, pady=5, fill="x", expand=1)

        save_button = tk.Button(self, text="Set Done", font="Consolas 14", command=self.set_undue_krar, bg=Colors.ACTIVE_BACKGROUND, fg=Colors.ACTIVE_FOREGROUND)
        save_button.pack(pady=20, padx=20, fill="x", expand=1)
        

    def set_undue_krar(self):
        customer_name = self.table_dropdown.get()
        if customer_name:
            krar.update_krar_tag_by_name(customer_name, 0)

    def show_data(self):
        table_data = set()
        t = krar.get_krars_by_date()
        max_len = 0
        for i in t:
            # print(i)
            if len(i[1]) > max_len:
                max_len = len(i[1])
            krar_count = len(krar.get_due_krars_by_customer_name(i[1]))
            temp = [i[1], krar_count]#, i[2]
            table_data.add(tuple(temp))
            # print(krar_count)
            # table_data.append(temp)
            # table_data.append([])
        
        return table_data, max_len
        
    def show_table(self):
        table_data, max_len = self.show_data()
        column_name = ["Name", "Krar count"]
        
        if column_name and table_data:
            for widget in self.table_frame.winfo_children():
                widget.destroy()
                
            tree = ttk.Treeview(self.table_frame)
            tree['columns'] = column_name
            tree.column('#0', minwidth=5, anchor="w")

            for i in column_name:
                tree.column(i, minwidth=300,  anchor='w')
                tree.heading(i, text=i)
            
            c = 0
            for i in table_data:
                c += 1
                tg = 'odd'
                if c%2 == 0:
                    tg = "even"
                tree.insert('', c, text=c, values=i, tags = tg )

            tree.tag_configure('odd', background=Colors.ACTIVE_BACKGROUND)
            tree.tag_configure('even', background=Colors.ACTIVE_FOREGROUND)
            tree.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        else:
            print("Empty fields : Krar")



if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    h = HomePage(app)
    h.pack(expand=1, fill="both")
    app.mainloop()

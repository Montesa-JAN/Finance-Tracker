import customtkinter as ctk
from tkinter.ttk import Treeview


class TableView(ctk.CTkFrame):
    FONT = ("BEBAS", 20)
    PADDING = 20
    COLS = ("Accounts", "Income", "Savings", "Expenses")

    def __init__(self, master, title):
        super().__init__(master)

        self.title = title

        self.title_label = ctk.CTkLabel(self, text=self.title, font=self.FONT)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=self.PADDING, pady=self.PADDING, sticky="new")

        self.treeview = Treeview(self, show="headings", columns=self.COLS, height=30)
        self.treeview["columns"] = ("Accounts", "Income", "Savings", "Expenses")
        self.treeview.column('Accounts', width=100, anchor='w')
        self.treeview.column('Income', width=100, anchor='w')
        self.treeview.column('Savings', width=100, anchor='w')
        self.treeview.column('Expenses', width=100, anchor='w')

        self.treeview.heading('Accounts', text='Accounts')
        self.treeview.heading('Income', text='Income')
        self.treeview.heading('Savings', text='Savings')
        self.treeview.heading('Expenses', text='Expenses')
        self.treeview.grid(row=1, column=0, columnspan=2, padx=self.PADDING, pady=self.PADDING, sticky="news")


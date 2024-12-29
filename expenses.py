import customtkinter as ctk
from tkinter.ttk import Treeview
from workbookdata import WorkbookData
from add_tr_window import AddTransactionWindow

class Expenses(ctk.CTkFrame):
    FONT = ("BEBAS", 20)
    PADDING = 10
    COLS = ("Source", "Amount", "Tags", "Date")

    def __init__(self, master, title):
        super().__init__(master)
        self.workbook = WorkbookData()
        self.title = title

        self.title_label = ctk.CTkLabel(self, text=self.title, font=self.FONT)
        self.title_label.grid(row=0, column=0, columnspan=3, padx=self.PADDING, pady=self.PADDING, sticky="new")

        self.treeview = Treeview(self, show="headings", columns=self.COLS, height=30)
        self.treeview["columns"] = self.COLS
        self.treeview.column('Source', width=100, anchor='center')
        self.treeview.column('Amount', width=100, anchor='center')
        self.treeview.column('Tags', width=100, anchor='center')
        self.treeview.column('Date', width=100, anchor='center')

        self.treeview.heading('Source', text='Source')
        self.treeview.heading('Amount', text='Amount')
        self.treeview.heading('Tags', text='Tags')
        self.treeview.heading('Date', text='Date')
        self.treeview.grid(row=1, column=0, columnspan=3, padx=self.PADDING, pady=self.PADDING, sticky="news")

        self.addButton = ctk.CTkButton(self, text="Add", font=self.FONT, command=self.add_expense)
        self.addButton.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.deleteButton = ctk.CTkButton(self, text="Delete", font=self.FONT, command=self.delete_expense)
        self.deleteButton.grid(row=2, column=1, padx=5, pady=5)

        self.refreshButton = ctk.CTkButton(self, text="Refresh", font=self.FONT, command=self.refresh_data)
        self.refreshButton.grid(row=2, column=2, padx=5, pady=5)

        # Populate the treeview with existing data
        self.load_expense_data()

    def load_expense_data(self):
        """Load expense data from workbook into treeview"""
        try:
            # Clear existing items
            self.treeview.delete(*self.treeview.get_children())
            
            # Get data from workbook
            expense_data = self.workbook.get_sheet_data('Expense')
            
            # Insert data into treeview
            for row in expense_data:
                self.treeview.insert('', 'end', values=row)
                
        except Exception as e:
            print(f"Error loading expense data: {e}")

    def refresh_data(self):
        """Refresh the treeview data"""
        self.workbook = WorkbookData()  # Reload the workbook
        self.load_expense_data()

    def add_expense(self):
        self.add_transaction_window = AddTransactionWindow()
        self.add_transaction_window.focus()
        self.add_transaction_window.grab_set()
    
    def delete_expense(self):
        print("Delete expense")


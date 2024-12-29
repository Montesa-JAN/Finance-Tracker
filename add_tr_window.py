import customtkinter as ctk

class AddTransactionWindow(ctk.CTkToplevel):
    def __init__(self):
        FONT = ("BEBAS", 20)
        PADDING = 10
        super().__init__()
        self.title("Add Transaction")
        self.geometry("400x300")

        # Labels
        self.source_label = ctk.CTkLabel(self, text="Source", font=FONT)
        self.source_label.grid(row=0, column=0, padx=PADDING, pady=PADDING)

        self.amount_label = ctk.CTkLabel(self, text="Amount", font=FONT )
        self.amount_label.grid(row=1, column=0, padx=PADDING, pady=PADDING)

        self.tags_label = ctk.CTkLabel(self, text="Tags", font=FONT)
        self.tags_label.grid(row=2, column=0, padx=PADDING, pady=PADDING)

        self.date_label = ctk.CTkLabel(self, text="Date", font=FONT)
        self.date_label.grid(row=3, column=0, padx=PADDING, pady=PADDING)

        # Entries
        self.source_entry = ctk.CTkEntry(self)
        self.source_entry.grid(row=0, column=1, padx=PADDING, pady=PADDING)

        self.amount_entry = ctk.CTkEntry(self)
        self.amount_entry.grid(row=1, column=1, padx=PADDING, pady=PADDING)

        self.tags_entry = ctk.CTkEntry(self)
        self.tags_entry.grid(row=2, column=1, padx=PADDING, pady=PADDING)

        self.date_entry = ctk.CTkEntry(self)
        self.date_entry.grid(row=3, column=1, padx=PADDING, pady=PADDING)

        self.addButton = ctk.CTkButton(self, text="Add", font=FONT, command=self.add_transaction)
        self.addButton.grid(row=4, column=1, padx=PADDING, pady=PADDING)

    def add_transaction(self):
        print("Transaction added")
        self.close_window()  

    def close_window(self):
        self.destroy()

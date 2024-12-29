import customtkinter as ctk


class TotalSavings(ctk.CTkFrame):
    FONT = ("BEBAS", 20)
    PADDING = 5

    def __init__(self, master, title):
        super().__init__(master)

        self.title = title

        self.title_label = ctk.CTkLabel(self, text=self.title, font=self.FONT)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=self.PADDING, pady=self.PADDING, sticky="nw")

        self.month = ctk.CTkLabel(self, text='Month:', font=self.FONT)
        self.totalIncome = ctk.CTkLabel(self, text='Income:', font=self.FONT)
        self.totalExpense = ctk.CTkLabel(self, text='Expense:', font=self.FONT)
        self.net = ctk.CTkLabel(self, text='Net:', font=self.FONT)

        self.month.grid(row=1, column=0, padx=self.PADDING, pady=self.PADDING, sticky='w')
        self.totalIncome.grid(row=2, column=0, padx=self.PADDING, pady=self.PADDING, sticky='w')
        self.totalExpense.grid(row=3, column=0, padx=self.PADDING, pady=self.PADDING, sticky='w')
        self.net.grid(row=4, column=0, padx=self.PADDING, pady=self.PADDING, sticky='w')

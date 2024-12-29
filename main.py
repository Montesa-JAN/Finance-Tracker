import customtkinter as ctk
from income import Income
from expenses import Expenses
from totalsavings import TotalSavings

class MainApp(ctk.CTk):
    ctk.set_appearance_mode("dark")
    FONT = ("BEBAS", 20)
    PADDING = 10

    def __init__(self):
        super().__init__()
        # Window Config
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f'{width}x{height}')
        self.title("Finance Tracker")

        # Frames
        self.appFrame = ctk.CTkScrollableFrame(self, corner_radius=20)
        self.appFrame.pack(padx=self.PADDING, pady=self.PADDING, fill='both', expand=True)

        self.incomeFrame = Income(self.appFrame, title="Income")
        self.incomeFrame.grid(row=0, column=0, padx=self.PADDING, pady=self.PADDING, sticky="nw")

        self.expenseFrame = Expenses(self.appFrame, title="Expense")
        self.expenseFrame.grid(row=0, column=1, padx=self.PADDING, pady=self.PADDING, sticky="ne")

        self.savingsFrame = TotalSavings(self.appFrame, title="Total Savings")
        self.savingsFrame.grid(row=1, column=0, columnspan=2, padx=self.PADDING, pady=self.PADDING, sticky="sew")

    

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

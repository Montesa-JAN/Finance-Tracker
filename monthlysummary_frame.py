import customtkinter as ctk


class MonthlySummaryFrame(ctk.CTkFrame):
    FONT = ("BEBAS", 20)
    PADDING = 20

    def __init__(self, master):
        super().__init__(master)

        self.paycheck_Label = ctk.CTkLabel(self, text="Monthly Summary: ", font=self.FONT)
        self.paycheck_Label.grid(row=0, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")

        self.paycheck_Label = ctk.CTkLabel(self, text="Total Income: ", font=self.FONT)
        self.paycheck_Label.grid(row=1, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")

        self.paycheck_Label = ctk.CTkLabel(self, text="Total Savings: ", font=self.FONT)
        self.paycheck_Label.grid(row=2, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")

        self.paycheck_Label = ctk.CTkLabel(self, text="Total Expenses: ", font=self.FONT)
        self.paycheck_Label.grid(row=3, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")

        self.calc_Button = ctk.CTkButton(self, width=150, height=30, corner_radius=10, text="Generate Summary", font=self.FONT
                                         , command=self.gensummary)
        self.calc_Button.grid(row=4, column=0, padx=self.PADDING, pady=self.PADDING, sticky="sw")

    def gensummary(self):
        pass

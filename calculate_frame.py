import customtkinter as ctk


class CalculateFrame(ctk.CTkFrame):
    FONT = ("BEBAS", 20)
    PADDING = 20

    def __init__(self, master):
        super().__init__(master)

        self.paycheck_Label = ctk.CTkLabel(self, text="Paycheck: ", font=self.FONT)
        self.paycheck_Label.grid(row=0, column=0, padx=self.PADDING, pady=self.PADDING, sticky="new")

        self.paycheck_Entry = ctk.CTkEntry(self, width=250, height=30, corner_radius=10)
        self.paycheck_Entry.grid(row=0, column=1, padx=self.PADDING, pady=self.PADDING, sticky="e")

        self.calc_Button = ctk.CTkButton(self, width=150, height=30, corner_radius=10, text="Calculate", font=self.FONT
                                         , command=self.calculate)
        self.calc_Button.grid(row=1, column=0, padx=self.PADDING, pady=self.PADDING, sticky="sw")

    def calculate(self):
        pass

import customtkinter as ctk
from tableview_frame import TableView
from calculate_frame import CalculateFrame
from monthlysummary_frame import MonthlySummaryFrame


class MainApp(ctk.CTk):
    ctk.set_appearance_mode("dark")
    WIDTH = 1000
    HEIGHT = 900
    FONT = ("BEBAS", 20)
    PADDING = 20

    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)

        self.title("Finance Tracker")
        self.geometry(f"{MainApp.WIDTH}x{MainApp.HEIGHT}")

        # Frames
        self.tableFrame = TableView(self, title="Table View")
        self.tableFrame.grid(row=0, column=0, padx=self.PADDING, pady=self.PADDING, sticky="nw")

        self.calculateFrame = CalculateFrame(self)
        self.calculateFrame.grid(row=0, column=1, columnspan=2, padx=self.PADDING, pady=self.PADDING, sticky="ne")

        self.summaryFrame = MonthlySummaryFrame(self)
        self.summaryFrame.grid(row=0, column=1, columnspan=2, padx=self.PADDING, pady=self.PADDING, sticky="ew")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

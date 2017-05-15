import tkinter as tk
import datetime
import configparser


class Report(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.lblfrm_riepilogo = tk.LabelFrame(self, text='Data da elaborare')
        self.lbl_data = tk.Label(self, text='')

        self.lblfrm_riepilogo.grid()
        self.lbl_data.grid()
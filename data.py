import tkinter as tk
import tkinter.ttk as ttk
import datetime
import configparser


class Data(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.data = datetime.date.today()

        self.lblfrm_intervallo_date = tk.LabelFrame(self,
                                                    text='Data da elaborare',
                                                    labelanchor='n',
                                                    foreground='blue')
        self.lbl_data = tk.Label(self.lblfrm_intervallo_date, text=self.data.strftime('%d/%m/%Y'))

        self.lblfrm_intervallo_date.grid()
        self.lbl_data.grid()

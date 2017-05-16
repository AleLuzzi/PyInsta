import tkinter as tk
from tkinter import ttk
import datetime
import configparser


class Data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)
        self.controller = controller

        self.data = datetime.date.today()

        self.config = self.leggi_file_ini()

        self.lblfrm_intervallo_date = tk.LabelFrame(self,
                                                    text='Data da elaborare',
                                                    labelanchor='n',
                                                    font=(self.config['Font']['font'], 20),
                                                    foreground='blue')
        self.data_scelta = tk.StringVar()
        self.data_scelta.set(self.data)
        self.rdbtn1 = tk.Radiobutton(self.lblfrm_intervallo_date,
                                     text='Oggi   ' + self.data.strftime('%d/%m/%Y'),
                                     font=(self.config['Font']['font'], 15),
                                     variable=self.data_scelta,
                                     value=self.data)
        self.rdbtn2 = tk.Radiobutton(self.lblfrm_intervallo_date,
                                     text='Ieri    ' + (self.data - datetime.timedelta(days=1)).strftime('%d/%m/%Y'),
                                     font=(self.config['Font']['font'], 15),
                                     variable=self.data_scelta,
                                     value=(self.data - datetime.timedelta(days=1)))

        self.lblfrm_intervallo_date.grid()
        self.rdbtn1.grid(sticky='w')
        self.rdbtn2.grid(sticky='w')

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

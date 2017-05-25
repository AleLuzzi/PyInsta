import configparser
# from tkinter import ttk
import datetime
import tkinter as tk
# import os
from distutils.dir_util import copy_tree
# import win32print


class Data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)
        self.controller = controller

        self.data = datetime.date.today()

        self.config = self.leggi_file_ini()

        # STRINGVAR
        self.data_scelta = tk.StringVar()
        self.data_scelta.set(self.data)

        # LABELFRAME Date
        self.lblfrm_intervallo_date = tk.LabelFrame(self,
                                                    text='Data da elaborare',
                                                    labelanchor='n',
                                                    font=(self.config['Font']['font'], 20),
                                                    foreground='blue')

        # RADIOBUTTON scelta data
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

        # BUTTON controlla aggiornamenti
        self.btn_aggiorna = tk.Button(self,
                                      text='Aggiorna dati\ndelle vendite',
                                      command=self.aggiorna)

        # LAYOUT
        self.lblfrm_intervallo_date.grid()
        self.rdbtn1.grid(sticky='w')
        self.rdbtn2.grid(sticky='w')

        self.btn_aggiorna.grid()

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def aggiorna(self):
            copy_tree(self.config['Ugalaxy']['dir'], self.config['PyInsta']['dir'])

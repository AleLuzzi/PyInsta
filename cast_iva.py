import configparser
import tkinter as tk
from tkinter import ttk
import datetime as dt
from dbfread import DBF
from tkinter import messagebox
import os


class CastellettoIva(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self, controller)

        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))
        self.title('Castelletto Iva')

        self.config = self.leggi_file_ini()

        self.controller = controller

        self.data = self.controller.tab1.data_scelta.get()
        self.data_conv = 'I0' + self.data[-2:] + self.data[3:5] + self.data[:2] + '.sid'
        self.percorso = self.config['iShuttle']['dir'] + '\\log\\' + self.data_conv
        print(self.percorso)
        exists = os.path.isfile(self.percorso)
        if exists:
            print(exists)
        else:
            print('non esiste')

        # TREEVIEW per visualizzare dati
        self.tree = ttk.Treeview(self, height=10)
        self.tree['columns'] = ('data', 'cod_iva', 'imponibile', 'imposta')

        self.tree['show'] = 'headings'
        self.tree.heading('data', text="data")
        self.tree.heading('cod_iva', text="Cod IVA")
        self.tree.heading('imponibile', text='Imponibile')
        self.tree.heading('imposta', text='Imposta')

        self.tree.column("data", width=80)
        self.tree.column("cod_iva", width=80)
        self.tree.column("imponibile", width=80)
        self.tree.column("imposta", width=80)

        # BUTTON chiudi
        self.btn_chiudi = tk.Button(self, text='Chiudi',
                                    command=self.chiudi)

        # LAYOUT
        self.tree.grid()
        self.btn_chiudi.grid()

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def chiudi(self):
        self.destroy()

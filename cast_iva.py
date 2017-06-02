import configparser
import tkinter as tk
from tkinter import ttk
import datetime as dt
from dbfread import DBF


class Castelletto_iva(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self, controller)

        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))
        self.title('Castelletto Iva')

        self.config = self.leggi_file_ini()

        self.controller = controller

        self.data = self.controller.tab1.data_scelta.get()

        self.tabella = DBF(self.config['PyInsta']['dir'] + '\\castiva.dbf', load=True)

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

        try:
            self.data_conv = dt.datetime.strptime(self.data, "%Y-%m-%d").date()

            for record in self.tabella:
                if record['IMPONIBILE'] is not None and record['DATA_IVA'] == self.data_conv:
                    self.tree.insert('', 'end',
                                     values=(record['DATA_IVA'].strftime('%d-%m-%Y'),
                                             record['DES_IVA'],
                                             record['IMPONIBILE'] / 100,
                                             record['IMPOSTA'] / 100))

        except ValueError:
            self.data_conv = dt.datetime.strptime(self.data, "%Y-%m").date()

            for record in self.tabella:
                if record['IMPONIBILE'] is not None:
                    if record['DATA_IVA'].month == self.data_conv.month and \
                                    record['DATA_IVA'].year == self.data_conv.year:
                        self.tree.insert('', 'end',
                                         values=(record['DATA_IVA'].strftime('%d-%m-%Y'),
                                                 record['DES_IVA'],
                                                 record['IMPONIBILE'] / 100,
                                                 record['IMPOSTA'] / 100))

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def chiudi(self):
        self.destroy()

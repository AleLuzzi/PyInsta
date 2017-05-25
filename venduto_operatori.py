import configparser
import tkinter as tk
import datetime as dt
from dbfread import DBF


class Venduto_operatori(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self, controller)
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))

        self.title('Venduto Operatori')

        self.config = self.leggi_file_ini()

        self.controller = controller
        self.data = self.controller.tab1.data_scelta.get()
        self.data_conv = dt.datetime.strptime(self.data, "%Y-%m-%d").date()

        self.tabella = DBF(self.config['Ugalaxy']['dir']+'\\finstor.dbf')
        print(self.tabella.field_names)

        print('Inizio: {:%Y-%m-%d %H:%M:%S}'.format(dt.datetime.now()))

        for record in self.tabella:
            if record['DATA_VEND'] == self.data_conv:
                print(record)

        print('Fine: {:%Y-%b-%d %H:%M:%S}'.format(dt.datetime.now()))

        # BUTTON chiudi
        self.btn_chiudi = tk.Button(self, text='Chiudi',
                                    command=self.chiudi)

        # LAYOUT
        self.btn_chiudi.grid()

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def chiudi(self):
        self.destroy()

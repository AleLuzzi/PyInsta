import dbf
import configparser
import tkinter as tk


class Venduto_operatori(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title('Venduto Operatori')

        self.config = self.leggi_file_ini()
        self.tabella = dbf.Table(self.config['Ugalaxy']['dir']+'\\finstor.dbf')
        self.tabella.open()
        print(self.tabella.field_names)

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

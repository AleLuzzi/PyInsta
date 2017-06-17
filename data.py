import configparser
from tkinter import ttk
import datetime
import tkinter as tk
import os
from distutils.dir_util import copy_tree
from datepicker import Datepicker
# import win32print


class Data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)
        self.controller = controller

        self.data = datetime.date.today().strftime('%d-%m-%Y')

        self.config = self.leggi_file_ini()

        self.mesi_dict = {'Gennaio': 1, 'Febbraio': 2, 'Marzo': 3,
                          'Aprile': 4, 'Maggio': 5, 'Giugno': 6,
                          'Luglio': 7, 'Agosto': 8, 'Settembre': 9,
                          'Ottobre': 10, 'Novembre': 11, 'Dicembre': 12}

        # STRINGVAR
        self.data_scelta = tk.StringVar()
        self.data_scelta.set(self.data)

        self.ultimo_agg = tk.StringVar()
        self.ultimo_agg.set(datetime.datetime.fromtimestamp(os.path.getmtime(self.config['PyInsta']['dir'] + '\\finstor.dbf')).strftime('%d/%m/%Y %H:%M'))

        # LABELFRAME Date
        self.lblfrm_intervallo_date = tk.LabelFrame(self,
                                                    text='Data da elaborare',
                                                    labelanchor='n',
                                                    font=(self.config['Font']['font'], 20),
                                                    foreground='blue')

        # DATEPICKER
        self.picker = Datepicker(self.lblfrm_intervallo_date, dateformat='%d-%m-%Y', datevar=self.data_scelta)

        # COMBOBOX per selezione mese
        self.cmb_box_mese = ttk.Combobox(self.lblfrm_intervallo_date,
                                         state='readonly',
                                         values=list(self.mesi_dict.keys()))
        self.cmb_box_mese.current(0)
        self.cmb_box_mese.bind('<<ComboboxSelected>>', self.combo_selected)

        # BUTTON controlla aggiornamenti
        self.btn_aggiorna = tk.Button(self,
                                      text='Aggiorna dati\ndelle vendite',
                                      command=self.aggiorna)
        self.lbl_ultimo_agg = tk.Label(self,
                                       text='Ultimo aggiornamento\n' + self.ultimo_agg.get())

        # LAYOUT
        self.lblfrm_intervallo_date.grid()
        self.picker.grid()
        self.cmb_box_mese.grid()

        self.btn_aggiorna.grid()
        self.lbl_ultimo_agg.grid()

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def aggiorna(self):
            copy_tree(self.config['Ugalaxy']['dir'], self.config['PyInsta']['dir'])
            self.ultimo_agg.set(datetime.datetime.fromtimestamp(os.path.getmtime(self.config['PyInsta']['dir'] + '\\finstor.dbf')).strftime('%d/%m/%Y %H:%M'))

    def combo_selected(self, event):
        self.data_scelta.set('2017-' + '0' + str(self.mesi_dict[self.cmb_box_mese.get()]))

if __name__ == "__main__":
    root = tk.Tk()
    main = tk.Frame(root)
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("600x300+%d+%d" % (x, y))
    root.title('PyInsta')
    notebook = ttk.Notebook(main)
    tab1 = Data(notebook, main)
    notebook.add(tab1, text='Data', compound='left')
    main.grid()
    notebook.grid()
    root.mainloop()

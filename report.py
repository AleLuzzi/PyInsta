import tkinter as tk
import datetime
import configparser


class Report(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)

        self.controller = controller

        # print(self.controller.tab1.data_scelta.get())

        self.lblfrm_riepilogo = tk.LabelFrame(self, text='Data da elaborare')
        self.lbl_data = tk.Label(self, text='')
        self.btn_aggiorna = tk.Button(self, text='Aggiorna', command=self.aggiorna_dati)

        self.lblfrm_riepilogo.grid()
        self.lbl_data.grid()
        self.btn_aggiorna.grid()

    def aggiorna_dati(self):
        data = self.controller.tab1.data_scelta.get()
        self.lbl_data['text'] = data

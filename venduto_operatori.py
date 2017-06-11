import configparser
import tkinter as tk
import datetime as dt
# from tkinter import messagebox
from dbfread import DBF
import time, threading


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
        print(len(self.tabella.records))

        wind_mes = tk.Toplevel()

        x_wind = (wind_mes.winfo_screenwidth() - wind_mes.winfo_reqwidth()) / 2
        y_wind = (wind_mes.winfo_screenheight() - wind_mes.winfo_reqheight()) / 2
        wind_mes.geometry("+%d+%d" % (x_wind, y_wind))
        wind_mes.attributes('-topmost', True)

        label = tk.Label(wind_mes, text='Attendi... sto elaborando\n(len(self.tabella.records)\nrecord')
        label.grid()
        self.op1 = {'tot_vend': 0, 'r_cre': 0, 'usc': 0, 'prel': 0, 'incasso': 0, 'c_cre': 0}
        self.op2 = {'tot_vend': 0, 'r_cre': 0, 'usc': 0, 'prel': 0, 'incasso': 0, 'c_cre': 0}

        thread = threading.Thread(target=self.elabora)
        thread.start()
        while thread.is_alive():
            wind_mes.update()
            time.sleep(0.001)

        wind_mes.destroy()

        # LABELFRAME cassa 1
        self.lblfrm_cassa1 = tk.LabelFrame(self, text='CASSA 1')
        self.lbl_incasso_op1 = tk.Label(self.lblfrm_cassa1, text='Incasso ' + str(self.op1['incasso']/100))
        self.lbl_uscite_op1 = tk.Label(self.lblfrm_cassa1, text='Uscite' + str(self.op1['usc']/100))
        self.lbl_prelievi_op1 = tk.Label(self.lblfrm_cassa1, text='Prelievi' + str(self.op1['prel']/100))

        # LABELFRAME cassa 2
        self.lblfrm_cassa2 = tk.LabelFrame(self, text='CASSA 2')
        self.lbl_incasso_op2 = tk.Label(self.lblfrm_cassa2, text='Incasso ' + str(self.op2['incasso']/100))
        self.lbl_uscite_op2 = tk.Label(self.lblfrm_cassa2, text='Uscite' + str(self.op2['usc'] / 100))
        self.lbl_prelievi_op2 = tk.Label(self.lblfrm_cassa2, text='Prelievi' + str(self.op2['prel'] / 100))

        # BUTTON chiudi
        self.btn_chiudi = tk.Button(self, text='Chiudi',
                                    command=self.chiudi)

        # LAYOUT
        self.lblfrm_cassa1.grid()
        self.lbl_incasso_op1.grid()
        self.lbl_uscite_op1.grid()
        self.lbl_prelievi_op1.grid()

        self.lblfrm_cassa2.grid()
        self.lbl_incasso_op2.grid()
        self.lbl_uscite_op2.grid()
        self.lbl_prelievi_op2.grid()

        self.btn_chiudi.grid()

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def elabora(self):
        print('Inizio: {:%Y-%m-%d %H:%M:%S}'.format(dt.datetime.now()))
        i = 0

        self.data_conv = dt.datetime.strptime(self.data, "%Y-%m-%d").date()

        for record in self.tabella:

            if record['DATA_VEND'] == self.data_conv:
                i += 1
                print(record['LABEL'])
                if record['CODICE'] == '0001' and record['LABEL'] == 'TOT_VEND':
                    self.op1['tot_vend'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00R_CRE':
                    self.op1['r_cre'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00USC':
                    self.op1['usc'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00PREL':
                    self.op1['prel'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00':
                    self.op1['incasso'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG05':
                    self.op1['c_cre'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'TOT_VEND':
                    self.op2['tot_vend'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG00R_CRE':
                    self.op2['r_cre'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG00PREL':
                    self.op2['prel'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG00':
                    self.op2['incasso'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG05':
                    self.op2['c_cre'] = record['IMP']

        print('Fine: {:%Y-%b-%d %H:%M:%S}'.format(dt.datetime.now()))
        print(i)

    def chiudi(self):
        self.destroy()

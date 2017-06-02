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
        print(len(self.tabella.records))

        self.op1 = {'tot_vend': 0, 'r_cre': 0, 'usc': 0, 'prel': 0, 'incasso': 0, 'c_cre': 0}
        self.op2 = {'tot_vend': 0, 'r_cre': 0, 'usc': 0, 'prel': 0, 'incasso': 0, 'c_cre': 0}

        # BUTTON chiudi
        self.btn_chiudi = tk.Button(self, text='Chiudi',
                                    command=self.chiudi)

        # LAYOUT
        self.btn_chiudi.grid()

        print('Inizio: {:%Y-%m-%d %H:%M:%S}'.format(dt.datetime.now()))
        i = 0
        for record in self.tabella:

            if record['DATA_VEND'] == dt.datetime.strptime('20170510', "%Y%m%d").date():
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

        print(self.op1)
        print(self.op2)
        print(i)

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def chiudi(self):
        self.destroy()

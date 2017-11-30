import configparser
import datetime as dt
import threading
import time
import tkinter as tk
import tkinter.ttk as ttk
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
        self.data_conv = dt.datetime.strptime(self.data, "%d-%m-%Y").date()

        self.tabella = DBF(self.config['Ugalaxy']['dir'] + '\\finstor.dbf')

        wind_mes = tk.Toplevel()

        x_wind = (wind_mes.winfo_screenwidth() - wind_mes.winfo_reqwidth()) / 2
        y_wind = (wind_mes.winfo_screenheight() - wind_mes.winfo_reqheight()) / 2
        wind_mes.geometry("+%d+%d" % (x_wind, y_wind))
        wind_mes.attributes('-topmost', True)

        label = tk.Label(wind_mes, text='Attendi... sto elaborando\n' + str(len(self.tabella.records)) + '\nrecord')
        prog_bar = ttk.Progressbar(wind_mes, orient='horizontal', mode='determinate')
        label.grid()
        prog_bar.grid()

        self.op1 = {'tot_vend': 0, 'r_cre': 0, 'usc': 0, 'prel': 0, 'incasso': 0, 'c_cre': 0, 'f_cassa': 0}
        self.op2 = {'tot_vend': 0, 'r_cre': 0, 'usc': 0, 'prel': 0, 'incasso': 0, 'c_cre': 0, 'f_cassa': 0}
        self.op3 = {'tot_vend': 0, 'r_cre': 0, 'usc': 0, 'prel': 0, 'incasso': 0, 'c_cre': 0, 'f_cassa': 0}

        self.op1_sbilancio = 0
        self.op2_sbilancio = 0
        self.op3_sbilancio = 0

        thread = threading.Thread(target=self.elabora)
        thread.start()
        while thread.is_alive():
            wind_mes.update()
            time.sleep(0.001)
            prog_bar.start(500)

        wind_mes.destroy()

        # FONT Label
        self.f_label = ('Verdana', 10)

        # LABELFRAME cassa 1
        self.lblfrm_cassa1 = tk.LabelFrame(self, text='SIMONETTA',
                                           foreground='blue',
                                           font=('Verdana', 20),
                                           labelanchor='n')

        self.lbl_f_cassa_op1 = tk.Label(self.lblfrm_cassa1, text='Fondo Cassa', font=self.f_label)
        self.lbl_f_cassa_op1_imp = tk.Label(self.lblfrm_cassa1, text=str(self.op1['f_cassa'] / 100), bg='white')

        self.lbl_incasso_op1 = tk.Label(self.lblfrm_cassa1, text='Incasso ', font=self.f_label)
        self.lbl_incasso_op1_imp = tk.Label(self.lblfrm_cassa1, text=str(self.op1['incasso'] / 100), bg='white')

        self.lbl_uscite_op1 = tk.Label(self.lblfrm_cassa1, text='Uscite', font=self.f_label)
        self.lbl_uscite_op1_imp = tk.Label(self.lblfrm_cassa1, text=str(self.op1['usc'] / 100), bg='white')

        self.lbl_prelievi_op1 = tk.Label(self.lblfrm_cassa1, text='Prelievi', font=self.f_label)
        self.lbl_prelievi_op1_imp = tk.Label(self.lblfrm_cassa1, text=str(self.op1['prel'] / 100), bg='white')

        self.lbl_rec_cred_op1 = tk.Label(self.lblfrm_cassa1, text='Recupero Crediti', font=self.f_label)
        self.lbl_rec_cred_op1_imp = tk.Label(self.lblfrm_cassa1, text=str(self.op1['r_cre'] / 100), bg='white')

        self.lbl_sbilancio_op1 = tk.Label(self.lblfrm_cassa1, text='SBILANCIO', font=('Verdana', 15))
        self.lbl_sbilancio_op1_imp = tk.Label(self.lblfrm_cassa1, text=str(self.op1_sbilancio / 100))

        # LABELFRAME cassa 2
        self.lblfrm_cassa2 = tk.LabelFrame(self, text='MARGHERITA',
                                           foreground='blue',
                                           font=('Verdana', 20),
                                           labelanchor='n')

        self.lbl_f_cassa_op2 = tk.Label(self.lblfrm_cassa2, text='Fondo Cassa', font=self.f_label)
        self.lbl_f_cassa_op2_imp = tk.Label(self.lblfrm_cassa2, text=str(self.op2['f_cassa'] / 100), bg='white')

        self.lbl_incasso_op2 = tk.Label(self.lblfrm_cassa2, text='Incasso', font=self.f_label)
        self.lbl_incasso_op2_imp = tk.Label(self.lblfrm_cassa2, text=str(self.op2['incasso'] / 100), bg='white')

        self.lbl_uscite_op2 = tk.Label(self.lblfrm_cassa2, text='Uscite', font=self.f_label)
        self.lbl_uscite_op2_imp = tk.Label(self.lblfrm_cassa2, text=str(self.op2['usc'] / 100), bg='white')

        self.lbl_prelievi_op2 = tk.Label(self.lblfrm_cassa2, text='Prelievi', font=self.f_label)
        self.lbl_prelievi_op2_imp = tk.Label(self.lblfrm_cassa2, text=str(self.op2['prel'] / 100), bg='white')

        self.lbl_rec_cred_op2 = tk.Label(self.lblfrm_cassa2, text='Recupero Crediti', font=self.f_label)
        self.lbl_rec_cred_op2_imp = tk.Label(self.lblfrm_cassa2, text=str(self.op2['r_cre'] / 100), bg='white')

        self.lbl_sbilancio_op2 = tk.Label(self.lblfrm_cassa2, text='SBILANCIO', font=('Verdana', 15))
        self.lbl_sbilancio_op2_imp = tk.Label(self.lblfrm_cassa2, text=str(self.op2_sbilancio / 100))

        # LABELFRAME cassa 3
        self.lblfrm_cassa3 = tk.LabelFrame(self, text='LUCIANO',
                                           foreground='blue',
                                           font=('Verdana', 20),
                                           labelanchor='n')

        self.lbl_f_cassa_op3 = tk.Label(self.lblfrm_cassa3, text='Fondo Cassa', font=self.f_label)
        self.lbl_f_cassa_op3_imp = tk.Label(self.lblfrm_cassa3, text=str(self.op3['f_cassa'] / 100), bg='white')

        self.lbl_incasso_op3 = tk.Label(self.lblfrm_cassa3, text='Incasso', font=self.f_label)
        self.lbl_incasso_op3_imp = tk.Label(self.lblfrm_cassa3, text=str(self.op3['incasso'] / 100), bg='white')

        self.lbl_uscite_op3 = tk.Label(self.lblfrm_cassa3, text='Uscite', font=self.f_label)
        self.lbl_uscite_op3_imp = tk.Label(self.lblfrm_cassa3, text=str(self.op3['usc'] / 100), bg='white')

        self.lbl_prelievi_op3 = tk.Label(self.lblfrm_cassa3, text='Prelievi', font=self.f_label)
        self.lbl_prelievi_op3_imp = tk.Label(self.lblfrm_cassa3, text=str(self.op3['prel'] / 100), bg='white')

        self.lbl_rec_cred_op3 = tk.Label(self.lblfrm_cassa3, text='Recupero Crediti', font=self.f_label)
        self.lbl_rec_cred_op3_imp = tk.Label(self.lblfrm_cassa3, text=str(self.op3['r_cre'] / 100), bg='white')

        self.lbl_sbilancio_op3 = tk.Label(self.lblfrm_cassa3, text='SBILANCIO', font=('Verdana', 15))
        self.lbl_sbilancio_op3_imp = tk.Label(self.lblfrm_cassa3, text=str(self.op3_sbilancio / 100))

        # BUTTON chiudi
        self.btn_chiudi = tk.Button(self, text='Chiudi',
                                    command=self.chiudi)

        # LAYOUT
        self.lblfrm_cassa1.grid(row=0, column=0)

        self.lbl_f_cassa_op1.grid(row=0, column=0)
        self.lbl_f_cassa_op1_imp.grid(row=0, column=1, sticky='e')

        self.lbl_incasso_op1.grid(row=1, column=0)
        self.lbl_incasso_op1_imp.grid(row=1, column=1, sticky='e')

        self.lbl_uscite_op1.grid(row=2, column=0)
        self.lbl_uscite_op1_imp.grid(row=2, column=1, sticky='e')

        self.lbl_prelievi_op1.grid(row=3, column=0)
        self.lbl_prelievi_op1_imp.grid(row=3, column=1, sticky='e')

        self.lbl_rec_cred_op1.grid(row=4, column=0)
        self.lbl_rec_cred_op1_imp.grid(row=4, column=1, sticky='e')

        self.lbl_sbilancio_op1.grid(row=5, column=0)
        self.lbl_sbilancio_op1_imp.grid(row=5, column=1, sticky='e')

        self.lblfrm_cassa2.grid(row=0, column=1)

        self.lbl_f_cassa_op2.grid(row=0, column=0)
        self.lbl_f_cassa_op2_imp.grid(row=0, column=1, sticky='e')

        self.lbl_incasso_op2.grid(row=1, column=0)
        self.lbl_incasso_op2_imp.grid(row=1, column=1, sticky='e')

        self.lbl_uscite_op2.grid(row=2, column=0)
        self.lbl_uscite_op2_imp.grid(row=2, column=1, sticky='e')

        self.lbl_prelievi_op2.grid(row=3, column=0)
        self.lbl_prelievi_op2_imp.grid(row=3, column=1, sticky='e')

        self.lbl_rec_cred_op2.grid(row=4, column=0)
        self.lbl_rec_cred_op2_imp.grid(row=4, column=1, sticky='e')

        self.lbl_sbilancio_op2.grid(row=5, column=0)
        self.lbl_sbilancio_op2_imp.grid(row=5, column=1, sticky='e')

        self.lblfrm_cassa3.grid(row=0, column=2)

        self.lbl_f_cassa_op3.grid(row=0, column=0)
        self.lbl_f_cassa_op3_imp.grid(row=0, column=1, sticky='e')

        self.lbl_incasso_op3.grid(row=1, column=0)
        self.lbl_incasso_op3_imp.grid(row=1, column=1, sticky='e')

        self.lbl_uscite_op3.grid(row=2, column=0)
        self.lbl_uscite_op3_imp.grid(row=2, column=1, sticky='e')

        self.lbl_prelievi_op3.grid(row=3, column=0)
        self.lbl_prelievi_op3_imp.grid(row=3, column=1, sticky='e')

        self.lbl_rec_cred_op3.grid(row=4, column=0)
        self.lbl_rec_cred_op3_imp.grid(row=4, column=1, sticky='e')

        self.lbl_sbilancio_op3.grid(row=5, column=0)
        self.lbl_sbilancio_op3_imp.grid(row=5, column=1, sticky='e')

        self.btn_chiudi.grid()

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def elabora(self):
        for record in self.tabella:

            if record['DATA_VEND'] == self.data_conv:

                print(record['TIPO'], record['LABEL'], record['IMP'])
                if record['CODICE'] == '0001' and record['LABEL'] == 'TOT_VEND' and record['TIPO'] == 'O':
                    self.op1['tot_vend'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00R_CRE' and record['TIPO'] == 'O':
                    self.op1['r_cre'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00USC' and record['TIPO'] == 'O':
                    self.op1['usc'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00PREL' and record['TIPO'] == 'O':
                    self.op1['prel'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00' and record['TIPO'] == 'O':
                    self.op1['incasso'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG05' and record['TIPO'] == 'O':
                    self.op1['c_cre'] = record['IMP']

                if record['CODICE'] == '0001' and record['LABEL'] == 'PAG00F_C' and record['TIPO'] == 'O':
                    self.op1['f_cassa'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'TOT_VEND' and record['TIPO'] == 'O':
                    self.op2['tot_vend'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG00R_CRE' and record['TIPO'] == 'O':
                    self.op2['r_cre'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG00USC' and record['TIPO'] == 'O':
                    self.op2['usc'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG00PREL' and record['TIPO'] == 'O':
                    self.op2['prel'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG00' and record['TIPO'] == 'O':
                    self.op2['incasso'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG05' and record['TIPO'] == 'O':
                    self.op2['c_cre'] = record['IMP']

                if record['CODICE'] == '0002' and record['LABEL'] == 'PAG00F_C' and record['TIPO'] == 'O':
                    self.op2['f_cassa'] = record['IMP']

                if record['CODICE'] == '0003' and record['LABEL'] == 'TOT_VEND' and record['TIPO'] == 'O':
                    self.op3['tot_vend'] = record['IMP']

                if record['CODICE'] == '0003' and record['LABEL'] == 'PAG00R_CRE' and record['TIPO'] == 'O':
                    self.op3['r_cre'] = record['IMP']

                if record['CODICE'] == '0003' and record['LABEL'] == 'PAG00USC' and record['TIPO'] == 'O':
                    self.op3['usc'] = record['IMP']

                if record['CODICE'] == '0003' and record['LABEL'] == 'PAG00PREL' and record['TIPO'] == 'O':
                    self.op3['prel'] = record['IMP']

                if record['CODICE'] == '0003' and record['LABEL'] == 'PAG00' and record['TIPO'] == 'O':
                    self.op3['incasso'] = record['IMP']

                if record['CODICE'] == '0003' and record['LABEL'] == 'PAG05' and record['TIPO'] == 'O':
                    self.op3['c_cre'] = record['IMP']

                if record['CODICE'] == '0003' and record['LABEL'] == 'PAG00F_C' and record['TIPO'] == 'O':
                    self.op3['f_cassa'] = record['IMP']

            self.op1_sbilancio = self.op1['f_cassa'] + self.op1['incasso'] \
                                 - self.op1['prel'] - self.op1['usc'] + self.op1['r_cre']
            self.op2_sbilancio = self.op2['f_cassa'] + self.op2['incasso'] \
                                 - self.op2['prel'] - self.op2['usc'] + self.op2['r_cre']
            self.op3_sbilancio = self.op3['f_cassa'] + self.op3['incasso'] \
                                 - self.op3['prel'] - self.op3['usc'] + self.op3['r_cre']

    def chiudi(self):
        self.destroy()

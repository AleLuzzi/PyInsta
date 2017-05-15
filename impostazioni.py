import tkinter as tk
import configparser


class Impostazioni(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.config = self.leggi_file_ini()

        # STRINGVAR
        self.winswgx_dir = tk.StringVar()
        self.winswgx_dir.set(self.config['Winswgx']['dir'])

        # LABELFRAME UGALAXY
        self.lblfrm_ugalaxy = tk.LabelFrame(self, text='Ugalaxy', foreground='blue')

        # LABEL Ugalaxy
        self.lbl_ugalaxy = tk.Label(self.lblfrm_ugalaxy, text='Ugalaxy Folder')

        # LABELFRAME winswgx
        self.lblfrm_winswgx = tk.LabelFrame(self, text='Winswgx-net', foreground='blue')

        # LABEL Winswgx-net
        self.lbl_dir_name = tk.Button(self.lblfrm_winswgx,
                                      text='Winswgx-Net Folder')

        self.lbl_win_loc = tk.Label(self.lblfrm_winswgx,
                                    text=self.winswgx_dir.get(),
                                    relief='sunken')

        # LAYOUT
        self.lblfrm_ugalaxy.grid(row=1, column=0)
        self.lblfrm_winswgx.grid(row=2, column=0)

        self.lbl_ugalaxy.grid()

        self.lbl_dir_name.grid(row=1, column=0)
        self.lbl_win_loc.grid(row=1, column=1)

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

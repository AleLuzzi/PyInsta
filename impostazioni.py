import tkinter as tk
from tkinter import filedialog
import configparser


class Impostazioni(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)

        self.config = self.leggi_file_ini()

        # STRINGVAR
        self.winswgx_dir = tk.StringVar()
        self.winswgx_dir.set(self.config['Winswgx']['dir'])

        self.lbl_ugalaxy_value = tk.StringVar()
        self.lbl_ugalaxy_value.set(self.config['Ugalaxy']['dir'])

        self.lbl_pyinsta_value = tk.StringVar()
        self.lbl_pyinsta_value.set(self.config['PyInsta']['dir'])

        # LABELFRAME UGALAXY
        self.lblfrm_ugalaxy = tk.LabelFrame(self, text='Ugalaxy', foreground='blue')

        # LABEL Ugalaxy
        self.btn_ugalaxy = tk.Button(self.lblfrm_ugalaxy,
                                     text='Ugalaxy Folder',
                                     command=self.ugalaxy_open_dir)

        self.lbl_ugalaxy = tk.Label(self.lblfrm_ugalaxy,
                                    textvariable=self.lbl_ugalaxy_value,
                                    relief='sunken')

        # LABELFRAME PyInsta
        self.lblfrm_pyinsta = tk.LabelFrame(self, text='PyInsta Folder', foreground='blue')

        # LABEL PyInsta
        self.btn_pyinsta = tk.Button(self.lblfrm_pyinsta,
                                     text='PyInsta Folder',
                                     command=self.pyinsta_open_dir)

        self.lbl_pyinsta = tk.Label(self.lblfrm_pyinsta,
                                    textvariable=self.lbl_pyinsta_value,
                                    relief='sunken')

        # LABELFRAME winswgx
        self.lblfrm_winswgx = tk.LabelFrame(self, text='Winswgx-net', foreground='blue')

        # LABEL Winswgx-net
        self.btn_dir_name = tk.Button(self.lblfrm_winswgx,
                                      text='Winswgx-Net Folder',
                                      command=self.winswgx_open_dir)

        self.lbl_win_loc = tk.Label(self.lblfrm_winswgx,
                                    textvariable=self.winswgx_dir,
                                    relief='sunken')

        # LAYOUT
        self.lblfrm_ugalaxy.grid(row=1, column=0)
        self.lblfrm_pyinsta.grid(row=2, column=0)
        self.lblfrm_winswgx.grid(row=3, column=0)

        self.btn_ugalaxy.grid()
        self.lbl_ugalaxy.grid()

        self.btn_pyinsta.grid()
        self.lbl_pyinsta.grid()

        self.btn_dir_name.grid()
        self.lbl_win_loc.grid()

    @staticmethod
    def leggi_file_ini():
        ini = configparser.ConfigParser()
        ini.read('config.ini')
        return ini

    def winswgx_open_dir(self):
        new_dirname = filedialog.askdirectory(parent=self, initialdir='c:\\')
        cfg_file = open('config.ini', 'w')
        self.config.set('Winswgx', 'dir', new_dirname)
        self.config.write(cfg_file)
        self.winswgx_dir.set(new_dirname)

    def ugalaxy_open_dir(self):
        new_dirname = filedialog.askdirectory(parent=self, initialdir='c:\\')
        cfg_file = open('config.ini', 'w')
        self.config.set('Ugalaxy', 'dir', new_dirname)
        self.config.write(cfg_file)
        self.lbl_ugalaxy_value.set(new_dirname)

    def pyinsta_open_dir(self):
        new_dirname = filedialog.askdirectory(parent=self, initialdir='c:\\')
        cfg_file = open('config.ini', 'w')
        self.config.set('PyInsta', 'dir', new_dirname)
        self.config.write(cfg_file)
        self.lbl_pyinsta_value.set(new_dirname)

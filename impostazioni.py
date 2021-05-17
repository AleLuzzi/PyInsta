import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import configparser


class Impostazioni(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)

        self.config = self.leggi_file_ini()

        # STRINGVAR
        self.winswgx_dir = tk.StringVar()
        self.winswgx_dir.set(self.config['Winswgx']['dir'])

        self.lbl_ishuttle_value = tk.StringVar()
        self.lbl_ishuttle_value.set(self.config['iShuttle']['dir'])

        self.lbl_pyinsta_value = tk.StringVar()
        self.lbl_pyinsta_value.set(self.config['PyInsta']['dir'])

        # LABELFRAME iShuttle
        self.lblfrm_ishuttle = tk.LabelFrame(self, text='iShuttle', foreground='blue')

        # LABEL iShuttle
        self.btn_ishuttle = tk.Button(self.lblfrm_ishuttle,
                                      text='iShuttle Folder',
                                      command=self.ishuttle_open_dir)

        self.lbl_ishuttle = tk.Label(self.lblfrm_ishuttle,
                                     textvariable=self.lbl_ishuttle_value,
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
        self.lblfrm_ishuttle.grid(row=1, column=0)
        self.lblfrm_pyinsta.grid(row=2, column=0, sticky='we')
        self.lblfrm_winswgx.grid(row=3, column=0, sticky='we')

        self.btn_ishuttle.grid()
        self.lbl_ishuttle.grid()

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

    def ishuttle_open_dir(self):
        new_dirname = filedialog.askdirectory(parent=self, initialdir='c:\\')
        cfg_file = open('config.ini', 'w')
        self.config.set('Ugalaxy', 'dir', new_dirname)
        self.config.write(cfg_file)
        self.lbl_ishuttle_value.set(new_dirname)

    def pyinsta_open_dir(self):
        new_dirname = filedialog.askdirectory(parent=self, initialdir='c:\\')
        cfg_file = open('config.ini', 'w')
        self.config.set('PyInsta', 'dir', new_dirname)
        self.config.write(cfg_file)
        self.lbl_pyinsta_value.set(new_dirname)


if __name__ == "__main__":
    root = tk.Tk()
    main = tk.Frame(root)
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("600x300+%d+%d" % (x, y))
    root.title('PyInsta')
    notebook = ttk.Notebook(main)
    tab1 = Impostazioni(notebook, main)
    notebook.add(tab1, text='Impostazioni', compound='left')
    main.grid()
    notebook.grid()
    root.mainloop()

import tkinter as tk
import tkinter.ttk as ttk
import datetime
import configparser


class Main(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0)

        self.tab1 = self.Data()
        self.notebook.add(self.tab1, text='Data', compound='left')

        self.tab2 = self.Impostazioni()
        self.notebook.add(self.tab2, text='Impostazioni', compound='left')

        self.tab3 = self.Report()
        self.notebook.add(self.tab3, text='Report', compound='left')

    class Data(tk.Frame):
        data = datetime.date.today()

        def __init__(self):
            tk.Frame.__init__(self)

            self.data = datetime.date.today()

            self.lbl_data = tk.Label(self, text=Main.Data.data.strftime('%d/%m/%Y'))
            self.lbl_data.grid()

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

    class Report(tk.Frame):
        def __init__(self):
            tk.Frame.__init__(self)

            self.lblfrm_riepilogo = tk.LabelFrame(self, text='Data da elaborare')
            self.lbl_data = tk.Label(self, text=Main.Data.data.strftime('%d/%m/%Y'))

            self.lblfrm_riepilogo.grid()
            self.lbl_data.grid()


if __name__ == "__main__":
    root = tk.Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))
    root.title('PyInsta')
    Main(root).grid()
    root.mainloop()

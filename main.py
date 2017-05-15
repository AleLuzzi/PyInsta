from data import *
from impostazioni import *
from report import *
import tkinter as tk
import tkinter.ttk as ttk


class Main(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0)

        self.tab1 = Data()
        self.notebook.add(self.tab1, text='Data', compound='left')

        self.tab2 = Impostazioni()
        self.notebook.add(self.tab2, text='Impostazioni', compound='left')

        self.tab3 = Report()
        self.notebook.add(self.tab3, text='Report', compound='left')


if __name__ == "__main__":
    root = tk.Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))
    root.title('PyInsta')
    Main(root).grid()
    root.mainloop()

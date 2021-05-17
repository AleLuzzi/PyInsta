from data import *
from impostazioni import *
from report import *
from venduto_operatori import *
from cast_iva import *
import tkinter as tk
import tkinter.ttk as ttk
import os


class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # FRAME
        self.frame_sx = tk.Frame(self, height=300, width=300, bd=1, relief="raised", bg="white")
        self.frame_sx.grid_propagate(False)
        self.frame_sx.grid_rowconfigure(0, weight=1)
        self.frame_sx.grid_columnconfigure(0, weight=1)

        self.frame_dx = tk.Frame(self, height=300, width=300, bg="white")
        self.frame_dx.grid_propagate(False)
        self.frame_dx.grid_rowconfigure(0, weight=2)
        self.frame_dx.grid_columnconfigure(0, weight=2)

        # NOTEBOOK
        self.notebook = ttk.Notebook(self.frame_dx)

        # TAB Data
        self.tab1 = Data(self.notebook, self)
        self.notebook.add(self.tab1, text='Data', compound='left')

        # TAB Impostazioni
        self.tab2 = Impostazioni(self.notebook, self)
        self.notebook.add(self.tab2, text='Impostazioni', compound='left')

        # TAB Report nascosto
        self.tab3 = Report(self.notebook, self)
        self.notebook.add(self.tab3, text='Report', compound='left')

        self.notebook.hide(2)

        # IMMAGINI
        self.img_btn1 = tk.PhotoImage(file=os.path.join('immagini', 'logo.gif'))

        # LABEL logo
        self.lbl_logo = tk.Label(self.frame_sx, image=self.img_btn1)

        # BUTTON operazioni
        self.btn_operatori = tk.Button(self.frame_sx,
                                       text='Venduto\nOperatori',
                                       command=self.venduto_operatori)
        self.btn_cast_iva = tk.Button(self.frame_sx,
                                      text='Castelletto Iva',
                                      command=self.castelletto_iva)

        self.btn_chiudi = tk.Button(self.frame_sx, text='Chiudi', command=self.chiudi)

        # LAYOUT
        self.frame_sx.grid(row=1, column=0, sticky='ns')
        self.frame_dx.grid(row=1, column=1)

        self.lbl_logo.grid()

        self.btn_operatori.grid(sticky='we')
        self.btn_cast_iva.grid(sticky='we')
        self.btn_chiudi.grid(sticky='we')

        self.notebook.grid(sticky='we')

    def chiudi(self):
        self.quit()

    def venduto_operatori(self):
        Venduto_operatori(self)

    def castelletto_iva(self):
        CastellettoIva(self)


if __name__ == "__main__":
    root = tk.Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("600x300+%d+%d" % (x, y))
    root.title('PyInsta')
    Main(root).grid()
    root.mainloop()

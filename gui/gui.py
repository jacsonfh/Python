#pip install tk
#sudo dnf install python3-tkinter

import tkinter
from tkinter import *


def mostraDiscos(recebe1):
    print("O Texto da txtMenu é: " + recebe1)

frmPrincipal = tkinter.Tk()
frmPrincipal.title("Allpy")
frmPrincipal.minsize("800","600")

lblMenu = Label(frmPrincipal, text="Menu")
lblMenu.pack(side=LEFT)

txtMenu = StringVar()
txtMenu = Entry(frmPrincipal,textvariable=txtMenu)
txtMenu.pack(side=LEFT)

cmdOk = Button(frmPrincipal, text="Pesquisar", command=lambda: mostraDiscos(txtMenu.get()))
cmdOk.pack(side=LEFT)

frmPrincipal.mainloop()

#pip install tk
#sudo dnf install python3-tkinter

import tkinter
from tkinter import *


def mostraDiscos(recebe1):
    print("O Texto da txtMenu é: " + recebe1)

frmPrincipal = tkinter.Tk()
frmPrincipal.title("Allpy")
frmPrincipal.minsize("400","300")

def fnArquivo:
    print(" ")

def fnEditar:
    print("1")


var1 = ['a','b','c']
mapa = {"arquivo":fnUsuario,"Editar":fnEditar}
for i in mapa:
    lblMenu = Label(frmPrincipal, text = i['Arquivo'])
    lblMenu.grid(row=indice+1, column=indice+1)
    indice = indice + 1




indice = 1
for j in var1:
    lblMenu = Label(frmPrincipal, text = j)
    lblMenu.grid(row=indice+1, column=indice+1)
    indice = indice + 1

#lblMenu = Label(frmPrincipal, text="Menu")
#lblMenu.grid(row=1, column=1)
#lblMenu.pack(side=LEFT)

txtMenu = StringVar()
txtMenu = Entry(frmPrincipal,textvariable=txtMenu)
txtMenu.grid(row=2, column=1)
#txtMenu.pack(side=LEFT)

cmdOk = Button(frmPrincipal, text="Pesquisar", command=lambda: mostraDiscos(txtMenu.get()))
cmdOk.grid(row=3, column=1)
#cmdOk.pack(side=LEFT)

frmPrincipal.mainloop()

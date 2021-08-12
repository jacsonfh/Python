#
"""
Caso ocorra problema no tkinter.
brew install python3 --with-tcl-tk
brew install tcl-tk
"""

try:
   from tkinter import *
except:
   from Tkinter import *
   
window=Tk()


def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)


caminho = "/Users/jacsonheiderscheidt/Google Drive/1_PESSOAL/NET_SEC/GitHub/Python/modelos/" #apagar essa linha de m"
imgnewfile = PhotoImage(file="./img/newfile.png")

filemenu.add_command(label=" Novo", image=imgnewfile, compound="left", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

#menu.add_command(label=txt, image=self._img4, compound='left', command=cmd)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

window.title('ap')
window.geometry("900x700+500+150")
window.mainloop()



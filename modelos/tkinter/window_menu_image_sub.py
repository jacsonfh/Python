from tkinter import *
root = Tk()
root.geometry("500x500-500+50")



imgvar1 = PhotoImage(file='airplane1.png')

mainmenu1 = Menubutton(root, image=imgvar1)
mainmenu1.grid(row=0, column=0)

submenu1 = Menu(mainmenu1)
mainmenu1.config(menu=submenu1)

submenu1.add_command(label="Option 1.1")
submenu1.add_command(label="Option 1.2")


imgvar2 = PhotoImage(file='automobile1.png')

mainmenu2 = Menubutton(root, image=imgvar2)
mainmenu2.grid(row=0, column=1)

submenu2 = Menu(mainmenu2)
mainmenu2.config(menu=submenu2)

submenu2.add_command(label="Option 2.1")
submenu2.add_command(label="Option 2.2")



imgvar = PhotoImage(file='eye.gif')
button = Button(root, image=imgvar)
button.grid(row=0, column=2)


"""
import tkinter as tk

from tkinter import *


your_app_name = Tk()
menubar = Menu(your_app_name)

file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Command", menu=file_menu)
icon = PhotoImage(file='your_file.png') # or: (file='./your_file.png')
file_menu.add_command(label='New', image=icon, compound='left', command=some_function)

your_app_name.config(menu=menubar)
your_app_name.mainloop()

"""

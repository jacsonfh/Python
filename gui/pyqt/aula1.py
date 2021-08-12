from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window();
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300,150, 800, 400) #xpos, ypos, width, height.
    win.setWindowTitle("Teste de Titulo")


    win.show()
    sys.exit(app.exec_())

    

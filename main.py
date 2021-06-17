# # Starting with creating a simple window

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget

# app = QApplication(sys.argv)

# window = QWidget()
# # window.setGeometry(0, 0, 1000, 600)
# window.setWindowTitle("Python-Penny-Pal")

# window.show()

# app.exec()

# ==============================================================================================================
# Still learning how to use PyQt5
# https://pythonspot.com/pyqt5-textbox-example/

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import numpy as np

from doMath import doMath

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Python-Penny-Pal'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 700
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(200, 200)
        self.textbox.resize(600,100)
        
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(200,300)
        self.button.resize(600,100)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Python-Penny-Pal', "Sqrt of " + textboxValue +": " + doMath(textboxValue), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
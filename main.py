# making my own basic window

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit
from doMath import domath, calc

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Python-Penny-Pal")
        self.setMinimumSize(1000, 800)

        layout = QGridLayout()

        self.button = QPushButton("Enter")
        fontb =  self.button.font()
        fontb.setPointSize(16)
        self.button.setFont(fontb)

        self.clear = QPushButton('Clear')
        fontClear = self.clear.font()
        fontClear.setPointSize(16)
        self.clear.setFont(fontClear)

        self.line = QLineEdit()
        self.line.setMaxLength(21)
        #self.line.setFixedHeight(100)
        fontLine =  self.line.font()
        fontLine.setPointSize(16)
        self.line.setFont(fontLine)
        self.line.setPlaceholderText("Enter a number, I'll sqrt it!")

        self.label = QLabel("Hello")
        font =  self.label.font()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        layout.addWidget(self.line, 0, 0)
        layout.addWidget(self.button, 1, 0)
        layout.addWidget(self.clear, 2, 0)
        layout.addWidget(self.label, 3, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button.clicked.connect(self.onClick)
        self.clear.clicked.connect(self.onClear)

    def onClick(self):
        print(calc(self.line.text()))
        self.label.setText(calc(self.line.text()))
        
    def onClear(self):
        self.line.setText('')
        self.label.setText('Cleared')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
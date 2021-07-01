# making my own basic window

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit
from doMath import doMath

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Python-Penny-Pal")
        self.setMinimumSize(1000, 800)

        layout = QGridLayout()

        self.button = QPushButton("Enter")

        self.line = QLineEdit()
        self.line.setMaxLength(21)
        self.line.setPlaceholderText("Enter a number, I'll sqrt it!")

        self.label = QLabel("Hello")
        font =  self.label.font()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        layout.addWidget(self.line, 0, 0)
        layout.addWidget(self.button, 1, 0)
        layout.addWidget(self.label, 2, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button.clicked.connect(self.onClick)

    def onClick(self):
        print(doMath(self.line.text()))
        self.label.setText(doMath(self.line.text()))
        
        #print(self.button_is_checked)
        






        #button.clicked.connect(label.setText(doMath(line.text())))

    #    button.clicked.connect(self.squares(line))

    #def squares(self, line):
    #    return domath(line.text())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
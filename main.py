# Starting with creating a simple window

import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
# window.setGeometry(0, 0, 1000, 600)
window.setWindowTitle("Python-Penny-Pal")

window.show()

app.exec()
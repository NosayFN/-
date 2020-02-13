import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MapWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainMap.ui', self)


app = QApplication(sys.argv)
ex = MapWidget()
ex.show()
sys.exit(app.exec_())
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MapWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainMap.ui', self)
        self.DrawMapBut.clicked.connect(self.draw_map)

    def draw_map(self):
        xcoord = float(self.XInput.text())
        ycoord = float(self.YInput.text())
        size = int(self.SizeInput.text())
        self.XNowLabel.setText("{}".format(xcoord))
        self.YNowLabel.setText("{}".format(ycoord))
        self.SizeNowLabel.setText("{}".format(size))


app = QApplication(sys.argv)
ex = MapWidget()
ex.show()
sys.exit(app.exec_())
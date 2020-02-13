import requests
import sys
import os

import requests
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel

SCREEN_SIZE = [600, 450]
error = 'error, try again'


class MapWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainMap.ui', self)
        self.SizeNowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DrawMapBut.clicked.connect(self.draw_map)
        self.counter = 0

    def draw_map(self):
        xcoord = float(self.XInput.text())
        ycoord = float(self.YInput.text())
        self.size = int(self.SizeInput.text())
        self.size += self.counter
        self.XNowLabel.setText("{}".format(xcoord))
        self.YNowLabel.setText("{}".format(ycoord))
        self.SizeNowLabel.setText("{}".format(self.size))

        map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&l=map&z={}".\
            format(xcoord, ycoord, self.size)
        response = requests.get(map_request)

        if not response:
            self.XNowLabel.setText("{}".format(error))
            self.YNowLabel.setText("{}".format(error))
            self.SizeNowLabel.setText("{}".format(error))
        else:
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)

            pixmap = QPixmap(map_file)
            self.MapLabel.setPixmap(pixmap)
            os.remove(map_file)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_PageUp:
            if self.size < 17:
                self.counter += 1
        if event.key() == QtCore.Qt.Key_PageDown:
            if self.size > 0:
                self.counter -= 1
        event.accept()


app = QApplication(sys.argv)
ex = MapWidget()
ex.show()
sys.exit(app.exec_())
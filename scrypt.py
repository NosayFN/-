import sys
import os

import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

SCREEN_SIZE = [600, 450]
error = 'error, try again'

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

        map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&l=map&z={}".\
            format(xcoord, ycoord, size)
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


app = QApplication(sys.argv)
ex = MapWidget()
ex.show()
sys.exit(app.exec_())
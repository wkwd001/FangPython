import requests
import sys

from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap


class LoadPicThread(QThread):
    signal_load_pic = QtCore.pyqtSignal(int,QPixmap)  # 信号

    def __init__(self, parent=None):
        super(LoadPicThread, self).__init__(parent)

    def start_thread(self,list):
        self.list = list
        self.start()

    def run(self):
        try:
            for index,listItem in enumerate(self.list):
                pixmap = QPixmap()
                pic = requests.get(listItem[0]).content
                pixmap.loadFromData(pic)
                self.signal_load_pic.emit(index,pixmap)
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])

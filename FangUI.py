import requests
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QMessageBox

from FangData import FangData
from FangItemUi import FangItemUi
from LoadPicThread import LoadPicThread

ui_file = 'MainUI.ui'
(class_ui, class_basic_class) = uic.loadUiType(ui_file)

class FangUI(class_basic_class, class_ui):

    def __init__(self):
        super(FangUI, self).__init__()
        self.url = "http://esf.nanjing.fang.com/"
        self.setupUi(self)

        self.loadPicThread = LoadPicThread()
        self.loadPicThread.signal_load_pic.connect(self.loadPicOneByOne)

        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 700)
        self.pushButton_refresh.clicked.connect(self._readAndShowTableWidget)

        verticalHeader = self.tableWidget.verticalHeader()
        verticalHeader.setDefaultSectionSize(135)

        self._readAndShowTableWidget()

    def _readAndShowTableWidget(self):
        self.totlist = FangData().printli()
        for i, item in enumerate(self.totlist):
            # for j,data in enumerate(item):
            #     newItem = QTableWidgetItem(data)
            #     self.tableWidget.setItem(i, j, newItem)
            newItem = QTableWidgetItem(item[0])
            self.tableWidget.setItem(i, 0, newItem)
            fangItem = FangItemUi()
            fangItem._setItemData(item)
            self.tableWidget.setCellWidget(i, 1, fangItem)

        self._notifyItemPicture()

    def _addHouseUrl(self,i,j,data):
        label = QLabel(data)
        self.tableWidget.setCellWidget(i, j, label)

    def _addHousePic(self,i,j,data):
        label = QLabel()
        pixmap = QPixmap()
        pic = requests.get(data).content
        pixmap.loadFromData(pic)
        label.setPixmap(pixmap)
        self.tableWidget.setCellWidget(i, j, label)

    def loadPicOneByOne(self,rows_index,pixmap):
        label = QLabel()
        label.setPixmap(pixmap)
        self.tableWidget.removeCellWidget(rows_index, 0);
        self.tableWidget.setCellWidget(rows_index, 0, label)
    def _notifyItemPicture(self):
        self.loadPicThread.start_thread(self.totlist)

    def keyPressEvent(self,event):
        if (event.key() == Qt.Key_Escape):
            reply = QMessageBox.information(self,  # 使用infomation信息框
                                            "退出",
                                            "是否确认退出？",
                                            QMessageBox.Yes | QMessageBox.No)
            if(reply == QMessageBox.Yes):
               self.close()




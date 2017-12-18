from PyQt5 import uic
# from PyQt5 import QtWebEngineWidgets

ui_file = 'FrangItemUI.ui'
(class_ui, class_basic_class) = uic.loadUiType(ui_file)

class FangItemUi(class_basic_class, class_ui):

    def __init__(self):
        super(FangItemUi, self).__init__()
        self.setupUi(self)
        self.label_website.setOpenExternalLinks(True)

        # eqwe = QWebView()
    def _setItemData(self,list):

        self.label_item_title.setText(list[1])#房源标题信息
        self.label_item_info.setText(list[2])#小区名字
        self.label_item_district.setText(list[3])#小区名字
        self.label_item_address.setText(list[4])#地址
        self.label_item_measure_area.setText(list[5])#面积
        self.label_item_price.setText(list[6])#价格
        self.label_website.setText("<a href='"+ list[7] +"'>点击打开网页</a>")#网页地址

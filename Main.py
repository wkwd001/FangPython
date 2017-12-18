from PyQt5 import QtWidgets

from FangUI import FangUI

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    fangUI = FangUI()
    fangUI.show()

    sys.exit(app.exec_())



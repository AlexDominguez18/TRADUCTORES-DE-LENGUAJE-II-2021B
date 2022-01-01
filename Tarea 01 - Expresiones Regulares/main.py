from PyQt5 import QtWidgets
from mainwindow import MainWindow

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
import sys
import singal_and_slot
from PySide6.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    mainwindow = QMainWindow()
    ui = singal_and_slot.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())

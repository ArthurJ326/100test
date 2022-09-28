import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle("主窗口画面Title")
        self.setWindowIcon(QIcon("D:/PYCHARM/100test/100test/Controls/Icon/th.ico"))

        #  设置尺寸
        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage("只存在五秒的消息",5000)


if __name__ == '__main__':
    app= QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("D:/PYCHARM/100test/100test/Controls/Icon/test.ico"))
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

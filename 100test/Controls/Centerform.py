import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon


class Centerform(QMainWindow):
    def __init__(self, parent=None):
        super(Centerform, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle("居中窗口")

        #  设置尺寸
        self.resize(400, 300)
        self.center()

    def center(self):
        # 获取窗口的坐标

        size = self.geometry()

        # 获取屏幕的坐标系

        screen = QApplication.primaryScreen().geometry()

        new_top= (screen.height() - size.height()) / 2
        new_left = (screen.width() - size.width()) / 2

        self.move(new_left,new_top)


if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("D:/PYCHARM/100test/100test/Controls/Icon/test.ico"))
    main = Centerform()
    main.show()
    sys.exit(app.exec_())

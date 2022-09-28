import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QToolTip, QHBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QIcon, QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        QToolTip.setFont(QFont("隶书", 18))
        self.setToolTip("马上国庆了")
        self.setGeometry(400, 300, 250, 250)
        self.setWindowTitle("TOOL TIP")

        self.button = QPushButton("按钮")

        self.button.setToolTip("我是按钮，你按啊")

        layout = QHBoxLayout()

        layout.addWidget(self.button)
        mainFram = QWidget()
        mainFram.setLayout(layout)
        self.setCentralWidget(mainFram)

if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())

import sys
from PySide6.QtWidgets import QMainWindow, QApplication,QHBoxLayout,QWidget,QPushButton
from PySide6.QtGui import QIcon


class QuitApplication(QMainWindow):
    def  __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(400,300)
        self.setWindowTitle("退出应用")


        self.button = QPushButton("退出应用按钮")
        # 把信号与槽关联
        self.button.clicked.connect (self.QuitClick_button)
        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        mainframe = QWidget()
        mainframe.setLayout(layout)
        self.setCentralWidget(mainframe)

    # 单机事件的方法
    def QuitClick_button(self):
        sender = self.sender()

        print(sender.text()+'被按下')
        app=QApplication.instance()
        app.quit()
if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()


    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())




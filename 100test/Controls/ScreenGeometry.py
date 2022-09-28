import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton

if not QApplication.instance():

    app = QApplication(sys.argv)
else:
    app = QApplication.instance()


def On_click_button():
    print("On_click_button")


widget = QWidget()

btn = QPushButton(widget)

btn.clicked.connect(On_click_button)

btn.setText("按钮")

btn.move(50, 80)

widget.resize(1920,1080)

btn.resize(100, 50)

widget.setWindowTitle("屏幕坐标系")

widget.show()

sys.exit(app.exec_())

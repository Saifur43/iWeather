import sys
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QMessageBox
import crawler


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lbl = QtWidgets.QLabel("Welcome to iWeather")
        self.lbl.setAlignment(Qt.Qt.AlignCenter)
        self.lbl2 = QtWidgets.QLabel("Enter any City Name from Bangladesh:")
        self.btn = QtWidgets.QPushButton("Get Weather!")
        self.text = QtWidgets.QLineEdit()

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.lbl)
        self.v_box.addStretch()
        self.v_box.addWidget(self.lbl2)
        self.v_box.addWidget(self.text)
        self.v_box.addWidget(self.btn)
        self.v_box.addStretch()

        self.btn.clicked.connect(self.get_weather)

        self.setLayout(self.v_box)
        self.setWindowTitle("iWeather")
        self.resize(250, 200)
        self.show()

    def get_weather(self):
        city_name = self.text.text()
        temp = crawler.get(city_name)
        mag = QMessageBox()
        mag.setIcon(QMessageBox.Information)
        mag.setText("The Weather of " + city_name + " is " + temp)
        mag.setWindowTitle("MessageBox demo")
        mag.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mag.exec_()


app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())

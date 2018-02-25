import sys
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QMessageBox
import crawler, default_city
from edit_city import EditWin


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lbl = QtWidgets.QLabel("Welcome to iWeather")
        self.lbl.setAlignment(Qt.Qt.AlignCenter)
        self.lbl3 = QtWidgets.QLabel()  # temp label
        self.lbl3.setAlignment(Qt.Qt.AlignCenter)
        self.city_lbl = QtWidgets.QLabel()  # city name label
        self.city_lbl.setAlignment(Qt.Qt.AlignCenter)
        # weather report label
        self.btn = QtWidgets.QPushButton("About")
        self.btn2 = QtWidgets.QPushButton("Change City")
        # creating vertical layout
        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.lbl)
        self.v_box.addStretch()
        self.v_box.addWidget(self.city_lbl)
        self.v_box.addWidget(self.lbl3)
        self.v_box.addStretch()

        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.btn)
        self.h_box.addWidget(self.btn2)

        self.v_box.addLayout(self.h_box)
        self.get_city()
        self.get_weather()

        self.btn.clicked.connect(self.about)
        self.btn2.clicked.connect(self.edit_win)

        self.setLayout(self.v_box)
        self.setWindowTitle("iWeather")
        self.resize(250, 200)
        self.show()

    def edit_win(self):
        self.ew = EditWin()
        self.ew.show()

    def about(self):
        mag = QMessageBox()
        mag.setIcon(QMessageBox.Information)
        mag.setText("Saifur Rahman")
        mag.setInformativeText("Dept of CSE, Comilla University")
        mag.setWindowTitle("About Developer")
        mag.setStandardButtons(QMessageBox.Ok)
        mag.exec_()

    def get_weather(self):
        city_name = default_city.get_default()
        weather = crawler.get(city_name)
        self.lbl3.setText(weather)

    def get_city(self):
        city_name = default_city.get_default()
        city_name_s = city_name.title()
        self.city_lbl.setText(city_name_s)


app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())

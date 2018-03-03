import sys
from PyQt5 import QtWidgets, Qt, QtGui
import crawler, default_city
from edit_city import EditWin
from about import About


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lbl = QtWidgets.QLabel("Welcome to iWeather")
        self.lbl.setAlignment(Qt.Qt.AlignCenter)
        self.lbl3 = QtWidgets.QLabel()   # weather report label
        self.lbl3.setAlignment(Qt.Qt.AlignCenter)
        self.city_lbl = QtWidgets.QLabel()  # city name label
        self.city_lbl.setAlignment(Qt.Qt.AlignCenter)
        self.btn = QtWidgets.QPushButton("About")
        self.btn2 = QtWidgets.QPushButton("Change City")
        self.btn3 = QtWidgets.QPushButton("Refresh")
        self.img_lbl = QtWidgets.QLabel()
        crawler.get_img(default_city.get_default())
        self.img_lbl.setPixmap(QtGui.QPixmap("images/weather.png"))
        self.img_lbl.setAlignment(Qt.Qt.AlignCenter)

        with open("qss/style.stylesheet", "r") as fh:
            self.setStyleSheet(fh.read())

        # creating vertical layout
        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.lbl)
        self.v_box.addStretch()
        self.v_box.addWidget(self.city_lbl)
        self.city_lbl.setFont(QtGui.QFont('SansSerif', 10))
        self.v_box.addWidget(self.img_lbl)
        self.v_box.addWidget(self.lbl3)
        self.lbl3.setFont(QtGui.QFont('SansSerif', 10))
        self.v_box.addStretch()

        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.btn)
        self.h_box.addWidget(self.btn3)
        self.h_box.addWidget(self.btn2)

        self.v_box.addLayout(self.h_box)
        self.get_city()
        self.get_weather()

        self.btn.clicked.connect(self.about)
        self.btn2.clicked.connect(self.edit_win)
        self.btn3.clicked.connect(self.refresh)

        self.setLayout(self.v_box)
        self.setWindowTitle("iWeather")
        self.resize(300, 250)
        self.show()

    def edit_win(self):
        self.ew = EditWin()
        self.ew.show()

    def about(self):
        self.aw = About()
        self.aw.show()

    def get_weather(self):
        city_name = default_city.get_default()
        weather = crawler.get(city_name)
        self.lbl3.setText(weather)

    def get_city(self):
        city_name = default_city.get_default()
        city_name_s = city_name.title()
        self.city_lbl.setText(city_name_s)

    def refresh(self):
        self.get_city()
        self.get_weather()
        crawler.get_img(default_city.get_default())
        self.img_lbl.setPixmap(QtGui.QPixmap("images/weather.png"))


app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())

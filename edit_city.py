from PyQt5 import QtWidgets
import default_city


class EditWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QtWidgets.QPushButton("Confirm")
        self.text = QtWidgets.QLineEdit()
        self.lbl = QtWidgets.QLabel("Enter new city name:")

        with open("qss/style.stylesheet", "r") as fh:
            self.setStyleSheet(fh.read())

        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.lbl)
        self.box.addWidget(self.text)
        self.box.addWidget(self.btn)

        self.btn.clicked.connect(self.btn_clicked)
        self.setLayout(self.box)
        self.setWindowTitle("Edit")

    def btn_clicked(self):
        city = self.text.text()
        default_city.set_default(city)
        QtWidgets.QApplication.exit()
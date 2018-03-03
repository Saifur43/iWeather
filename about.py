from PyQt5 import QtWidgets, QtGui


class About(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.name_lbl = QtWidgets.QLabel("Saifur Rahman")
        self.img_lbl = QtWidgets.QLabel()
        self.img_lbl.setPixmap(QtGui.QPixmap("images/image.jpg"))
        self.dept_lbl = QtWidgets.QLabel("Dept of CSE, Comilla University")
        self.email_lbl = QtWidgets.QLabel("saifurrahmany43@gmail.com")

        with open("qss/style.stylesheet", "r") as fh:
            self.setStyleSheet(fh.read())

        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.img_lbl)
        self.box.addWidget(self.name_lbl)
        self.box.addWidget(self.dept_lbl)
        self.box.addWidget(self.email_lbl)

        self.setLayout(self.box)
        self.setWindowTitle("About")

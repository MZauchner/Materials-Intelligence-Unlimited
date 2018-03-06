from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import sys
from D1 import *
from D2 import *
from D3 import Python3SolenoidDriver as p3
from D4 import *
from D5 import *
from D6 import *
from D7 import analysis
import sys
sys.path.append("..")
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton("move forward")
        self.l = QtWidgets.QLabel("rod silo")
        self.b2 = QtWidgets.QPushButton("move backward")
        self.b3= QtWidgets.QPushButton("move forward")
        self.b4= QtWidgets.QPushButton("move backward")
        self.l2= QtWidgets.QLabel("slide silo")

        self.l10= QtWidgets.QLabel("slide holder")
        self.b15 = QtWidgets.QPushButton("tilt")
        self.b16 = QtWidgets.QPushButton("move back")
        self.l3= QtWidgets.QLabel("excitation")
        self.b5 = QtWidgets.QPushButton("excite rod")
        self.b6 = QtWidgets.QPushButton("excite slide")
        self.b7 = QtWidgets.QPushButton("move to slide")
        self.b8 = QtWidgets.QPushButton("move to rod")
        self.l4= QtWidgets.QLabel("frequency analysis")
        self.b9 = QtWidgets.QPushButton("excite and measure (rod)")
        self.b10 = QtWidgets.QPushButton("excite and measure (slide)")
        self.b11 = QtWidgets.QPushButton("move forward")
        self.b12 = QtWidgets.QPushButton("move backward")
        self.l5 = QtWidgets.QLabel("conveyor belt")
        self.l6 = QtWidgets.QLabel("run all")
        self.b13 = QtWidgets.QPushButton("run")
        self.b14 = QtWidgets.QPushButton("stop")


        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()

        hbox.addStretch()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.l)

        vbox.addWidget(self.b) #rod silo
        vbox.addWidget(self.b2)
        vbox.addWidget(self.l2) #slide silo
        vbox.addWidget(self.b4)
        vbox.addWidget(self.b3)
        vbox.addWidget(self.l10) #slide holder
        vbox.addWidget(self.b15)
        vbox.addWidget(self.b16)
        vbox.addWidget(self.l3) #excitation
        vbox.addWidget(self.b5)
        vbox.addWidget(self.b6)
        vbox.addWidget(self.b7)
        vbox.addWidget(self.b8)
        vbox.addWidget(self.l4) #frequency
        vbox.addWidget(self.b9)
        vbox.addWidget(self.b10)
        vbox.addWidget(self.l5) #conveyor belt
        vbox.addWidget(self.b11)
        vbox.addWidget(self.b12)
        vbox.addWidget(self.l6) #run all
        vbox.addWidget(self.b13)
        vbox.addWidget(self.b14)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setWindowTitle("VibratINC Quality Control")
        self.show()
        self.b.clicked.connect(self.click)


    def click(self):
        analysis.analyze(1,2,3,"rod")

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())


import sys

from D1 import stepperD1python
from D2 import slide_holder as sh
from D3 import Python3SolenoidDriver as p3
from D4 import conveyor as conv
from D5 import pyserial_control as psc
from D7 import analysis
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

sys.path.append("..")
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton("push in")
        self.l = QtWidgets.QLabel("rod silo")
        self.b2 = QtWidgets.QPushButton("push out")
        self.b3= QtWidgets.QPushButton("push in")
        self.b4= QtWidgets.QPushButton("adjust +36 deg")
        self.l2= QtWidgets.QLabel("slide silo")

        self.l10= QtWidgets.QLabel("slide holder")
        self.b15 = QtWidgets.QPushButton("forward")
        self.b16 = QtWidgets.QPushButton("backward")
        self.b18 = QtWidgets.QPushButton("both")
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
        self.b17= QtWidgets.QPushButton("adjust -36 deg")


        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()

        hbox.addStretch()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.l)

        vbox.addWidget(self.b) #rod silo
        vbox.addWidget(self.b2)
        vbox.addWidget(self.l2) #slide silo
        vbox.addWidget(self.b4)
        vbox.addWidget(self.b17)
        vbox.addWidget(self.b3)
        vbox.addWidget(self.l10) #slide holder
        vbox.addWidget(self.b15)
        vbox.addWidget(self.b16)
        vbox.addWidget(self.b18)
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

        """buttons for rodsilo"""
        self.b.clicked.connect(self.rodsilo_push_in) #pushes into holder
        self.b2.clicked.connect(self.rodsilo_push_out) #pushes out of holder

        """buttons for slidesilo"""
        self.b4.clicked.connect(self.slideforward)
        self.b17.clicked.connect(self.slidebackward)
        self.b3.clicked.connect(self.sliderotate) #pushes into holder

        """buttons for slideholder"""
        self.b15.clicked.connect(self.slideholderforward)
        self.b16.clicked.connect(self.slideholderbackward)
        self.b18.clicked.connect(self.slideholderboth) #pushes into holder

        """buttons for excitation"""
        self.b5.clicked.connect(self.exciterod) #excite rod
        self.b6.clicked.connect(self.exicteslide) #excite slide
        self.b7.clicked.connect(self.moveslide) #move to slide
        self.b8.clicked.connect(self.moverod) #move to rod

        """buttons for conveyor belt"""
        self.b11.clicked.connect(self.convforward) #forward motion
        self.b12.clicked.connect(self.convbackward) #backward motion


    """function for frequency analysis"""
    def click(self):
        analysis.analyze(1,2,3,"rod")

    """functions for rod silo"""

    def rodsilo_push_in(self):
        stepperD1python.rodsilo(1)

    def rodsilo_push_out(self):
        stepperD1python.rodsilo(2)

    """buttons for slidsilo"""
    def slideforward(self): #adjusts position of stepper motor by +36 degrees
        psc.slidesilo("forward")

    def slidebackward(self): #adjusts position of stepper motor by -36 degrees
        psc.slidesilo("backward")

    def sliderotate(self): #pushes slides into holder
        psc.slidesilo("rotate")


    """button functions for slideholder"""
    def slideholderforward(self):
        sh.slideholder("cw")
    def slideholderbackward(self):
        sh.slideholder("ccw")
    def slideholderboth(self):
        sh.slideholder("both")

    """functions for excitation"""
    def exciterod(self):
        p3.test("rod")
    def exicteslide(self):
        p3.test("slide")
    def moveslide(self):
        return 0
    def moverod(self):
        return 0

    """functions for conveyor belt"""
    def convforward(self):
        conv.conveyor("1")
    def convbackward(self):
        conv.conveyor("2")



app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

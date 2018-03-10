import sys

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import \
    NavigationToolbar2QT as NavigationToolbar

from D1 import stepperD1python
from D2 import slide_holder as sh
from D3 import manual_pos_driver as p3
from D4 import conveyor as conv
from D5 import pyserial_control as psc
from D7 import analysis
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

sys.path.append("..")
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.init_ui()

    def init_ui(self):
        self.rodfrequency = QtWidgets.QLineEdit("3450")
        self.rodfrequencyl = QtWidgets.QLabel("frequency of rod [Hz]")

        self.slidefrequency = QtWidgets.QLineEdit("1050")
        self.slidefrequencyl = QtWidgets.QLabel("frequency of slide [Hz]")
        self.frequencytolerance = QtWidgets.QLineEdit("100")
        self.frequencytolerancel = QtWidgets.QLabel("tolerated error [Hz]")
        self.result = QtWidgets.QLabel()
        self.resultlabel = QtWidgets.QLabel("result")


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
        self.b13 = QtWidgets.QPushButton("run all")
        self.b14 = QtWidgets.QPushButton("stop")
        self.b17= QtWidgets.QPushButton("adjust -36 deg")


        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()

        hbox.addStretch()



        """button box"""
        vbox = QtWidgets.QVBoxLayout()
        """options box"""
        vbox2 = QtWidgets.QVBoxLayout()
        """plot box"""
        vbox3 = QtWidgets.QVBoxLayout()
        vbox3.addWidget(self.canvas)
        vbox2.addWidget(self.rodfrequencyl)
        vbox2.addWidget(self.rodfrequency)
        vbox2.addWidget(self.slidefrequencyl)
        vbox2.addWidget(self.slidefrequency)
        vbox2.addWidget(self.frequencytolerancel)
        vbox2.addWidget(self.frequencytolerance)
        vbox2.addWidget(self.resultlabel)
        vbox2.addWidget(self.result)
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
        #vbox.addWidget(self.l6) #run all
        vbox.addWidget(self.b13)
        vbox.addWidget(self.b14)
        hbox.addLayout(vbox3)
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox)
        self.setLayout(hbox)
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

        """buttons for frequency analysis"""
        self.b9.clicked.connect(self.analyserod) #analyse rod
        self.b10.clicked.connect(self.analyseslide) #analyse slide


    """function for frequency analysis"""
    def analyserod(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        frequency, amplitude = analysis.analyze("rod")
        resonance = frequency[np.where(amplitude == max(amplitude))]
        rodf = float(self.rodfrequency.text())
        tol = float(self.frequencytolerance.text())
        if resonance <= rodf-tol/2 or resonance >=rodf+tol/2:

            self.result.setText("rejected")
        else:
            self.result.setText("accepted")
        ax.plot(frequency, amplitude)
        self.canvas.draw()

    def analyseslide(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        frequency, amplitude = analysis.analyze("slide")
        resonance = frequency[np.where(amplitude == max(amplitude))]
        print(resonance)
        slidef = float(self.slidefrequency.text())
        tol = float(self.frequencytolerance.text())
        if resonance <= slidef-tol/2 or resonance >=slidef+tol/2:
            self.result.setText("rejected")
        else:
            self.result.setText("accepted")
        plt.plot(frequency, amplitude)
        self.canvas.draw()



    """functions for rod silo"""

    def rodsilo_push_in(self):
        stepperD1python.rodsilo("1")

    def rodsilo_push_out(self):
        stepperD1python.rodsilo("2")

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
        p3.move("rod")
        p3.test("rod")
    def exicteslide(self):
        p3.move("slide")
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

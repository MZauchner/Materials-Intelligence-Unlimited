import sys
import time

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
        self.stopvar = False
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.init_ui()

    def init_ui(self):
        self.rodfrequency = QtWidgets.QLineEdit("4500")
        self.rodfrequencyl = QtWidgets.QLabel("frequency of rod [Hz]")

        self.slidefrequency = QtWidgets.QLineEdit("1050")
        self.slidefrequencyl = QtWidgets.QLabel("frequency of slide [Hz]")
        self.frequencytolerance = QtWidgets.QLineEdit("200")
        self.frequencytolerancel = QtWidgets.QLabel("tolerated error [Hz]")
        self.result = QtWidgets.QLabel()
        self.resultlabel = QtWidgets.QLabel("result")

        self.rodsilo_te = QtWidgets.QLineEdit("/dev/ttyACM0")
        self.slidesilo_te = QtWidgets.QLineEdit("/dev/ttyACM1")
        self.slideholder_te = QtWidgets.QLineEdit("/dev/ttyACM2")
        self.conveyor_te = QtWidgets.QLineEdit("/dev/ttyACM3")
        self.excitation_te = QtWidgets.QLineEdit("/dev/ttyUSB0")
        self.excitation_label = QtWidgets.QLabel("excitation")
        self.conveyor_label = QtWidgets.QLabel("conveyor")
        self.rodsilo_label = QtWidgets.QLabel("rod silo")
        self.slidesilo_label = QtWidgets.QLabel("slide silo")
        self.slideholder_label = QtWidgets.QLabel("slide holder")
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
        self.sample_list = QtWidgets.QListWidget()
        self.button_add_slide = QtWidgets.QPushButton("add slide")
        self.button_remove = QtWidgets.QPushButton("remove")
        self.button_add_rod = QtWidgets.QPushButton("add rod")


        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()

        hbox.addStretch()



        """button box"""
        vbox = QtWidgets.QVBoxLayout()
        """options box"""
        vbox2 = QtWidgets.QVBoxLayout()
        """sample list box"""
        vbox4 = QtWidgets.QVBoxLayout()
        """plot box"""
        vbox3 = QtWidgets.QVBoxLayout()

        vbox4.addWidget(self.sample_list)
        vbox4.addWidget(self.button_add_slide)
        vbox4.addWidget(self.button_add_rod)
        vbox4.addWidget(self.button_remove)
        vbox3.addWidget(self.canvas)
        vbox2.addWidget(self.rodfrequencyl)
        vbox2.addWidget(self.rodfrequency)
        vbox2.addWidget(self.slidefrequencyl)
        vbox2.addWidget(self.slidefrequency)
        vbox2.addWidget(self.frequencytolerancel)
        vbox2.addWidget(self.frequencytolerance)
        vbox3.addWidget(self.resultlabel)
        vbox3.addWidget(self.result)
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
        vbox2.addWidget(self.b13)
        vbox2.addWidget(self.b14)
        vbox2.addWidget(self.slidesilo_label)
        vbox2.addWidget(self.slidesilo_te)
        vbox2.addWidget(self.rodsilo_label)
        vbox2.addWidget(self.rodsilo_te)
        vbox2.addWidget(self.slideholder_label)
        vbox2.addWidget(self.slideholder_te)
        vbox2.addWidget(self.conveyor_label)
        vbox2.addWidget(self.conveyor_te)
        vbox2.addWidget(self.excitation_label)
        vbox2.addWidget(self.excitation_te)
        hbox.addLayout(vbox3)
        hbox.addLayout(vbox4)
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

        """buttons for sample list"""
        self.button_add_slide.clicked.connect(self.add_slide)
        self.button_add_rod.clicked.connect(self.add_rod)
        self.button_remove.clicked.connect(self.remove)

        """automatic mode buttons"""
        self.b13.clicked.connect(self.run_all)
        self.b14.clicked.connect(self.stop)



    """function for frequency analysis"""
    def analyserod(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        frequency, amplitude = analysis.analyze("rod", com_port=self.excitation_te.text())
        resonance = frequency[np.where(amplitude == max(amplitude))]
        rodf = float(self.rodfrequency.text())
        tol = float(self.frequencytolerance.text())
        if resonance <= rodf-tol/2 or resonance >=rodf+tol/2:
            #rejected
            self.result.setText("rejected")
            print(str(resonance))
        else:
            #accepted
            self.result.setText("accepted")
            print(str(resonance))
        ax.plot(frequency, amplitude)
        self.canvas.draw()

    def analyseslide(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        frequency, amplitude = analysis.analyze("slide",com_port=self.excitation_te.text())
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
        stepperD1python.rodsilo("1", com_port = self.rodsilo_te.text())

    def rodsilo_push_out(self):
        stepperD1python.rodsilo("2", com_port=self.rodsilo_te.text())

    """buttons for slidsilo"""
    def slideforward(self): #adjusts position of stepper motor by +36 degrees
        psc.slidesilo("forward", com_port=self.slidesilo_te.text())

    def slidebackward(self): #adjusts position of stepper motor by -36 degrees
        psc.slidesilo("backward", com_port=self.slidesilo_te.text())

    def sliderotate(self): #pushes slides into holder
        psc.slidesilo("rotate", com_port=self.slidesilo_te.text())


    """button functions for slideholder"""
    def slideholderforward(self):
        sh.slideholder("cw", com_port=self.slideholder_te.text())
    def slideholderbackward(self):
        sh.slideholder("ccw", com_port=self.slideholder_te.text())
    def slideholderboth(self):
        sh.slideholder("both", com_port=self.slideholder_te.text())

    """functions for excitation"""
    def exciterod(self):
        p3.move("rod",com_port=self.excitation_te.text())
        p3.test("rod",com_port=self.excitation_te.text())
    def exicteslide(self):
        p3.move("slide", com_port=self.excitation_te.text())
        p3.test("slide",com_port=self.excitation_te.text())
    def moveslide(self):
        p3.move("slide",com_port=self.excitation_te.text())
    def moverod(self):
        p3.move("rod",com_port=self.excitation_te.text())

    """functions for conveyor belt"""
    def convforward(self):
        conv.conveyor("1", com_port=self.conveyor_te.text())
    def convbackward(self):
        conv.conveyor("2", com_port=self.conveyor_te.text())

    """function for full automation. This is rather convoluted, because
     I need to test if someone clicked the stop button after each step of the
     process and make sure that the samples come out in the correct order.
     I wouldn't try to understand the actual code, but what it essentially does is:
     iterate over every element in the list and execute the routine for the type
     of sample. If the sample is rejected: test the same sample again. If it
     is accepted, continue to the next and remove the sample from the sample list.
     If someone clicked the stop button during execution, the while loop breaks append
     automatic execution is stopped.
    """

    def run_all(self):
        self.stopvar = False
        self.rejected = False
        itemsTextList =  [str(self.sample_list.item(i).text()) for i in range(self.sample_list.count())]
        itemindex = 0
        while itemindex < len(list(itemsTextList)):
            if itemsTextList[itemindex] == "slide" and self.stopvar == False:
                if self.stopvar == False:
                    self.sliderotate() #push slide into slide_holder
                else:
                    break
                time.sleep(3)
                if self.stopvar == False:
                    self.analyseslide() #analyse slide
                else:
                    break
                if self.stopvar == False:
                    self.moverod() #move excitation device to rod to prevent collision
                else:
                    break
                time.sleep(2)
                if self.stopvar == False:
                    self.slideholderboth() #eject slide from slideholder
                else:
                    break
                if self.result.text() == "rejected":
                    self.rejected = True
                    if self.stopvar == False:
                        self.convbackward()#reject sample
                    else:
                        break
                else:
                    self.rejected = False
                    itemindex += 1 #move to next sample
                    if self.stopvar == False:
                        self.convforward()#accept sample
                        items_list = self.sample_list.findItems("slide",Qt.MatchExactly)
                        item = items_list[0]
                        r = self.sample_list.row(item)
                        self.sample_list.takeItem(r) #remove item from sample_list
                    else:
                        break


            if itemsTextList[itemindex]  == "rod" and self.stopvar == False:
                if self.stopvar == False:
                    self.rodsilo_push_in()  # push rod in

                else:
                    break
                time.sleep(3)
                if self.stopvar == False:
                    self.analyserod()

                else:
                    break
                time.sleep(2)
                if self.stopvar == False:
                    self.rodsilo_push_out() # push rod out

                else:
                    break
                if self.result.text() == "rejected":
                    self.rejected = True
                    if self.stopvar == False:
                        self.convbackward()#reject sample

                    else:
                        break
                else:
                    self.rejected = False
                    itemindex += 1 # move to next sample
                    if self.stopvar == False:
                        self.convforward()#accept sample
                        items_list = self.sample_list.findItems("rod",Qt.MatchExactly)
                        item = items_list[0]
                        r = self.sample_list.row(item)
                        self.sample_list.takeItem(r) #remove item from sample_list
                    else:
                        break
            else:
                break


    def stop(self):
        self.stopvar = True


    def add_slide(self):
        self.sample_list.addItem("slide")
    def add_rod(self):
        self.sample_list.addItem("rod")
    def remove(self):
        try:
            item = self.sample_list.selectedItems()[0]
            self.sample_list.takeItem(self.sample_list.row(item))
        except:
            pass



app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())


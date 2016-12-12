from PyQt4 import QtGui,QtCore # Import the PyQt4 module we'll need

import sys # We need sys so that we can pass argv to QApplication
import random
import re

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from matplotlib.backend_bases import FigureManagerBase, key_press_handler

import boxClass
import box
import design

def def_PlotBase(self):
    pass


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        #
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.canvas.setFocus()
        self.canvas.mpl_connect('key_press_event', self.on_key_press)
        # Toolbar von Plots
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)

        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.addWidget(self.mpl_toolbar)
        self.plotLayout.addWidget(self.canvas)
        self.PlotWidget = QtGui.QWidget()
        self.PlotWidget.setLayout(self.plotLayout)

        # stacked widget which can hold multiple Plot Librarys
        self.stackedWidget.insertWidget(0,self.PlotWidget)
        self.stackedWidget.setCurrentIndex(0)

        self.PlotBaseRandom()
        self.CreateConnections()


    def CreateConnections(self):
        self.pb_loadVal.clicked.connect(self.loadValues)


    def loadValues(self):

        print("load val")
        # Grab Line Edit
        values = self.te_Values.toPlainText()

        P = re.compile("\d*[\.,]?\d*")
        values = P.findall(values)
        values = [str(x) for x in values]
        values = [x.replace(",", ".") for x in values if x is not '']

        print (values)
        self.PlotBase(values)


    def PlotBase(self,data):
        # plot data
        ax = self.figure.get_axes()


        # discards the old graph
        ax[0].hold(False)

        ax[0].plot(data, '*-')

        # refresh canvas
        self.canvas.draw()


    def loadPlugin(self):
        pass


    def PlotBaseRandom(self):
        data = [random.random() for i in range(10)]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()


    def on_key_press(self, event):
        """ redirects the KeyPress event to the MPL"""
        # implement the default mpl key press events described at
        # http://matplotlib.sourceforge.net/users/navigation_toolbar.html#navigation-keyboard-shortcuts
        key_press_handler(event, self.canvas, self.mpl_toolbar)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1DProcessing.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(837, 430)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.VertLayout_Main = QtGui.QVBoxLayout()
        self.VertLayout_Main.setObjectName(_fromUtf8("VertLayout_Main"))
        self.widget_Main = QtGui.QWidget(self.centralwidget)
        self.widget_Main.setMinimumSize(QtCore.QSize(500, 0))
        self.widget_Main.setObjectName(_fromUtf8("widget_Main"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_Main)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.widget_Main)
        self.widget.setMinimumSize(QtCore.QSize(350, 50))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(60, 10, 281, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 56, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.widget)
        self.tabWidget = QtGui.QTabWidget(self.widget_Main)
        self.tabWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pb_loadVal = QtGui.QPushButton(self.tab)
        self.pb_loadVal.setGeometry(QtCore.QRect(10, 50, 85, 27))
        self.pb_loadVal.setObjectName(_fromUtf8("pb_loadVal"))
        self.te_Values = QtGui.QTextEdit(self.tab)
        self.te_Values.setGeometry(QtCore.QRect(10, 80, 321, 181))
        self.te_Values.setObjectName(_fromUtf8("te_Values"))
        self.pb_loadVal.raise_()
        self.te_Values.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.stackedWidget = QtGui.QStackedWidget(self.widget_Main)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.VertLayout_Main.addWidget(self.widget_Main)
        self.verticalLayout_3.addLayout(self.VertLayout_Main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 837, 27))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionLaden = QtGui.QAction(MainWindow)
        self.actionLaden.setObjectName(_fromUtf8("actionLaden"))
        self.actionSpeichern = QtGui.QAction(MainWindow)
        self.actionSpeichern.setObjectName(_fromUtf8("actionSpeichern"))
        self.menuFile.addAction(self.actionLaden)
        self.menuFile.addAction(self.actionSpeichern)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Plugin", None))
        self.pb_loadVal.setText(_translate("MainWindow", "LoadValues", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuFile.setTitle(_translate("MainWindow", "Datei", None))
        self.actionLaden.setText(_translate("MainWindow", "laden", None))
        self.actionSpeichern.setText(_translate("MainWindow", "speichern", None))


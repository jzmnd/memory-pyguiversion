#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
mainwindow.py
Form implementation generated from reading ui file 'mainwindow.ui'
Created by: PyQt4 UI code generator 4.11.4

Modified by Jeremy Smith
University of California, Berkeley
j-smith@eecs.berkeley.edu
"""

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
        MainWindow.resize(750, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 730, 580))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))

        self.comboBox_1 = QtGui.QComboBox(self.tab_1)
        self.comboBox_1.setGeometry(QtCore.QRect(130, 30, 104, 26))
        self.comboBox_1.setObjectName(_fromUtf8("comboBox_1"))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.tab_1)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 60, 104, 26))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))

        self.label_1 = QtGui.QLabel(self.tab_1)
        self.label_1.setGeometry(QtCore.QRect(30, 30, 80, 16))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.label_2 = QtGui.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 80, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 90, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(330, 30, 161, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(330, 60, 171, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(330, 90, 161, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(330, 120, 59, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.lineEdit_1 = QtGui.QLineEdit(self.tab_1)
        self.lineEdit_1.setGeometry(QtCore.QRect(130, 100, 120, 21))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 30, 113, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(510, 60, 113, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_1)
        self.lineEdit_4.setGeometry(QtCore.QRect(510, 90, 113, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_1)
        self.lineEdit_5.setGeometry(QtCore.QRect(510, 120, 113, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        self.textBrowser_1 = QtGui.QTextBrowser(self.tab_1)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 260, 700, 280))
        self.textBrowser_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_1.setObjectName(_fromUtf8("textBrowser_1"))

        self.pushButton_1 = QtGui.QPushButton(self.tab_1)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 160, 161, 32))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 200, 113, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_1)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 200, 113, 32))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_9 = QtGui.QPushButton(self.tab_1)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 200, 113, 32))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))

        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))

        self.comboBox_3 = QtGui.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 30, 104, 26))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))

        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 80, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))        
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(330, 30, 161, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(330, 60, 161, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(330, 90, 59, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.lineEdit_11 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(130, 70, 120, 21))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit"))        
        self.lineEdit_6 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(510, 30, 113, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(510, 60, 113, 21))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(510, 90, 113, 21))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))

        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 260, 700, 280))
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))

        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 160, 161, 32))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 200, 113, 32))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 200, 113, 32))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_10 = QtGui.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(270, 200, 113, 32))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))

        self.graphicsView = QtGui.QGraphicsView(self.tab_3)
        self.graphicsView.setGeometry(QtCore.QRect(30, 20, 400, 500))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(450, 20, 59, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(450, 80, 59, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))

        self.lineEdit_9 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(450, 40, 250, 21))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(450, 100, 100, 21))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))

        self.pushButton_6 = QtGui.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(570, 95, 80, 32))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 160, 120, 32))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MemTest v1.0", None))

        self.comboBox_1.setItemText(0, _translate("MainWindow", "0", None))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "1", None))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "2", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1x1", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2x2", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3x3", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1x1", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2x2", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3x3", None))

        self.lineEdit_1.setText(_translate("MainWindow", "0", None))
        self.lineEdit_2.setText(_translate("MainWindow", "100", None))
        self.lineEdit_3.setText(_translate("MainWindow", "200", None))
        self.lineEdit_4.setText(_translate("MainWindow", "100", None))
        self.lineEdit_5.setText(_translate("MainWindow", "1", None))
        self.lineEdit_6.setText(_translate("MainWindow", "100", None))
        self.lineEdit_7.setText(_translate("MainWindow", "100", None))
        self.lineEdit_8.setText(_translate("MainWindow", "1", None))
        self.lineEdit_9.setText(_translate("MainWindow", "datafile", None))
        self.lineEdit_10.setText(_translate("MainWindow", "1", None))
        self.lineEdit_11.setText(_translate("MainWindow", "0", None))

        self.label_1.setText(_translate("MainWindow", "Word line", None))
        self.label_2.setText(_translate("MainWindow", "Array size", None))
        self.label_3.setText(_translate("MainWindow", "Write Pattern", None))
        self.label_4.setText(_translate("MainWindow", "Write pulse width [ms]", None))
        self.label_5.setText(_translate("MainWindow", "Precharge pulse width [ms]", None))
        self.label_6.setText(_translate("MainWindow", "GND pulse width [ms]", None))
        self.label_7.setText(_translate("MainWindow", "Loops", None))
        self.label_8.setText(_translate("MainWindow", "Array size", None))
        self.label_9.setText(_translate("MainWindow", "Write pulse width [ms]", None))
        self.label_10.setText(_translate("MainWindow", "GND pulse width [ms]", None))
        self.label_11.setText(_translate("MainWindow", "Loops", None))
        self.label_12.setText(_translate("MainWindow", "Filename", None))
        self.label_13.setText(_translate("MainWindow", "Run #", None))
        self.label_14.setText(_translate("MainWindow", "Write pattern", None))

        self.pushButton_1.setText(_translate("MainWindow", "Initialize variables", None))
        self.pushButton_2.setText(_translate("MainWindow", "RUN", None))
        self.pushButton_3.setText(_translate("MainWindow", "Initialize variables", None))
        self.pushButton_4.setText(_translate("MainWindow", "RUN", None))
        self.pushButton_5.setText(_translate("MainWindow", "Save", None))
        self.pushButton_6.setText(_translate("MainWindow", "Reset", None))
        self.pushButton_7.setText(_translate("MainWindow", "Cancel", None))
        self.pushButton_8.setText(_translate("MainWindow", "Cancel", None))
        self.pushButton_9.setText(_translate("MainWindow", "Continue...", None))
        self.pushButton_10.setText(_translate("MainWindow", "Continue...", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Write-Read", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Write Only", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Results", None))
        
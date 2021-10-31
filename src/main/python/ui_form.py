# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\main\resources\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startTime = QtWidgets.QTimeEdit(self.centralwidget)
        self.startTime.setGeometry(QtCore.QRect(120, 40, 71, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTime.sizePolicy().hasHeightForWidth())
        self.startTime.setSizePolicy(sizePolicy)
        self.startTime.setMaximumSize(QtCore.QSize(75, 16777215))
        self.startTime.setObjectName("startTime")
        self.startTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.startTimeLabel.setGeometry(QtCore.QRect(60, 40, 61, 20))
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.endTime = QtWidgets.QTimeEdit(self.centralwidget)
        self.endTime.setGeometry(QtCore.QRect(120, 140, 71, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endTime.sizePolicy().hasHeightForWidth())
        self.endTime.setSizePolicy(sizePolicy)
        self.endTime.setMaximumSize(QtCore.QSize(75, 16777215))
        self.endTime.setObjectName("endTime")
        self.endTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.endTimeLabel.setGeometry(QtCore.QRect(60, 140, 61, 20))
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.idleTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.idleTimeLabel.setGeometry(QtCore.QRect(60, 90, 47, 13))
        self.idleTimeLabel.setObjectName("idleTimeLabel")
        self.idleTime = QtWidgets.QTimeEdit(self.centralwidget)
        self.idleTime.setGeometry(QtCore.QRect(120, 90, 71, 22))
        self.idleTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.idleTime.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.idleTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.idleTime.setDisplayFormat("hh:mm")
        self.idleTime.setTimeSpec(QtCore.Qt.LocalTime)
        self.idleTime.setObjectName("idleTime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startTimeLabel.setText(_translate("MainWindow", "Start Time"))
        self.endTimeLabel.setText(_translate("MainWindow", "End Time"))
        self.idleTimeLabel.setText(_translate("MainWindow", "Idle Time"))

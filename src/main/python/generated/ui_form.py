################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
from PySide6.QtCore import QLocale
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import QObject
from PySide6.QtCore import QPoint
from PySide6.QtCore import QRect
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtCore import QTime
from PySide6.QtCore import QUrl
from PySide6.QtGui import QBrush
from PySide6.QtGui import QColor
from PySide6.QtGui import QConicalGradient
from PySide6.QtGui import QCursor
from PySide6.QtGui import QFont
from PySide6.QtGui import QFontDatabase
from PySide6.QtGui import QGradient
from PySide6.QtGui import QIcon
from PySide6.QtGui import QImage
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QLinearGradient
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPalette
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QRadialGradient
from PySide6.QtGui import QTransform
from PySide6.QtWidgets import QAbstractSpinBox
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QDateTimeEdit
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMenuBar
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QStatusBar
from PySide6.QtWidgets import QTimeEdit
from PySide6.QtWidgets import QWidget

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 372)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startTime = QTimeEdit(self.centralwidget)
        self.startTime.setObjectName("startTime")
        self.startTime.setGeometry(QRect(120, 20, 100, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTime.sizePolicy().hasHeightForWidth())
        self.startTime.setSizePolicy(sizePolicy)
        self.startTime.setMinimumSize(QSize(100, 0))
        self.startTime.setMaximumSize(QSize(75, 16777215))
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(10)
        self.startTime.setFont(font)
        self.startTimeLabel = QLabel(self.centralwidget)
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.startTimeLabel.setGeometry(QRect(50, 30, 61, 20))
        self.startTimeLabel.setFont(font)
        self.endTime = QTimeEdit(self.centralwidget)
        self.endTime.setObjectName("endTime")
        self.endTime.setGeometry(QRect(120, 80, 100, 41))
        sizePolicy.setHeightForWidth(self.endTime.sizePolicy().hasHeightForWidth())
        self.endTime.setSizePolicy(sizePolicy)
        self.endTime.setMinimumSize(QSize(100, 0))
        self.endTime.setMaximumSize(QSize(75, 16777215))
        self.endTime.setFont(font)
        self.endTimeLabel = QLabel(self.centralwidget)
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.endTimeLabel.setGeometry(QRect(50, 90, 61, 20))
        self.endTimeLabel.setFont(font)
        self.curIdleTimeLabel = QLabel(self.centralwidget)
        self.curIdleTimeLabel.setObjectName("curIdleTimeLabel")
        self.curIdleTimeLabel.setGeometry(QRect(256, 40, 101, 16))
        self.curIdleTimeLabel.setFont(font)
        self.curIdleTime = QTimeEdit(self.centralwidget)
        self.curIdleTime.setObjectName("curIdleTime")
        self.curIdleTime.setEnabled(True)
        self.curIdleTime.setGeometry(QRect(370, 30, 81, 41))
        self.curIdleTime.setMinimumSize(QSize(30, 0))
        self.curIdleTime.setMaximumSize(QSize(100, 16777215))
        self.curIdleTime.setFont(font)
        self.curIdleTime.setReadOnly(True)
        self.curIdleTime.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.curIdleTime.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.curIdleTime.setMaximumTime(QTime(23, 59, 59))
        self.curIdleTime.setCurrentSection(QDateTimeEdit.HourSection)
        self.curIdleTime.setDisplayFormat("hh:mm")
        self.curIdleTime.setTimeSpec(Qt.LocalTime)
        self.workdayHours = QSpinBox(self.centralwidget)
        self.workdayHours.setObjectName("workdayHours")
        self.workdayHours.setGeometry(QRect(160, 130, 61, 41))
        self.workdayHours.setFont(font)
        self.workdayHours.setValue(9)
        self.workdayHoursLabel = QLabel(self.centralwidget)
        self.workdayHoursLabel.setObjectName("workdayHoursLabel")
        self.workdayHoursLabel.setGeometry(QRect(50, 140, 91, 20))
        self.workdayHoursLabel.setFont(font)
        self.consoleTextArea = QPlainTextEdit(self.centralwidget)
        self.consoleTextArea.setObjectName("consoleTextArea")
        self.consoleTextArea.setGeometry(QRect(20, 190, 481, 141))
        self.consoleTextArea.setReadOnly(True)
        self.consoleLabel = QLabel(self.centralwidget)
        self.consoleLabel.setObjectName("consoleLabel")
        self.consoleLabel.setGeometry(QRect(20, 170, 81, 21))
        self.consoleLabel.setFont(font)
        self.idleThresholdLabel = QLabel(self.centralwidget)
        self.idleThresholdLabel.setObjectName("idleThresholdLabel")
        self.idleThresholdLabel.setGeometry(QRect(250, 140, 111, 20))
        self.idleThresholdLabel.setFont(font)
        self.idleThreshold = QSpinBox(self.centralwidget)
        self.idleThreshold.setObjectName("idleThreshold")
        self.idleThreshold.setGeometry(QRect(370, 130, 61, 41))
        self.idleThreshold.setFont(font)
        self.idleThreshold.setValue(20)
        self.totalIdleTimeLabel = QLabel(self.centralwidget)
        self.totalIdleTimeLabel.setObjectName("totalIdleTimeLabel")
        self.totalIdleTimeLabel.setGeometry(QRect(270, 90, 101, 16))
        self.totalIdleTimeLabel.setFont(font)
        self.totalIdleTime = QTimeEdit(self.centralwidget)
        self.totalIdleTime.setObjectName("totalIdleTime")
        self.totalIdleTime.setEnabled(True)
        self.totalIdleTime.setGeometry(QRect(370, 80, 81, 41))
        self.totalIdleTime.setMinimumSize(QSize(30, 0))
        self.totalIdleTime.setMaximumSize(QSize(100, 16777215))
        self.totalIdleTime.setFont(font)
        self.totalIdleTime.setReadOnly(True)
        self.totalIdleTime.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.totalIdleTime.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.totalIdleTime.setMaximumTime(QTime(23, 59, 59))
        self.totalIdleTime.setCurrentSection(QDateTimeEdit.HourSection)
        self.totalIdleTime.setDisplayFormat("hh:mm")
        self.totalIdleTime.setTimeSpec(Qt.LocalTime)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 524, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Hourly Tracker", None))
        self.startTimeLabel.setText(QCoreApplication.translate("MainWindow", "Start Time", None))
        self.endTimeLabel.setText(QCoreApplication.translate("MainWindow", "End Time", None))
        self.curIdleTimeLabel.setText(QCoreApplication.translate("MainWindow", "Current Idle Time", None))
        self.workdayHoursLabel.setText(QCoreApplication.translate("MainWindow", "Workday Hours", None))
        self.consoleLabel.setText(QCoreApplication.translate("MainWindow", "Console Log", None))
        self.idleThresholdLabel.setText(QCoreApplication.translate("MainWindow", "Idle Threshold (m)", None))
        self.totalIdleTimeLabel.setText(QCoreApplication.translate("MainWindow", "Total Idle Time", None))
    # retranslateUi

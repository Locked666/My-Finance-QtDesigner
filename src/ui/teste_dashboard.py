# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1263, 876)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(8, 8, 8)")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 80))
        self.topBar.setMaximumSize(QSize(16777215, 80))
        self.topBar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 5px 0px 0px 5px;\n"
"}")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.topBar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.topBar)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 30))
        self.titleBar.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(1504, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.actionButtonsBar = QFrame(self.titleBar)
        self.actionButtonsBar.setObjectName(u"actionButtonsBar")
        self.actionButtonsBar.setMinimumSize(QSize(100, 0))
        self.actionButtonsBar.setMaximumSize(QSize(100, 16777215))
        self.actionButtonsBar.setStyleSheet(u"")
        self.actionButtonsBar.setFrameShape(QFrame.StyledPanel)
        self.actionButtonsBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.actionButtonsBar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.actionButtonsBar)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(17, 17))

        self.horizontalLayout_8.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.actionButtonsBar)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(30, 30))
        self.pushButton_5.setMaximumSize(QSize(30, 30))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(17, 17))

        self.horizontalLayout_8.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.actionButtonsBar)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0) ;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(17, 17))

        self.horizontalLayout_8.addWidget(self.pushButton_4)


        self.horizontalLayout_7.addWidget(self.actionButtonsBar)


        self.verticalLayout_5.addWidget(self.titleBar)

        self.actionBar = QFrame(self.topBar)
        self.actionBar.setObjectName(u"actionBar")
        self.actionBar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QSpacer {\n"
"	background-color: rgb(13, 9, 36);\n"
"}")
        self.actionBar.setFrameShape(QFrame.NoFrame)
        self.actionBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.actionBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.actionBar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(250, 0))
        self.frame_6.setMaximumSize(QSize(250, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 15)
        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(40, 40))
        self.frame_5.setMaximumSize(QSize(40, 40))
        self.frame_5.setStyleSheet(u"background-color: rgb(85, 0, 255);\n"
"border-radius: 20;\n"
"image: url(:/icons/icons/discord.svg);\n"
"padding: 3px;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignVCenter)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(200, 0))
        self.frame_9.setMaximumSize(QSize(200, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(168, 168, 168);")

        self.verticalLayout_8.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(134, 134, 134);")

        self.verticalLayout_8.addWidget(self.label_5)


        self.horizontalLayout_4.addWidget(self.frame_9, 0, Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(134, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_7 = QFrame(self.actionBar)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 0))
        self.frame_7.setMaximumSize(QSize(250, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(255, 115, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(255, 115, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(255, 115, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.actionItems = QFrame(self.actionBar)
        self.actionItems.setObjectName(u"actionItems")
        self.actionItems.setMinimumSize(QSize(120, 0))
        self.actionItems.setMaximumSize(QSize(120, 16777215))
        self.actionItems.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.actionItems.setFrameShape(QFrame.NoFrame)
        self.actionItems.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.actionItems)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.actionItems)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(36, 36))
        self.pushButton.setMaximumSize(QSize(36, 36))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/chart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_2 = QPushButton(self.actionItems)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(36, 36))
        self.pushButton_2.setMaximumSize(QSize(36, 36))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_3 = QPushButton(self.actionItems)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(36, 36))
        self.pushButton_3.setMaximumSize(QSize(36, 36))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.actionItems)


        self.verticalLayout_5.addWidget(self.actionBar)


        self.verticalLayout.addWidget(self.topBar)

        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"background-color: rgb(8, 8, 8);")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.frame = QFrame(self.container)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spendingFrame = QFrame(self.frame)
        self.spendingFrame.setObjectName(u"spendingFrame")
        self.spendingFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}\n"
"")
        self.spendingFrame.setFrameShape(QFrame.NoFrame)
        self.spendingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.spendingFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.monthly = QFrame(self.spendingFrame)
        self.monthly.setObjectName(u"monthly")
        self.monthly.setMinimumSize(QSize(0, 40))
        self.monthly.setMaximumSize(QSize(16777215, 30))
        self.monthly.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.monthly.setFrameShape(QFrame.NoFrame)
        self.monthly.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.monthly)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 3)
        self.label_6 = QLabel(self.monthly)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 0))
        self.label_6.setMaximumSize(QSize(150, 16777215))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.pushButton_7 = QPushButton(self.monthly)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(26, 26))
        self.pushButton_7.setMaximumSize(QSize(26, 26))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/wink.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.pushButton_7)


        self.verticalLayout_6.addWidget(self.monthly)

        self.frame_10 = QFrame(self.spendingFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 250))
        self.frame_10.setMaximumSize(QSize(16777215, 250))
        self.frame_10.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_33 = QFrame(self.frame_16)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(30, 10, 200, 200))
        self.frame_33.setMinimumSize(QSize(200, 200))
        self.frame_33.setMaximumSize(QSize(200, 200))
        self.frame_33.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 0, 255, 255), stop:0.0340909 rgba(255, 85, 0, 255), stop:0.295455 rgba(255, 85, 0, 255), stop:0.323864 rgba(255, 17, 80, 255), stop:0.625 rgba(255, 17, 80, 255), stop:0.670455 rgba(85, 0, 255, 255));\n"
"border: none;\n"
"border-radius: 100px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(180, 180))
        self.frame_34.setMaximumSize(QSize(180, 180))
        self.frame_34.setStyleSheet(u"background-color: rgb(13, 9, 36);\n"
"border-radius: 90px;")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_32 = QFrame(self.frame_34)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 80))
        self.frame_32.setMaximumSize(QSize(16777215, 80))
        self.frame_32.setStyleSheet(u"border: none;")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_32)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_32)
        self.label_18.setObjectName(u"label_18")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_15.addWidget(self.label_18, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_19 = QLabel(self.frame_32)
        self.label_19.setObjectName(u"label_19")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.verticalLayout_15.addWidget(self.label_19, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_20 = QLabel(self.frame_32)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_15.addWidget(self.label_20, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_21.addWidget(self.frame_32)


        self.horizontalLayout_20.addWidget(self.frame_34)


        self.horizontalLayout_17.addWidget(self.frame_16)


        self.horizontalLayout_5.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(150, 16777215))
        self.frame_13.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_13)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(20, 20))
        self.frame_20.setMaximumSize(QSize(20, 20))
        self.frame_20.setStyleSheet(u"QFrame {\n"
"	border: 4px solid  rgb(85, 0, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 10;\n"
"}")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 50))
        self.frame_21.setMaximumSize(QSize(16777215, 50))
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_21)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.frame_21)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(159, 159, 159);")

        self.verticalLayout_10.addWidget(self.label_7, 0, Qt.AlignVCenter)

        self.label_8 = QLabel(self.frame_21)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(85, 0, 255);")

        self.verticalLayout_10.addWidget(self.label_8, 0, Qt.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.frame_21)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.frame_13)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_8)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(20, 20))
        self.frame_22.setMaximumSize(QSize(20, 20))
        self.frame_22.setStyleSheet(u"QFrame {\n"
"	border: 4px solid rgb(255, 17, 80);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 10;\n"
"}")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_8)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 50))
        self.frame_23.setMaximumSize(QSize(16777215, 50))
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_23)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.frame_23)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(159, 159, 159);")

        self.verticalLayout_11.addWidget(self.label_9, 0, Qt.AlignVCenter)

        self.label_10 = QLabel(self.frame_23)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(85, 0, 255);")

        self.verticalLayout_11.addWidget(self.label_10, 0, Qt.AlignVCenter)


        self.horizontalLayout_11.addWidget(self.frame_23)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_12)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(20, 20))
        self.frame_24.setMaximumSize(QSize(20, 20))
        self.frame_24.setStyleSheet(u"QFrame {\n"
"	border: 4px solid rgb(255, 136, 0);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 10;\n"
"}")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_12)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 50))
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_25)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_11 = QLabel(self.frame_25)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(159, 159, 159);")

        self.verticalLayout_12.addWidget(self.label_11, 0, Qt.AlignVCenter)

        self.label_12 = QLabel(self.frame_25)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(85, 0, 255);")

        self.verticalLayout_12.addWidget(self.label_12, 0, Qt.AlignVCenter)


        self.horizontalLayout_12.addWidget(self.frame_25)


        self.verticalLayout_9.addWidget(self.frame_12)


        self.horizontalLayout_5.addWidget(self.frame_13)


        self.verticalLayout_6.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.spendingFrame)

        self.subSpendBox = QFrame(self.frame)
        self.subSpendBox.setObjectName(u"subSpendBox")
        self.subSpendBox.setMinimumSize(QSize(0, 0))
        self.subSpendBox.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.subSpendBox.setFrameShape(QFrame.NoFrame)
        self.subSpendBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.subSpendBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.subSpendBox)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 30))
        self.frame_14.setMaximumSize(QSize(16777215, 30))
        self.frame_14.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 10, 0)
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))
        self.label_13.setMaximumSize(QSize(150, 16777215))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.horizontalLayout_13.addWidget(self.label_13, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_8 = QPushButton(self.frame_14)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(26, 26))
        self.pushButton_8.setMaximumSize(QSize(26, 26))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/more.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.pushButton_8, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.subSpendBox)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_15)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 5, 5)
        self.frame_35 = QFrame(self.frame_15)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border: 1px solid rgb(34, 24, 97);")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(5, 0, 5, 0)
        self.frame_30 = QFrame(self.frame_35)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(120, 120))
        self.frame_30.setMaximumSize(QSize(120, 120))
        self.frame_30.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.867 rgba(7, 255, 119, 1), stop:0.869 rgba(29, 21, 83, 1));\n"
"border: 1px solid rgb(33, 24, 94);\n"
"border-radius: 60;")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(100, 100))
        self.frame_31.setMaximumSize(QSize(130, 130))
        self.frame_31.setStyleSheet(u"background-color: rgb(13, 9, 36);\n"
"border: 1px solid rgb(33, 24, 94);\n"
"border-radius: 50px;")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_36 = QFrame(self.frame_31)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(50, 50))
        self.frame_36.setMaximumSize(QSize(50, 50))
        self.frame_36.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	image: url(:/icons/icons/money-hand.svg);\n"
"	border-radius: 25;\n"
"}")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_36)


        self.horizontalLayout_18.addWidget(self.frame_31, 0, Qt.AlignHCenter)


        self.horizontalLayout_19.addWidget(self.frame_30, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(110, 0))
        self.frame_37.setMaximumSize(QSize(110, 16777215))
        self.frame_37.setStyleSheet(u"border: none;")
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_37)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_22 = QLabel(self.frame_37)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"color: rgb(7, 255, 119);")

        self.verticalLayout_16.addWidget(self.label_22, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_21 = QLabel(self.frame_37)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_16.addWidget(self.label_21, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_19.addWidget(self.frame_37, 0, Qt.AlignVCenter)


        self.gridLayout.addWidget(self.frame_35, 0, 0, 1, 1)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_18)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"border: 1px solid rgb(34, 24, 97);")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_42 = QFrame(self.frame_38)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(120, 120))
        self.frame_42.setMaximumSize(QSize(120, 120))
        self.frame_42.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.867 rgba(7, 255, 119, 1), stop:0.869 rgba(29, 21, 83, 1));\n"
"border: 1px solid rgb(33, 24, 94);\n"
"border-radius: 60;")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(100, 100))
        self.frame_43.setMaximumSize(QSize(130, 130))
        self.frame_43.setStyleSheet(u"background-color: rgb(13, 9, 36);\n"
"border: 1px solid rgb(33, 24, 94);\n"
"border-radius: 50px;")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(50, 50))
        self.frame_44.setMaximumSize(QSize(50, 50))
        self.frame_44.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	\n"
"	image: url(:/icons/icons/euro_money.svg);\n"
"	border-radius: 25;\n"
"}")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_31.addWidget(self.frame_44)


        self.horizontalLayout_23.addWidget(self.frame_43, 0, Qt.AlignHCenter)


        self.horizontalLayout_24.addWidget(self.frame_42)

        self.frame_41 = QFrame(self.frame_38)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(110, 0))
        self.frame_41.setMaximumSize(QSize(110, 16777215))
        self.frame_41.setStyleSheet(u"border: none;")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_41)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_23 = QLabel(self.frame_41)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font4)
        self.label_23.setStyleSheet(u"color: rgb(7, 255, 119);")

        self.verticalLayout_17.addWidget(self.label_23, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_24 = QLabel(self.frame_41)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_17.addWidget(self.label_24, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_24.addWidget(self.frame_41, 0, Qt.AlignVCenter)


        self.horizontalLayout_25.addWidget(self.frame_38)


        self.gridLayout.addWidget(self.frame_18, 0, 1, 1, 1)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_17)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"border: 1px solid rgb(34, 24, 97);")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 5, 0)
        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(120, 120))
        self.frame_46.setMaximumSize(QSize(120, 120))
        self.frame_46.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.267 rgba(7, 255, 119, 1), stop:0.269 rgba(29, 21, 83, 1));\n"
"border: 1px solid rgb(33, 24, 94);\n"
"border-radius: 60;")
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(100, 100))
        self.frame_47.setMaximumSize(QSize(100, 100))
        self.frame_47.setStyleSheet(u"background-color: rgb(13, 9, 36);\n"
"border: 1px solid rgb(33, 24, 94);\n"
"border-radius: 50px;")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(50, 50))
        self.frame_48.setMaximumSize(QSize(50, 50))
        self.frame_48.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	image: url(:/icons/icons/account.svg);\n"
"	border-radius: 25;\n"
"}")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_29.addWidget(self.frame_48)


        self.horizontalLayout_27.addWidget(self.frame_47, 0, Qt.AlignHCenter)


        self.horizontalLayout_26.addWidget(self.frame_46, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_49 = QFrame(self.frame_45)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(110, 0))
        self.frame_49.setMaximumSize(QSize(110, 16777215))
        self.frame_49.setStyleSheet(u"border: none;")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_49)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_25 = QLabel(self.frame_49)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"color: rgb(7, 255, 119);")

        self.verticalLayout_18.addWidget(self.label_25, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_26 = QLabel(self.frame_49)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_18.addWidget(self.label_26, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_26.addWidget(self.frame_49, 0, Qt.AlignVCenter)


        self.horizontalLayout_28.addWidget(self.frame_45)


        self.gridLayout.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"border: 1px solid rgb(34, 24, 97);")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 10, 0, 20)
        self.pushButton_9 = QPushButton(self.frame_19)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 50))
        self.pushButton_9.setMaximumSize(QSize(100, 50))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"color: rgb(130, 130, 130);\n"
"border: none;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"background-color: rgb(13, 9, 36);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(25, 25))

        self.verticalLayout_19.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_19)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 0))
        self.pushButton_10.setMaximumSize(QSize(22222, 22222))
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(u"color: rgb(130, 130, 130);\n"
"border: none;\n"
"text-align: center;\n"
"padding-left: 10px;\n"
"background-color: rgb(13, 9, 36);")
        self.pushButton_10.setIcon(icon8)
        self.pushButton_10.setIconSize(QSize(40, 40))

        self.verticalLayout_19.addWidget(self.pushButton_10)


        self.gridLayout.addWidget(self.frame_19, 1, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.subSpendBox)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.incomeBox = QFrame(self.frame_2)
        self.incomeBox.setObjectName(u"incomeBox")
        self.incomeBox.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.incomeBox.setFrameShape(QFrame.NoFrame)
        self.incomeBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.incomeBox)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.incomeBox)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 30))
        self.frame_26.setMaximumSize(QSize(16777215, 30))
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 10, 0)
        self.label_14 = QLabel(self.frame_26)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(180, 0))
        self.label_14.setMaximumSize(QSize(150, 16777215))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.horizontalLayout_14.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_13.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.incomeBox)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_27.setFrameShape(QFrame.Panel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_28)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 20, 10, 20)
        self.label_17 = QLabel(self.frame_28)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(70, 16))
        font5 = QFont()
        font5.setBold(True)
        self.label_17.setFont(font5)
        self.label_17.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.verticalLayout_14.addWidget(self.label_17, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.progressBar = QProgressBar(self.frame_28)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 16))
        self.progressBar.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setBold(False)
        self.progressBar.setFont(font6)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	color: rgb(177, 177, 177);\n"
"	border: none;\n"
"	background-color: rgb(102, 102, 102);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(7, 255, 119);\n"
"	border-radius : 8px;\n"
"}     ")
        self.progressBar.setValue(75)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_14.addWidget(self.progressBar, 0, Qt.AlignVCenter)

        self.label_16 = QLabel(self.frame_28)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(70, 16))
        self.label_16.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.verticalLayout_14.addWidget(self.label_16, 0, Qt.AlignVCenter)

        self.progressBar_2 = QProgressBar(self.frame_28)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMinimumSize(QSize(0, 16))
        self.progressBar_2.setMaximumSize(QSize(16777215, 16))
        self.progressBar_2.setStyleSheet(u"QProgressBar {\n"
"	color: rgb(177, 177, 177);\n"
"	border: none;\n"
"	background-color: rgb(102, 102, 102);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(85, 0, 255);\n"
"	border-radius : 8px;\n"
"}     ")
        self.progressBar_2.setValue(25)
        self.progressBar_2.setAlignment(Qt.AlignCenter)
        self.progressBar_2.setTextVisible(False)

        self.verticalLayout_14.addWidget(self.progressBar_2, 0, Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(140, 0))
        self.frame_29.setMaximumSize(QSize(140, 16777215))
        self.frame_29.setStyleSheet(u"")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_29)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_29)
        self.label_15.setObjectName(u"label_15")
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        self.label_15.setFont(font7)
        self.label_15.setStyleSheet(u"color: rgb(159, 159, 159);")

        self.verticalLayout_20.addWidget(self.label_15, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_27 = QLabel(self.frame_29)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 0))
        self.label_27.setMaximumSize(QSize(120, 16777215))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.verticalLayout_20.addWidget(self.label_27, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.frame_29)


        self.verticalLayout_13.addWidget(self.frame_27)


        self.verticalLayout_3.addWidget(self.incomeBox)

        self.billsBox = QFrame(self.frame_2)
        self.billsBox.setObjectName(u"billsBox")
        self.billsBox.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.billsBox.setFrameShape(QFrame.NoFrame)
        self.billsBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.billsBox)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.billsBox)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 40))
        self.frame_54.setMaximumSize(QSize(16777215, 40))
        self.frame_54.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 10, 0)
        self.label_32 = QLabel(self.frame_54)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 0))
        self.label_32.setMaximumSize(QSize(16777215, 16777215))
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.horizontalLayout_34.addWidget(self.label_32, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_12 = QPushButton(self.frame_54)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(26, 26))
        self.pushButton_12.setMaximumSize(QSize(26, 26))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_12.setIcon(icon7)
        self.pushButton_12.setIconSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.pushButton_12, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.billsBox)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_55)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_33 = QLabel(self.frame_55)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(200, 0))
        self.label_33.setMaximumSize(QSize(150, 16777215))
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.verticalLayout_24.addWidget(self.label_33, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_34 = QLabel(self.frame_56)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 20))
        self.label_34.setMaximumSize(QSize(70, 20))
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"color: rgb(203, 203, 203);\n"
"background-color: rgb(255, 17, 80);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.horizontalLayout_35.addWidget(self.label_34)

        self.label_37 = QLabel(self.frame_56)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(50, 0))
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.horizontalLayout_35.addWidget(self.label_37)

        self.horizontalSpacer_4 = QSpacerItem(136, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_4)

        self.label_36 = QLabel(self.frame_56)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(50, 0))
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.horizontalLayout_35.addWidget(self.label_36)

        self.label_35 = QLabel(self.frame_56)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 20))
        self.label_35.setMaximumSize(QSize(100, 20))
        self.label_35.setFont(font5)
        self.label_35.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"background-color: rgb(85, 0, 255);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.horizontalLayout_35.addWidget(self.label_35)


        self.verticalLayout_24.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_55)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_38 = QLabel(self.frame_57)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 20))
        self.label_38.setMaximumSize(QSize(70, 20))
        self.label_38.setFont(font5)
        self.label_38.setStyleSheet(u"color: rgb(203, 203, 203);\n"
"background-color: rgb(0, 0, 0);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.horizontalLayout_36.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_57)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(50, 0))
        self.label_39.setFont(font)
        self.label_39.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.horizontalLayout_36.addWidget(self.label_39)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_5)

        self.label_40 = QLabel(self.frame_57)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(50, 0))
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.horizontalLayout_36.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_57)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 20))
        self.label_41.setMaximumSize(QSize(100, 20))
        self.label_41.setFont(font5)
        self.label_41.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"background-color: rgb(85, 0, 255);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.horizontalLayout_36.addWidget(self.label_41)


        self.verticalLayout_24.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_55)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_42 = QLabel(self.frame_58)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 20))
        self.label_42.setMaximumSize(QSize(70, 20))
        self.label_42.setFont(font5)
        self.label_42.setStyleSheet(u"color: rgb(203, 203, 203);\n"
"background-color: rgb(0, 0, 0);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.horizontalLayout_37.addWidget(self.label_42)

        self.label_43 = QLabel(self.frame_58)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(50, 0))
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.horizontalLayout_37.addWidget(self.label_43)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_6)

        self.label_44 = QLabel(self.frame_58)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(50, 0))
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.horizontalLayout_37.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_58)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 20))
        self.label_45.setMaximumSize(QSize(100, 20))
        self.label_45.setFont(font5)
        self.label_45.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"background-color: rgb(85, 0, 255);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.horizontalLayout_37.addWidget(self.label_45)


        self.verticalLayout_24.addWidget(self.frame_58)


        self.verticalLayout_23.addWidget(self.frame_55)


        self.verticalLayout_3.addWidget(self.billsBox)

        self.savingsBox = QFrame(self.frame_2)
        self.savingsBox.setObjectName(u"savingsBox")
        self.savingsBox.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.savingsBox.setFrameShape(QFrame.NoFrame)
        self.savingsBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.savingsBox)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_39 = QFrame(self.savingsBox)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_51 = QFrame(self.frame_39)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(120, 120))
        self.frame_51.setMaximumSize(QSize(120, 120))
        self.frame_51.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.267 rgba(29, 21, 83, 1), stop:0.269 rgba(255, 17, 80, 1));\n"
"border: 1px solid rgb(13, 9, 36);\n"
"border-radius: 60;")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(100, 100))
        self.frame_52.setMaximumSize(QSize(100, 100))
        self.frame_52.setStyleSheet(u"background-color: rgb(13, 9, 36);\n"
"border: 1px solid rgb(33, 24, 94);\n"
"border-radius: 50px;")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(50, 50))
        self.frame_53.setMaximumSize(QSize(50, 50))
        self.frame_53.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	image: url(:/icons/icons/euro_money.svg);\n"
"	border-radius: 25;\n"
"}")
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_53)


        self.horizontalLayout_32.addWidget(self.frame_52, 0, Qt.AlignHCenter)


        self.horizontalLayout_16.addWidget(self.frame_51)

        self.frame_50 = QFrame(self.frame_39)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_50)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(30, 20, 10, 20)
        self.label_28 = QLabel(self.frame_50)
        self.label_28.setObjectName(u"label_28")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        self.label_28.setFont(font8)
        self.label_28.setStyleSheet(u"color: rgb(182, 182, 182);")

        self.verticalLayout_22.addWidget(self.label_28)

        self.label_31 = QLabel(self.frame_50)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color: rgb(182, 182, 182);")

        self.verticalLayout_22.addWidget(self.label_31, 0, Qt.AlignVCenter)

        self.label_29 = QLabel(self.frame_50)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font7)
        self.label_29.setStyleSheet(u"color: rgb(159, 159, 159);")

        self.verticalLayout_22.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_50)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"color: rgb(159, 159, 159);")

        self.verticalLayout_22.addWidget(self.label_30)


        self.horizontalLayout_16.addWidget(self.frame_50)


        self.verticalLayout_21.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.savingsBox)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 50))
        self.frame_40.setMaximumSize(QSize(16777215, 50))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_40)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 50))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(u"border: 3px solid rgb(85, 0, 255);\n"
"border-radius: 25;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"color: rgb(194, 194, 194);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/smile.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon9)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.pushButton_11)


        self.verticalLayout_21.addWidget(self.frame_40)


        self.verticalLayout_3.addWidget(self.savingsBox)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.calenderBox = QFrame(self.frame_3)
        self.calenderBox.setObjectName(u"calenderBox")
        self.calenderBox.setMinimumSize(QSize(0, 300))
        self.calenderBox.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.calenderBox.setFrameShape(QFrame.NoFrame)
        self.calenderBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.calenderBox)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 0, 5, 0)
        self.frame_61 = QFrame(self.calenderBox)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 30))
        self.frame_61.setMaximumSize(QSize(16777215, 30))
        self.frame_61.setStyleSheet(u"")
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 10, 0)
        self.label_46 = QLabel(self.frame_61)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(180, 0))
        self.label_46.setMaximumSize(QSize(150, 16777215))
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.horizontalLayout_38.addWidget(self.label_46, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_25.addWidget(self.frame_61)

        self.label_47 = QLabel(self.calenderBox)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(180, 0))
        self.label_47.setMaximumSize(QSize(150, 30))
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(u"color: rgb(170, 170, 170);")

        self.verticalLayout_25.addWidget(self.label_47)

        self.frame_59 = QFrame(self.calenderBox)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"border-image: url(:/icons/chart2.jpg);\n"
"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.calenderBox)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(16777215, 60))
        self.frame_60.setStyleSheet(u"")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_60)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(30, 0, 30, 0)
        self.label_48 = QLabel(self.frame_60)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font7)
        self.label_48.setStyleSheet(u"color: rgb(182, 182, 182);")

        self.gridLayout_2.addWidget(self.label_48, 0, 0, 1, 1)

        self.label_49 = QLabel(self.frame_60)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 20))
        self.label_49.setMaximumSize(QSize(60, 20))
        self.label_49.setFont(font5)
        self.label_49.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"background-color: rgb(85, 0, 255);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.gridLayout_2.addWidget(self.label_49, 0, 1, 1, 1)

        self.label_51 = QLabel(self.frame_60)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(50, 0))
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.gridLayout_2.addWidget(self.label_51, 1, 0, 1, 1)

        self.label_50 = QLabel(self.frame_60)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(0, 20))
        self.label_50.setMaximumSize(QSize(60, 20))
        self.label_50.setFont(font5)
        self.label_50.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"background-color: rgb(255, 17, 80);\n"
"padding: 1px;\n"
"border-radius: 8px;")

        self.gridLayout_2.addWidget(self.label_50, 1, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.frame_60)


        self.verticalLayout_4.addWidget(self.calenderBox)

        self.investBox = QFrame(self.frame_3)
        self.investBox.setObjectName(u"investBox")
        self.investBox.setMaximumSize(QSize(16777215, 150))
        self.investBox.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.investBox.setFrameShape(QFrame.NoFrame)
        self.investBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.investBox)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_52 = QLabel(self.investBox)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(60, 60))
        self.label_52.setMaximumSize(QSize(60, 60))
        font9 = QFont()
        font9.setPointSize(20)
        font9.setBold(True)
        self.label_52.setFont(font9)
        self.label_52.setStyleSheet(u"color: rgb(206, 206, 206);")

        self.horizontalLayout_39.addWidget(self.label_52)

        self.frame_63 = QFrame(self.investBox)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_63)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 20, 0, 20)
        self.label_53 = QLabel(self.frame_63)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font7)
        self.label_53.setStyleSheet(u"color: rgb(182, 182, 182);")

        self.verticalLayout_27.addWidget(self.label_53, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_54 = QLabel(self.frame_63)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(0, 0))
        self.label_54.setFont(font)
        self.label_54.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_27.addWidget(self.label_54, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_55 = QLabel(self.frame_63)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(0, 0))
        self.label_55.setFont(font)
        self.label_55.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_27.addWidget(self.label_55, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_39.addWidget(self.frame_63)

        self.frame_62 = QFrame(self.investBox)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMaximumSize(QSize(50, 16777215))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_62)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.frame_62)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(26, 26))
        self.pushButton_14.setMaximumSize(QSize(26, 26))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.pushButton_14, 0, Qt.AlignTop)

        self.pushButton_13 = QPushButton(self.frame_62)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(26, 26))
        self.pushButton_13.setMaximumSize(QSize(26, 26))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/black-shades.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon10)
        self.pushButton_13.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.pushButton_13, 0, Qt.AlignBottom)


        self.horizontalLayout_39.addWidget(self.frame_62)


        self.verticalLayout_4.addWidget(self.investBox)

        self.loadnsBox = QFrame(self.frame_3)
        self.loadnsBox.setObjectName(u"loadnsBox")
        self.loadnsBox.setMaximumSize(QSize(16777215, 150))
        self.loadnsBox.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.loadnsBox.setFrameShape(QFrame.NoFrame)
        self.loadnsBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.loadnsBox)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_59 = QLabel(self.loadnsBox)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(90, 60))
        self.label_59.setMaximumSize(QSize(60, 60))
        self.label_59.setFont(font9)
        self.label_59.setStyleSheet(u"color: rgb(206, 206, 206);")

        self.horizontalLayout_40.addWidget(self.label_59)

        self.frame_64 = QFrame(self.loadnsBox)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_64)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 20, 0, 20)
        self.label_56 = QLabel(self.frame_64)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font7)
        self.label_56.setStyleSheet(u"color: rgb(182, 182, 182);")

        self.verticalLayout_28.addWidget(self.label_56, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_57 = QLabel(self.frame_64)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 0))
        self.label_57.setFont(font)
        self.label_57.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_28.addWidget(self.label_57, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_58 = QLabel(self.frame_64)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(0, 0))
        self.label_58.setFont(font)
        self.label_58.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_28.addWidget(self.label_58, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_40.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.loadnsBox)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMaximumSize(QSize(50, 16777215))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_65)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.frame_65)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(26, 26))
        self.pushButton_15.setMaximumSize(QSize(26, 26))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.pushButton_15, 0, Qt.AlignTop)

        self.pushButton_16 = QPushButton(self.frame_65)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(26, 26))
        self.pushButton_16.setMaximumSize(QSize(26, 26))
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/cry.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_16.setIcon(icon11)
        self.pushButton_16.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.pushButton_16, 0, Qt.AlignBottom)


        self.horizontalLayout_40.addWidget(self.frame_65)


        self.verticalLayout_4.addWidget(self.loadnsBox)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.container)

        self.bottomBar = QFrame(self.centralwidget)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 40))
        self.bottomBar.setMaximumSize(QSize(16777215, 40))
        self.bottomBar.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.pushButton_17 = QPushButton(self.bottomBar)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(100, 26))
        self.pushButton_17.setMaximumSize(QSize(26, 26))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_17.setIcon(icon12)
        self.pushButton_17.setIconSize(QSize(20, 20))

        self.horizontalLayout_41.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.bottomBar)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(100, 26))
        self.pushButton_18.setMaximumSize(QSize(26, 26))
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_18.setIcon(icon3)
        self.pushButton_18.setIconSize(QSize(20, 20))

        self.horizontalLayout_41.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.bottomBar)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(100, 26))
        self.pushButton_19.setMaximumSize(QSize(26, 26))
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/pouch.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_19.setIcon(icon13)
        self.pushButton_19.setIconSize(QSize(20, 20))

        self.horizontalLayout_41.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.bottomBar)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(100, 26))
        self.pushButton_20.setMaximumSize(QSize(26, 26))
        self.pushButton_20.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/account.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_20.setIcon(icon14)
        self.pushButton_20.setIconSize(QSize(20, 20))

        self.horizontalLayout_41.addWidget(self.pushButton_20)


        self.verticalLayout.addWidget(self.bottomBar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Welcome to Chairman Studios.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"We are made for this. @Python.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Insight", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Treads", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"My Monthly Spendings", None))
        self.pushButton_7.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Budget Report", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"$ 5, 200.00", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Sep 2021", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Food", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"$ 250.00", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Food", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"$ 250.00", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Food", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"$ 250.00", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Improving Financial Habit", None))
        self.pushButton_8.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"$ 5, 200.00", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Sep 2021", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"$ 5, 200.00", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Sep 2021", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"$ 5, 200.00", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Sep 2021", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.pushButton_10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Improving Financial Habit", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u" Savings", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"  SPendings", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"$ 25, 500.00", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u2714Spending Rate", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Upcoming Bills", None))
        self.pushButton_12.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#828282;\">Total Due in 30 Days</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Sep 12", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Water", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"$ 250.00", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Pedding", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Sep 22", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Gas", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"$ 320.00", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Pedding", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Sep 18", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Rent", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"$ 3000.00", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Pedding", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Saved for Goals", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5500ff;\">Moved to Bank</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff1150;\">$ 2,500.00</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff1150;\">$ 3900.00</span></p></body></html>", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"SAVE MORE WITH CHAIRMAN STUDIOS.", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"My CashFLow for September", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"LEADINGs", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#b9b9b9;\">$150, 570. 00</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Pedding", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00aa00;\">+23%</span> Since first week</p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Pedding", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"$50", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#b9b9b9;\">Invest in my Future</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Chairman Studios", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Invested since your last login", None))
        self.pushButton_14.setText("")
        self.pushButton_13.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"$100k", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#b9b9b9;\">Paying off Loans</span></p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Chairman Studios", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Paid towards car loan and house mortgae", None))
        self.pushButton_15.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Earnings", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Account", None))
    # retranslateUi


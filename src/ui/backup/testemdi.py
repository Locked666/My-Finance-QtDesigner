# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testemdi.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMdiArea, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(951, 732)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(120, 0))
        self.frame.setMaximumSize(QSize(120, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.subwindow = QWidget()
        self.subwindow.setObjectName(u"subwindow")
        self.label = QLabel(self.subwindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 170, 47, 13))
        self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow_2 = QWidget()
        self.subwindow_2.setObjectName(u"subwindow_2")
        self.label_2 = QLabel(self.subwindow_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 190, 47, 13))
        self.mdiArea.addSubWindow(self.subwindow_2)
        self.subwindow_3 = QWidget()
        self.subwindow_3.setObjectName(u"subwindow_3")
        self.label_3 = QLabel(self.subwindow_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 190, 47, 13))
        self.mdiArea.addSubWindow(self.subwindow_3)
        self.subwindow_4 = QWidget()
        self.subwindow_4.setObjectName(u"subwindow_4")
        self.label_4 = QLabel(self.subwindow_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 230, 47, 13))
        self.mdiArea.addSubWindow(self.subwindow_4)

        self.horizontalLayout.addWidget(self.mdiArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.subwindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Subwindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"window 1 ", None))
        self.subwindow_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"Subwindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"window 2", None))
        self.subwindow_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"Subwindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"window 3 ", None))
        self.subwindow_4.setWindowTitle(QCoreApplication.translate("MainWindow", u"Subwindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"window 4", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmGraficFinc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(761, 594)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 761, 171))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(80, 20, 191, 131))
        self.frame_2.setStyleSheet(u"border-radius: 20px ;\n"
"border: 1px solid blue;\n"
"background-color: rgb(0, 145, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 151, 41))
        self.label.setStyleSheet(u"font: 87 20pt \"Segoe UI Black\";\n"
"color: white;\n"
"border: none;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 141, 41))
        self.label_2.setSizeIncrement(QSize(10, 10))
        self.label_2.setBaseSize(QSize(10, 10))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"font: 87 20pt \"Segoe UI Black\";\n"
"color: white;\n"
"border: none;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 90, 81, 21))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border:none;\n"
"color: white; \n"
"font: 12pt \"Segoe UI\";")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(280, 20, 191, 131))
        self.frame_3.setStyleSheet(u"border-radius: 20px ;\n"
"border: 1px solid blue;\n"
"background-color: rgb(255, 102, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 151, 41))
        self.label_5.setStyleSheet(u"font: 87 20pt \"Segoe UI Black\";\n"
"color: white;\n"
"border: none;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 50, 141, 41))
        self.label_6.setSizeIncrement(QSize(10, 10))
        self.label_6.setBaseSize(QSize(10, 10))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"font: 87 20pt \"Segoe UI Black\";\n"
"color: white;\n"
"border: none;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 90, 81, 21))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border:none;\n"
"color: white; \n"
"font: 12pt \"Segoe UI\";")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(480, 20, 191, 131))
        self.frame_4.setStyleSheet(u"border-radius: 20px ;\n"
"border: 1px solid blue;\n"
"background-color: rgb(0, 158, 0);\n"
"alternate-background-color: rgb(225, 0, 0);\n"
"alternate-background-color: rgb(0, 158, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 151, 41))
        self.label_7.setStyleSheet(u"font: 87 20pt \"Segoe UI Black\";\n"
"color: white;\n"
"border: none;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 50, 141, 41))
        self.label_8.setSizeIncrement(QSize(10, 10))
        self.label_8.setBaseSize(QSize(10, 10))
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet(u"font: 87 20pt \"Segoe UI Black\";\n"
"color: white;\n"
"border: none;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 90, 81, 21))
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"border:none;\n"
"color: white; \n"
"font: 12pt \"Segoe UI\";")
        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 170, 761, 421))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top: 1px solid black;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Receita", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Visualizar", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Despesa", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Visualizar", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Diff.", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Visualizar", None))
    # retranslateUi


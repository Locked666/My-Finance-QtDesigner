# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainLogin.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_Ui_Login(object):
    def setupUi(self, Ui_Login):
        if not Ui_Login.objectName():
            Ui_Login.setObjectName(u"Ui_Login")
        Ui_Login.resize(350, 448)
        Ui_Login.setMinimumSize(QSize(350, 448))
        Ui_Login.setMaximumSize(QSize(350, 448))
        Ui_Login.setAutoFillBackground(False)
        Ui_Login.setStyleSheet(u" border-top: none;")
        self.centralwidget = QWidget(Ui_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"alternate-background-color: rgb(28, 28, 28);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 350, 448))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 180, 331, 20))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"border: 1px solid #2980b9; /* Borda ao redor do frame */\n"
"selection-background-color: rgb(28, 28, 28);\n"
"border-radius: 0px; /* Arredondamento se desejar */;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"background-color: rgb(28, 28, 28);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 260, 331, 20))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"border: 1px solid #2980b9; /* Borda ao redor do frame */\n"
"selection-background-color: rgb(28, 28, 28);\n"
"border-radius: 0px; /* Arredondamento se desejar */;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"background-color: rgb(28, 28, 28);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 150, 71, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 230, 71, 16))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 300, 221, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setToolTipDuration(3)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px;\n"
"\n"
"selection-background-color: rgb(0, 0, 212);")
        self.pushButton.setAutoDefault(False)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 350, 201, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"/*\n"
"border: 1px solid #2980b9;\n"
"border-radius: 10px;\n"
"border-top:  none;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-bottom: 2px;\n"
"*/\n"
"\n"
"border: 1px solid #2980b9; /* Borda ao redor do frame */\n"
"selection-background-color: rgb(28, 28, 28);\n"
"border-radius: 0px; /* Arredondamento se desejar */;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        Ui_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_Login)

        QMetaObject.connectSlotsByName(Ui_Login)
    # setupUi

    def retranslateUi(self, Ui_Login):
        Ui_Login.setWindowTitle(QCoreApplication.translate("Ui_Login", u"MainWindow", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label.setText(QCoreApplication.translate("Ui_Login", u"Usu\u00e1rio:", None))
        self.label_2.setText(QCoreApplication.translate("Ui_Login", u"Senha:", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Ui_Login", u"<html><head/><body><p>Acessar o sistema.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Ui_Login", u"Entrar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Ui_Login", u"Esqueci senha", None))
    # retranslateUi


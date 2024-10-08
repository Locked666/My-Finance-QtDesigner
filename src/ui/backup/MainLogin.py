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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 448)
        self.Mainframe = QFrame(Dialog)
        self.Mainframe.setObjectName(u"Mainframe")
        self.Mainframe.setGeometry(QRect(0, 0, 350, 448))
        self.Mainframe.setAutoFillBackground(False)
        self.Mainframe.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"")
        self.Mainframe.setFrameShape(QFrame.NoFrame)
        self.Mainframe.setFrameShadow(QFrame.Raised)
        self.text_usuario = QLineEdit(self.Mainframe)
        self.text_usuario.setObjectName(u"text_usuario")
        self.text_usuario.setGeometry(QRect(10, 180, 331, 20))
        font = QFont()
        font.setPointSize(10)
        self.text_usuario.setFont(font)
        self.text_usuario.setStyleSheet(u"border: 1px solid #2980b9; /* Borda ao redor do frame */\n"
"selection-background-color: rgb(28, 28, 28);\n"
"border-radius: 0px; /* Arredondamento se desejar */;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"background-color: rgb(28, 28, 28);\n"
"color: rgb(255, 255, 255);")
        self.text_password = QLineEdit(self.Mainframe)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setGeometry(QRect(10, 260, 331, 19))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_password.sizePolicy().hasHeightForWidth())
        self.text_password.setSizePolicy(sizePolicy)
        self.text_password.setFont(font)
        self.text_password.setStyleSheet(u"border: 1px solid #2980b9; /* Borda ao redor do frame */\n"
"selection-background-color: rgb(28, 28, 28);\n"
"border-radius: 0px; /* Arredondamento se desejar */;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"background-color: rgb(28, 28, 28);\n"
"color: rgb(255, 255, 255);")
        self.text_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.text_password.setEchoMode(QLineEdit.Password)
        self.label_user = QLabel(self.Mainframe)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(10, 150, 71, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_user.setFont(font1)
        self.label_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_password = QLabel(self.Mainframe)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(10, 230, 71, 16))
        self.label_password.setFont(font1)
        self.label_password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bnt_entrar = QPushButton(self.Mainframe)
        self.bnt_entrar.setObjectName(u"bnt_entrar")
        self.bnt_entrar.setGeometry(QRect(60, 300, 221, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.bnt_entrar.setFont(font2)
        self.bnt_entrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bnt_entrar.setToolTipDuration(3)
        self.bnt_entrar.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px;\n"
"hover{\n"
"background-color: rgb(0, 0, 115);\n"
"};\n"
"selection-color: rgb(0, 0, 126);a")
        self.bnt_entrar.setCheckable(False)
        self.bnt_entrar.setChecked(False)
        self.bnt_entrar.setAutoDefault(False)
        self.bnt_reset_password = QPushButton(self.Mainframe)
        self.bnt_reset_password.setObjectName(u"bnt_reset_password")
        self.bnt_reset_password.setGeometry(QRect(70, 350, 201, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.bnt_reset_password.setFont(font3)
        self.bnt_reset_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bnt_reset_password.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
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
        self.label_version = QLabel(self.Mainframe)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(10, 10, 211, 16))
        self.label_version.setFont(font1)
        self.label_version.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.Mainframe.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.text_usuario.setText("")
#if QT_CONFIG(statustip)
        self.text_password.setStatusTip(QCoreApplication.translate("Dialog", u"ts", None))
#endif // QT_CONFIG(statustip)
        self.text_password.setText("")
        self.label_user.setText(QCoreApplication.translate("Dialog", u"Usu\u00e1rio:", None))
        self.label_password.setText(QCoreApplication.translate("Dialog", u"Senha:", None))
#if QT_CONFIG(tooltip)
        self.bnt_entrar.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Acessar o sistema.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_entrar.setText(QCoreApplication.translate("Dialog", u"Entrar", None))
        self.bnt_reset_password.setText(QCoreApplication.translate("Dialog", u"Esqueci senha", None))
        self.label_version.setText("")
    # retranslateUi


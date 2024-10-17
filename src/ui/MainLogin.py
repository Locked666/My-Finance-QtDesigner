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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(396, 555)
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Mainframe = QFrame(Login)
        self.Mainframe.setObjectName(u"Mainframe")
        self.Mainframe.setMinimumSize(QSize(396, 555))
        self.Mainframe.setMaximumSize(QSize(396, 555))
        self.Mainframe.setAutoFillBackground(False)
        self.Mainframe.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"")
        self.Mainframe.setFrameShape(QFrame.NoFrame)
        self.Mainframe.setFrameShadow(QFrame.Raised)
        self.label_version = QLabel(self.Mainframe)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(10, 10, 211, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_version.setFont(font)
        self.label_version.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self.Mainframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, -20, 221, 191))
        self.widget = QWidget(self.Mainframe)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 160, 381, 277))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setSpacing(25)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_user = QLabel(self.widget)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setFont(font)
        self.label_user.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_user)

        self.text_usuario = QLineEdit(self.widget)
        self.text_usuario.setObjectName(u"text_usuario")
        self.text_usuario.setMinimumSize(QSize(331, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.text_usuario.setFont(font1)
        self.text_usuario.setStyleSheet(u"border: 1px solid #2980b9; /* Borda ao redor do frame */\n"
"selection-background-color: rgb(28, 28, 28);\n"
"border-radius: 0px; /* Arredondamento se desejar */;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"background-color: rgb(28, 28, 28);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.text_usuario)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_password = QLabel(self.widget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font)
        self.label_password.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.label_password)

        self.text_password = QLineEdit(self.widget)
        self.text_password.setObjectName(u"text_password")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_password.sizePolicy().hasHeightForWidth())
        self.text_password.setSizePolicy(sizePolicy)
        self.text_password.setMinimumSize(QSize(331, 19))
        self.text_password.setFont(font1)
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
        self.text_password.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.text_password)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.checkBox.setChecked(False)

        self.verticalLayout_6.addWidget(self.checkBox)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(60, -1, -1, -1)
        self.bnt_entrar = QPushButton(self.widget)
        self.bnt_entrar.setObjectName(u"bnt_entrar")
        self.bnt_entrar.setMinimumSize(QSize(221, 31))
        self.bnt_entrar.setMaximumSize(QSize(221, 31))
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

        self.verticalLayout_4.addWidget(self.bnt_entrar)

        self.bnt_reset_password = QPushButton(self.widget)
        self.bnt_reset_password.setObjectName(u"bnt_reset_password")
        self.bnt_reset_password.setMinimumSize(QSize(201, 31))
        self.bnt_reset_password.setMaximumSize(QSize(201, 31))
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

        self.verticalLayout_4.addWidget(self.bnt_reset_password)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.Mainframe)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.Mainframe.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_version.setText("")
        self.label.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><img src=\":/icons/image_prin.png\"width=\"200\" height=\"200\"/></p></body></html>", None))
        self.label_user.setText(QCoreApplication.translate("Login", u"Usu\u00e1rio:", None))
        self.text_usuario.setText("")
        self.label_password.setText(QCoreApplication.translate("Login", u"Senha:", None))
#if QT_CONFIG(statustip)
        self.text_password.setStatusTip(QCoreApplication.translate("Login", u"ts", None))
#endif // QT_CONFIG(statustip)
        self.text_password.setText("")
        self.checkBox.setText(QCoreApplication.translate("Login", u"Salvar Senha", None))
#if QT_CONFIG(tooltip)
        self.bnt_entrar.setToolTip(QCoreApplication.translate("Login", u"<html><head/><body><p>Acessar o sistema.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_entrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.bnt_reset_password.setText(QCoreApplication.translate("Login", u"Esqueci senha", None))
    # retranslateUi


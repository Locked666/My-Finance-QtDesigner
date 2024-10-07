# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadReceita.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDateTimeEdit, QDialog, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_CadReceita(object):
    def setupUi(self, CadReceita):
        if not CadReceita.objectName():
            CadReceita.setObjectName(u"CadReceita")
        CadReceita.resize(405, 543)
        CadReceita.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        CadReceita.setModal(True)
        self.frame_2 = QFrame(CadReceita)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 100, 41))
        self.frame_2.setMaximumSize(QSize(100, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lcdNumber = QLCDNumber(self.frame_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 10, 64, 23))
        self.frame_3 = QFrame(CadReceita)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 480, 401, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(81, 41))
        self.pushButton.setMaximumSize(QSize(81, 41))

        self.horizontalLayout_21.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(81, 41))
        self.pushButton_2.setMaximumSize(QSize(81, 41))

        self.horizontalLayout_21.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(81, 41))

        self.horizontalLayout_21.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(81, 41))

        self.horizontalLayout_21.addWidget(self.pushButton_4)

        self.tab_receita = QTabWidget(CadReceita)
        self.tab_receita.setObjectName(u"tab_receita")
        self.tab_receita.setGeometry(QRect(0, 40, 411, 441))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 398, 301))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_7.addWidget(self.label_21)

        self.lineEdit_9 = QLineEdit(self.frame)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_7.addWidget(self.lineEdit_9)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_20.addWidget(self.label_20)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_20.addWidget(self.label_3)

        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaxLength(32767)
        self.lineEdit_8.setFrame(True)
        self.lineEdit_8.setCursorPosition(0)
        self.lineEdit_8.setClearButtonEnabled(False)

        self.horizontalLayout_20.addWidget(self.lineEdit_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)

        self.checkBox_6 = QCheckBox(self.frame)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setChecked(True)

        self.horizontalLayout_19.addWidget(self.checkBox_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_18.addWidget(self.label_19)

        self.dateEdit_3 = QDateEdit(self.frame)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setDate(QDate(2000, 1, 2))

        self.horizontalLayout_18.addWidget(self.dateEdit_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.dateTimeEdit_3 = QDateTimeEdit(self.frame)
        self.dateTimeEdit_3.setObjectName(u"dateTimeEdit_3")
        self.dateTimeEdit_3.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateTimeEdit_3.setCalendarPopup(True)

        self.horizontalLayout_16.addWidget(self.dateTimeEdit_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.checkBox_5 = QCheckBox(self.frame)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_15.addWidget(self.checkBox_5)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_15.addWidget(self.lineEdit_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_5.addWidget(self.label_17)

        self.comboBox_5 = QComboBox(self.frame)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_5.addWidget(self.comboBox_5)


        self.horizontalLayout_17.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_6.addWidget(self.label_18)

        self.comboBox_6 = QComboBox(self.frame)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.verticalLayout_6.addWidget(self.comboBox_6)


        self.horizontalLayout_17.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.label_23 = QLabel(self.tab_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 290, 141, 21))
        self.textEdit = QTextEdit(self.tab_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 310, 381, 91))
        self.textEdit.setAutoFormatting(QTextEdit.AutoBulletList)
        self.tab_receita.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.frame_4 = QFrame(self.tab_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 401, 151))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.tab_receita.addTab(self.tab_4, "")

        self.retranslateUi(CadReceita)

        self.tab_receita.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CadReceita)
    # setupUi

    def retranslateUi(self, CadReceita):
        CadReceita.setWindowTitle(QCoreApplication.translate("CadReceita", u"Cadastro de Receitas", None))
        self.pushButton.setText(QCoreApplication.translate("CadReceita", u"&Alterar", None))
        self.pushButton_2.setText(QCoreApplication.translate("CadReceita", u"&Salvar", None))
        self.pushButton_3.setText(QCoreApplication.translate("CadReceita", u"&Incluir", None))
        self.pushButton_4.setText(QCoreApplication.translate("CadReceita", u"&Cancelar", None))
        self.label_21.setText(QCoreApplication.translate("CadReceita", u"Descri\u00e7\u00e3o :", None))
        self.label_20.setText(QCoreApplication.translate("CadReceita", u"Valor:", None))
        self.label_3.setText(QCoreApplication.translate("CadReceita", u"R$", None))
        self.lineEdit_8.setInputMask("")
        self.lineEdit_8.setText("")
        self.checkBox_6.setText(QCoreApplication.translate("CadReceita", u"Efetivar ?", None))
        self.label_19.setText(QCoreApplication.translate("CadReceita", u"Data do Recebimento:", None))
        self.label_16.setText(QCoreApplication.translate("CadReceita", u"Data do Lan\u00e7amento", None))
        self.checkBox_5.setText(QCoreApplication.translate("CadReceita", u"Repetir ?", None))
        self.label_15.setText(QCoreApplication.translate("CadReceita", u"Per\u00edodo em Meses :", None))
        self.label_17.setText(QCoreApplication.translate("CadReceita", u"Origem da Receita:", None))
        self.label_18.setText(QCoreApplication.translate("CadReceita", u"Conta Cr\u00e9dito", None))
        self.label_23.setText(QCoreApplication.translate("CadReceita", u"Observa\u00e7\u00f5es", None))
        self.textEdit.setDocumentTitle("")
        self.tab_receita.setTabText(self.tab_receita.indexOf(self.tab_3), QCoreApplication.translate("CadReceita", u"Dados Principais", None))
        self.tab_receita.setTabText(self.tab_receita.indexOf(self.tab_4), QCoreApplication.translate("CadReceita", u"Dados Adicionais ", None))
    # retranslateUi


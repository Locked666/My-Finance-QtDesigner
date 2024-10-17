# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadProdutos.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(882, 677)
        icon = QIcon()
        icon.addFile(u":/icons/smile.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 61))
        self.frame_3.setMaximumSize(QSize(16777215, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = QLCDNumber(self.frame_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(64, 23))
        self.lcdNumber.setMaximumSize(QSize(64, 23))

        self.horizontalLayout_8.addWidget(self.lcdNumber)

        self.horizontalSpacer_4 = QSpacerItem(642, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_principal = QWidget()
        self.tab_principal.setObjectName(u"tab_principal")
        self.groupBox = QGroupBox(self.tab_principal)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(390, 90, 456, 222))
        self.groupBox.setMaximumSize(QSize(456, 241))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(71, 21))
        self.lineEdit_2.setMaximumSize(QSize(71, 21))

        self.horizontalLayout_9.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(241, 21))
        self.lineEdit.setMaximumSize(QSize(241, 21))

        self.horizontalLayout_9.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(31, 31))
        self.pushButton.setMaximumSize(QSize(31, 31))
        icon1 = QIcon()
        icon1.addFile(u":/icons/adicionar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setFlat(True)

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_12)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(71, 21))
        self.lineEdit_3.setMaximumSize(QSize(71, 21))

        self.horizontalLayout_10.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(241, 21))
        self.lineEdit_4.setMaximumSize(QSize(241, 21))

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(31, 31))
        self.pushButton_2.setMaximumSize(QSize(31, 31))
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(25, 25))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_10.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(71, 21))
        self.lineEdit_5.setMaximumSize(QSize(71, 21))

        self.horizontalLayout_11.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(241, 21))
        self.lineEdit_6.setMaximumSize(QSize(241, 21))

        self.horizontalLayout_11.addWidget(self.lineEdit_6)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(31, 31))
        self.pushButton_3.setMaximumSize(QSize(31, 31))
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_11.addWidget(self.pushButton_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_16)

        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(71, 21))
        self.lineEdit_7.setMaximumSize(QSize(71, 21))

        self.horizontalLayout_14.addWidget(self.lineEdit_7)

        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(241, 21))
        self.lineEdit_10.setMaximumSize(QSize(241, 21))

        self.horizontalLayout_14.addWidget(self.lineEdit_10)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(31, 31))
        self.pushButton_4.setMaximumSize(QSize(31, 31))
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(25, 25))
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_14.addWidget(self.pushButton_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.label_17.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_17)

        self.lineEdit_11 = QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(71, 21))
        self.lineEdit_11.setMaximumSize(QSize(71, 21))

        self.horizontalLayout_15.addWidget(self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(241, 21))
        self.lineEdit_12.setMaximumSize(QSize(241, 21))

        self.horizontalLayout_15.addWidget(self.lineEdit_12)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(31, 31))
        self.pushButton_5.setMaximumSize(QSize(31, 31))
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(25, 25))
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_15.addWidget(self.pushButton_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.layoutWidget_5 = QWidget(self.tab_principal)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 10, 391, 33))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.lineEdit_8 = QLineEdit(self.layoutWidget_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(241, 21))
        self.lineEdit_8.setMaximumSize(QSize(333, 21))

        self.horizontalLayout_12.addWidget(self.lineEdit_8)

        self.layoutWidget_6 = QWidget(self.tab_principal)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 50, 391, 33))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_15)

        self.lineEdit_9 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(241, 21))
        self.lineEdit_9.setMaximumSize(QSize(333, 21))

        self.horizontalLayout_13.addWidget(self.lineEdit_9)

        self.tabWidget.addTab(self.tab_principal, "")
        self.tab_tributacao = QWidget()
        self.tab_tributacao.setObjectName(u"tab_tributacao")
        self.tabWidget.addTab(self.tab_tributacao, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 41))
        self.frame_4.setMaximumSize(QSize(16777215, 41))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(731, 94))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lbl_total = QLabel(self.frame)
        self.lbl_total.setObjectName(u"lbl_total")

        self.horizontalLayout_4.addWidget(self.lbl_total)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bnt_back_full = QPushButton(self.frame)
        self.bnt_back_full.setObjectName(u"bnt_back_full")
        self.bnt_back_full.setMinimumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.bnt_back_full)

        self.bnt_back = QPushButton(self.frame)
        self.bnt_back.setObjectName(u"bnt_back")
        self.bnt_back.setMinimumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.bnt_back)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bnt_next = QPushButton(self.frame)
        self.bnt_next.setObjectName(u"bnt_next")
        self.bnt_next.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.bnt_next)

        self.bnt_next_full = QPushButton(self.frame)
        self.bnt_next_full.setObjectName(u"bnt_next_full")
        self.bnt_next_full.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.bnt_next_full)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.bnt_alterar = QPushButton(self.frame)
        self.bnt_alterar.setObjectName(u"bnt_alterar")
        self.bnt_alterar.setMinimumSize(QSize(100, 30))
        self.bnt_alterar.setMaximumSize(QSize(131, 41))
        icon2 = QIcon()
        icon2.addFile(u":/icons/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_alterar.setIcon(icon2)
        self.bnt_alterar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bnt_alterar)

        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bnt_adicionar = QPushButton(self.frame)
        self.bnt_adicionar.setObjectName(u"bnt_adicionar")
        self.bnt_adicionar.setEnabled(True)
        self.bnt_adicionar.setMinimumSize(QSize(100, 30))
        self.bnt_adicionar.setMaximumSize(QSize(131, 41))
        self.bnt_adicionar.setIcon(icon1)
        self.bnt_adicionar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bnt_adicionar)

        self.bnt_salvar = QPushButton(self.frame)
        self.bnt_salvar.setObjectName(u"bnt_salvar")
        self.bnt_salvar.setEnabled(False)
        self.bnt_salvar.setMinimumSize(QSize(100, 0))
        self.bnt_salvar.setMaximumSize(QSize(100, 36))
        icon3 = QIcon()
        icon3.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_salvar.setIcon(icon3)
        self.bnt_salvar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.bnt_salvar)

        self.bnt_search = QPushButton(self.frame)
        self.bnt_search.setObjectName(u"bnt_search")
        self.bnt_search.setMinimumSize(QSize(100, 36))
        self.bnt_search.setMaximumSize(QSize(100, 36))
        icon4 = QIcon()
        icon4.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_search.setIcon(icon4)
        self.bnt_search.setIconSize(QSize(17, 17))
        self.bnt_search.setCheckable(False)
        self.bnt_search.setChecked(False)
        self.bnt_search.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_search)

        self.bnt_excluir = QPushButton(self.frame)
        self.bnt_excluir.setObjectName(u"bnt_excluir")
        self.bnt_excluir.setMinimumSize(QSize(100, 30))
        self.bnt_excluir.setMaximumSize(QSize(131, 41))
        icon5 = QIcon()
        icon5.addFile(u":/icons/excluir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_excluir.setIcon(icon5)
        self.bnt_excluir.setIconSize(QSize(25, 25))
        self.bnt_excluir.setCheckable(False)
        self.bnt_excluir.setChecked(False)
        self.bnt_excluir.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_excluir)

        self.bnt_cancelar = QPushButton(self.frame)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")
        self.bnt_cancelar.setMinimumSize(QSize(100, 30))
        self.bnt_cancelar.setMaximumSize(QSize(131, 41))
        icon6 = QIcon()
        icon6.addFile(u":/icons/error.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_cancelar.setIcon(icon6)
        self.bnt_cancelar.setIconSize(QSize(25, 25))
        self.bnt_cancelar.setCheckable(False)
        self.bnt_cancelar.setChecked(False)
        self.bnt_cancelar.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_cancelar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Data Inclus\u00e3o: ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"10/01/2024", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Data Altera\u00e7\u00e3o:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"10/01/2024", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Usu\u00e1rio Altera\u00e7\u00e3o:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Julio Sergio", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Classifica\u00e7\u00e3o do Produto", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"*Grupo :", None))
        self.pushButton.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"*SubGrupo :", None))
        self.pushButton_2.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"*Categoria :", None))
        self.pushButton_3.setText("")
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Marca :", None))
        self.pushButton_4.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Grupo de Pre\u00e7o", None))
        self.pushButton_5.setText("")
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Descri\u00e7\u00e3o ", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Descri\u00e7\u00e3o ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_principal), QCoreApplication.translate("Dialog", u"Dado Principais", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tributacao), QCoreApplication.translate("Dialog", u"Tributa\u00e7\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Quantidade de cadastros:", None))
        self.lbl_total.setText(QCoreApplication.translate("Dialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.bnt_back_full.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Ir para o primeiro...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back_full.setText(QCoreApplication.translate("Dialog", u"<<", None))
#if QT_CONFIG(tooltip)
        self.bnt_back.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Voltar...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back.setText(QCoreApplication.translate("Dialog", u"<", None))
#if QT_CONFIG(tooltip)
        self.bnt_next.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Pr\u00f3ximo...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next.setText(QCoreApplication.translate("Dialog", u">", None))
#if QT_CONFIG(tooltip)
        self.bnt_next_full.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Ir para o fim.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next_full.setText(QCoreApplication.translate("Dialog", u">>", None))
        self.bnt_alterar.setText(QCoreApplication.translate("Dialog", u"&Alterar", None))
        self.bnt_adicionar.setText(QCoreApplication.translate("Dialog", u"&Incluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_adicionar.setShortcut(QCoreApplication.translate("Dialog", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_salvar.setText(QCoreApplication.translate("Dialog", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_salvar.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.bnt_search.setText(QCoreApplication.translate("Dialog", u"&Pesquisar", None))
#if QT_CONFIG(shortcut)
        self.bnt_search.setShortcut(QCoreApplication.translate("Dialog", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_excluir.setText(QCoreApplication.translate("Dialog", u"&Excluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_excluir.setShortcut(QCoreApplication.translate("Dialog", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_cancelar.setText(QCoreApplication.translate("Dialog", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.bnt_cancelar.setShortcut(QCoreApplication.translate("Dialog", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


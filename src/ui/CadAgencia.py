# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadAgencia.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLCDNumber, QLabel,
    QLayout, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(731, 524)
        Dialog.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.verticalLayout_15 = QVBoxLayout(Dialog)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.DdPrincipal = QWidget()
        self.DdPrincipal.setObjectName(u"DdPrincipal")
        self.widget = QWidget(self.DdPrincipal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 9, 577, 226))
        self.verticalLayout_18 = QVBoxLayout(self.widget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lcdNumber = QLCDNumber(self.widget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.horizontalLayout.addWidget(self.lcdNumber)

        self.horizontalSpacer = QSpacerItem(438, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout_18.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(131, 21))

        self.verticalLayout.addWidget(self.lineEdit_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(321, 22))
        self.comboBox.setMaximumSize(QSize(321, 22))

        self.verticalLayout_2.addWidget(self.comboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(35, 35))
        self.pushButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_18.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(131, 21))
        self.lineEdit.setMaximumSize(QSize(131, 21))

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(61, 21))
        self.lineEdit_3.setMaximumSize(QSize(61, 21))

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_18.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(241, 21))
        self.lineEdit_2.setMaximumSize(QSize(241, 21))
        self.lineEdit_2.setCursorPosition(18)

        self.verticalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout_18.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.DdPrincipal, "")
        self.DdAdicionais = QWidget()
        self.DdAdicionais.setObjectName(u"DdAdicionais")
        self.widget1 = QWidget(self.DdAdicionais)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(370, 210, 323, 160))
        self.vertical_obs = QVBoxLayout(self.widget1)
        self.vertical_obs.setSpacing(0)
        self.vertical_obs.setObjectName(u"vertical_obs")
        self.vertical_obs.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.widget1)
        self.label_27.setObjectName(u"label_27")

        self.vertical_obs.addWidget(self.label_27)

        self.plainTextEdit = QPlainTextEdit(self.widget1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(321, 100))
        self.plainTextEdit.setMaximumSize(QSize(321, 100))

        self.vertical_obs.addWidget(self.plainTextEdit)

        self.widget2 = QWidget(self.DdAdicionais)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 10, 638, 212))
        self.verticalLayout_6 = QVBoxLayout(self.widget2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.vertical_rua = QVBoxLayout()
        self.vertical_rua.setSpacing(0)
        self.vertical_rua.setObjectName(u"vertical_rua")
        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")

        self.vertical_rua.addWidget(self.label_11)

        self.lineEdit_9 = QLineEdit(self.widget2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(501, 21))
        self.lineEdit_9.setMaximumSize(QSize(501, 21))

        self.vertical_rua.addWidget(self.lineEdit_9)


        self.horizontalLayout_9.addLayout(self.vertical_rua)

        self.vertical_numero = QVBoxLayout()
        self.vertical_numero.setObjectName(u"vertical_numero")
        self.label_18 = QLabel(self.widget2)
        self.label_18.setObjectName(u"label_18")

        self.vertical_numero.addWidget(self.label_18)

        self.lineEdit_16 = QLineEdit(self.widget2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(121, 21))
        self.lineEdit_16.setMaximumSize(QSize(121, 21))

        self.vertical_numero.addWidget(self.lineEdit_16)


        self.horizontalLayout_9.addLayout(self.vertical_numero)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.vertical_bairro = QVBoxLayout()
        self.vertical_bairro.setSpacing(0)
        self.vertical_bairro.setObjectName(u"vertical_bairro")
        self.label_19 = QLabel(self.widget2)
        self.label_19.setObjectName(u"label_19")

        self.vertical_bairro.addWidget(self.label_19)

        self.lineEdit_15 = QLineEdit(self.widget2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(291, 21))
        self.lineEdit_15.setMaximumSize(QSize(291, 21))

        self.vertical_bairro.addWidget(self.lineEdit_15)


        self.horizontalLayout_10.addLayout(self.vertical_bairro)

        self.vertical_complementar = QVBoxLayout()
        self.vertical_complementar.setSpacing(0)
        self.vertical_complementar.setObjectName(u"vertical_complementar")
        self.label_20 = QLabel(self.widget2)
        self.label_20.setObjectName(u"label_20")

        self.vertical_complementar.addWidget(self.label_20)

        self.lineEdit_17 = QLineEdit(self.widget2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(321, 21))
        self.lineEdit_17.setMaximumSize(QSize(321, 21))

        self.vertical_complementar.addWidget(self.lineEdit_17)


        self.horizontalLayout_10.addLayout(self.vertical_complementar)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.vertical_cep = QVBoxLayout()
        self.vertical_cep.setSpacing(0)
        self.vertical_cep.setObjectName(u"vertical_cep")
        self.label_21 = QLabel(self.widget2)
        self.label_21.setObjectName(u"label_21")

        self.vertical_cep.addWidget(self.label_21)

        self.lineEdit_18 = QLineEdit(self.widget2)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(161, 21))
        self.lineEdit_18.setMaximumSize(QSize(161, 21))

        self.vertical_cep.addWidget(self.lineEdit_18)


        self.horizontalLayout_11.addLayout(self.vertical_cep)

        self.vertical_cidade = QVBoxLayout()
        self.vertical_cidade.setSpacing(0)
        self.vertical_cidade.setObjectName(u"vertical_cidade")
        self.label_22 = QLabel(self.widget2)
        self.label_22.setObjectName(u"label_22")

        self.vertical_cidade.addWidget(self.label_22)

        self.lineEdit_19 = QLineEdit(self.widget2)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(291, 21))
        self.lineEdit_19.setMaximumSize(QSize(291, 21))

        self.vertical_cidade.addWidget(self.lineEdit_19)


        self.horizontalLayout_11.addLayout(self.vertical_cidade)

        self.vertical_uf = QVBoxLayout()
        self.vertical_uf.setSpacing(0)
        self.vertical_uf.setObjectName(u"vertical_uf")
        self.label_23 = QLabel(self.widget2)
        self.label_23.setObjectName(u"label_23")

        self.vertical_uf.addWidget(self.label_23)

        self.lineEdit_20 = QLineEdit(self.widget2)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(151, 21))
        self.lineEdit_20.setMaximumSize(QSize(151, 21))
        self.lineEdit_20.setInputMethodHints(Qt.ImhNoAutoUppercase)
        self.lineEdit_20.setMaxLength(2)

        self.vertical_uf.addWidget(self.lineEdit_20)


        self.horizontalLayout_11.addLayout(self.vertical_uf)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_24 = QLabel(self.widget2)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_12.addWidget(self.label_24)

        self.lineEdit_21 = QLineEdit(self.widget2)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(181, 21))
        self.lineEdit_21.setMaximumSize(QSize(181, 21))
        self.lineEdit_21.setMaxLength(15)
        self.lineEdit_21.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.verticalLayout_12.addWidget(self.lineEdit_21)


        self.horizontalLayout_4.addLayout(self.verticalLayout_12)

        self.checkBox_4 = QCheckBox(self.widget2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(False)

        self.horizontalLayout_4.addWidget(self.checkBox_4)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_25 = QLabel(self.widget2)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_13.addWidget(self.label_25)

        self.lineEdit_22 = QLineEdit(self.widget2)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(181, 21))
        self.lineEdit_22.setMaximumSize(QSize(181, 21))
        self.lineEdit_22.setMaxLength(14)
        self.lineEdit_22.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.verticalLayout_13.addWidget(self.lineEdit_22)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.widget3 = QWidget(self.DdAdicionais)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 230, 353, 50))
        self.vertical_email = QVBoxLayout(self.widget3)
        self.vertical_email.setSpacing(0)
        self.vertical_email.setObjectName(u"vertical_email")
        self.vertical_email.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.widget3)
        self.label_26.setObjectName(u"label_26")

        self.vertical_email.addWidget(self.label_26)

        self.lineEdit_23 = QLineEdit(self.widget3)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(351, 21))
        self.lineEdit_23.setMaximumSize(QSize(351, 21))

        self.vertical_email.addWidget(self.lineEdit_23)

        self.tabWidget.addTab(self.DdAdicionais, "")

        self.verticalLayout_15.addWidget(self.tabWidget)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lbl_total = QLabel(self.frame)
        self.lbl_total.setObjectName(u"lbl_total")

        self.horizontalLayout_5.addWidget(self.lbl_total)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bnt_back_full = QPushButton(self.frame)
        self.bnt_back_full.setObjectName(u"bnt_back_full")
        self.bnt_back_full.setMinimumSize(QSize(75, 23))

        self.horizontalLayout_7.addWidget(self.bnt_back_full)

        self.bnt_back = QPushButton(self.frame)
        self.bnt_back.setObjectName(u"bnt_back")
        self.bnt_back.setMinimumSize(QSize(75, 23))

        self.horizontalLayout_7.addWidget(self.bnt_back)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.bnt_next = QPushButton(self.frame)
        self.bnt_next.setObjectName(u"bnt_next")
        self.bnt_next.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_7.addWidget(self.bnt_next)

        self.bnt_next_full = QPushButton(self.frame)
        self.bnt_next_full.setObjectName(u"bnt_next_full")
        self.bnt_next_full.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_7.addWidget(self.bnt_next_full)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.bnt_alterar = QPushButton(self.frame)
        self.bnt_alterar.setObjectName(u"bnt_alterar")
        self.bnt_alterar.setMinimumSize(QSize(100, 30))
        self.bnt_alterar.setMaximumSize(QSize(131, 41))

        self.horizontalLayout_8.addWidget(self.bnt_alterar)

        self.horizontalSpacer_4 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.bnt_adicionar = QPushButton(self.frame)
        self.bnt_adicionar.setObjectName(u"bnt_adicionar")
        self.bnt_adicionar.setEnabled(True)
        self.bnt_adicionar.setMinimumSize(QSize(100, 30))
        self.bnt_adicionar.setMaximumSize(QSize(131, 41))

        self.horizontalLayout_8.addWidget(self.bnt_adicionar)

        self.bnt_salvar = QPushButton(self.frame)
        self.bnt_salvar.setObjectName(u"bnt_salvar")
        self.bnt_salvar.setEnabled(False)
        self.bnt_salvar.setMinimumSize(QSize(100, 0))
        self.bnt_salvar.setMaximumSize(QSize(100, 36))

        self.horizontalLayout_8.addWidget(self.bnt_salvar)

        self.bnt_search = QPushButton(self.frame)
        self.bnt_search.setObjectName(u"bnt_search")
        self.bnt_search.setMinimumSize(QSize(100, 0))
        self.bnt_search.setMaximumSize(QSize(100, 36))
        self.bnt_search.setCheckable(False)
        self.bnt_search.setChecked(False)
        self.bnt_search.setAutoRepeat(False)

        self.horizontalLayout_8.addWidget(self.bnt_search)

        self.bnt_excluir = QPushButton(self.frame)
        self.bnt_excluir.setObjectName(u"bnt_excluir")
        self.bnt_excluir.setMinimumSize(QSize(100, 30))
        self.bnt_excluir.setMaximumSize(QSize(131, 41))
        self.bnt_excluir.setCheckable(False)
        self.bnt_excluir.setChecked(False)
        self.bnt_excluir.setAutoRepeat(False)

        self.horizontalLayout_8.addWidget(self.bnt_excluir)

        self.bnt_cancelar = QPushButton(self.frame)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")
        self.bnt_cancelar.setMinimumSize(QSize(100, 30))
        self.bnt_cancelar.setMaximumSize(QSize(131, 41))
        self.bnt_cancelar.setCheckable(False)
        self.bnt_cancelar.setChecked(False)
        self.bnt_cancelar.setAutoRepeat(False)

        self.horizontalLayout_8.addWidget(self.bnt_cancelar)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)


        self.verticalLayout_15.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Ativo", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"C\u00f3digo Febraban :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Banco :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Banco do Brasil", None))

        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Ag\u00eancia", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u" -", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"CNPJ :", None))
        self.lineEdit_2.setInputMask(QCoreApplication.translate("Dialog", u"##.###.###/####-##", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"00.000.000/0000-00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DdPrincipal), QCoreApplication.translate("Dialog", u"Dados Principais", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Observa\u00e7\u00e3o :", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Rua :", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"N \u00ba :", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Bairro :", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Dados Complementares :", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"CEP :", None))
        self.lineEdit_18.setInputMask(QCoreApplication.translate("Dialog", u"#####-###", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Cidade:", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"UF :", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Celular:", None))
        self.lineEdit_21.setInputMask(QCoreApplication.translate("Dialog", u"(##) #####-####", None))
        self.lineEdit_21.setText(QCoreApplication.translate("Dialog", u"() ------", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Possui WhatsApp ?", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Telefone :", None))
        self.lineEdit_22.setInputMask(QCoreApplication.translate("Dialog", u"(##) ####-####", None))
        self.lineEdit_22.setText(QCoreApplication.translate("Dialog", u"() ------", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"E-mail :", None))
        self.lineEdit_23.setInputMask("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DdAdicionais), QCoreApplication.translate("Dialog", u"Dados Adicionais", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Quantidade de cadastros:", None))
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


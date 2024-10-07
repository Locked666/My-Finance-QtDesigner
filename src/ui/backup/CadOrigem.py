# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadOrigem.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_CadOrigem(object):
    def setupUi(self, CadOrigem):
        if not CadOrigem.objectName():
            CadOrigem.setObjectName(u"CadOrigem")
        CadOrigem.setWindowModality(Qt.ApplicationModal)
        CadOrigem.resize(685, 186)
        CadOrigem.setMinimumSize(QSize(685, 186))
        CadOrigem.setMaximumSize(QSize(685, 186))
        CadOrigem.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        CadOrigem.setModal(True)
        self.lcdNumber = QLCDNumber(CadOrigem)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(20, 10, 64, 23))
        self.widget = QWidget(CadOrigem)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 661, 29))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.comboBox.setFont(font)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.widget1 = QWidget(CadOrigem)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 130, 661, 43))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(111, 41))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(111, 41))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(111, 41))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(111, 41))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.widget2 = QWidget(CadOrigem)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 40, 191, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.widget2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.retranslateUi(CadOrigem)

        QMetaObject.connectSlotsByName(CadOrigem)
    # setupUi

    def retranslateUi(self, CadOrigem):
        CadOrigem.setWindowTitle(QCoreApplication.translate("CadOrigem", u"Cadastro de Origem", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CadOrigem", u"Receita", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("CadOrigem", u"Despesa", None))

        self.pushButton.setText(QCoreApplication.translate("CadOrigem", u"&Alterar", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("CadOrigem", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(whatsthis)
        self.pushButton_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_2.setText(QCoreApplication.translate("CadOrigem", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("CadOrigem", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("CadOrigem", u"&Incluir", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("CadOrigem", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("CadOrigem", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("CadOrigem", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("CadOrigem", u"Tipo :", None))
        self.label.setText(QCoreApplication.translate("CadOrigem", u"Descri\u00e7\u00e3o :", None))
    # retranslateUi


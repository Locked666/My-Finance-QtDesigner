# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadBank.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLCDNumber,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(704, 269)
        Dialog.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 711, 181))
        self.tabWidget.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 60, 501, 21))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 141, 21))
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 120, 241, 21))
        self.lineEdit_2.setCursorPosition(18)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 141, 21))
        self.lcdNumber = QLCDNumber(self.tab)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 10, 81, 23))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 90, 141, 21))
        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 120, 241, 21))
        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(570, 10, 101, 31))
        self.checkBox.setChecked(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(430, 220, 131, 41))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QRect(290, 220, 131, 41))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(570, 220, 131, 41))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 220, 131, 41))

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"CNPJ :", None))
        self.lineEdit_2.setInputMask(QCoreApplication.translate("Dialog", u"##.###.###/####-##", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"00.000.000/0000-00", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nome de banco :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"C\u00f3digo Febraban :", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Ativo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Dados Principais", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Outros", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"A&dicionar", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("Dialog", u"Alt+D", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("Dialog", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"&Alterar", None))
    # retranslateUi


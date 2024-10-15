# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadEntregas.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CadEntregas(object):
    def setupUi(self, CadEntregas):
        if not CadEntregas.objectName():
            CadEntregas.setObjectName(u"CadEntregas")
        CadEntregas.resize(359, 310)
        self.verticalLayout_2 = QVBoxLayout(CadEntregas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(CadEntregas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 50, 110, 22))
        self.dateEdit.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2024, 10, 15))
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 90, 278, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_4.addWidget(self.lineEdit_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.widget1 = QWidget(self.frame_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 140, 278, 43))
        self.horizontalLayout_5 = QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_5.addWidget(self.lineEdit_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_6.addWidget(self.lineEdit_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(CadEntregas)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(708, 94))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.bnt_alterar = QPushButton(self.frame)
        self.bnt_alterar.setObjectName(u"bnt_alterar")
        self.bnt_alterar.setMinimumSize(QSize(100, 30))
        self.bnt_alterar.setMaximumSize(QSize(131, 41))

        self.horizontalLayout.addWidget(self.bnt_alterar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(CadEntregas)

        QMetaObject.connectSlotsByName(CadEntregas)
    # setupUi

    def retranslateUi(self, CadEntregas):
        CadEntregas.setWindowTitle(QCoreApplication.translate("CadEntregas", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("CadEntregas", u"KM Inicial", None))
        self.label_3.setText(QCoreApplication.translate("CadEntregas", u"KM Final", None))
        self.label_4.setText(QCoreApplication.translate("CadEntregas", u"KM / LT", None))
        self.label_5.setText(QCoreApplication.translate("CadEntregas", u"QT de entregas ", None))
        self.bnt_alterar.setText(QCoreApplication.translate("CadEntregas", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_alterar.setShortcut(QCoreApplication.translate("CadEntregas", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


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
        CadEntregas.resize(359, 354)
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
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 90, 278, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.text_km_inicial = QLineEdit(self.layoutWidget)
        self.text_km_inicial.setObjectName(u"text_km_inicial")

        self.verticalLayout_3.addWidget(self.text_km_inicial)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.text_km_final = QLineEdit(self.layoutWidget)
        self.text_km_final.setObjectName(u"text_km_final")

        self.verticalLayout_4.addWidget(self.text_km_final)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(self.frame_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 140, 278, 43))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.text_km_media = QLineEdit(self.layoutWidget1)
        self.text_km_media.setObjectName(u"text_km_media")

        self.verticalLayout_5.addWidget(self.text_km_media)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.text_qt_entregas = QLineEdit(self.layoutWidget1)
        self.text_qt_entregas.setObjectName(u"text_qt_entregas")

        self.verticalLayout_6.addWidget(self.text_qt_entregas)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.layoutWidget_2 = QWidget(self.frame_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 190, 135, 41))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.text_vlr_final = QLineEdit(self.layoutWidget_2)
        self.text_vlr_final.setObjectName(u"text_vlr_final")

        self.verticalLayout_7.addWidget(self.text_vlr_final)


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
        self.bnt_salvar = QPushButton(self.frame)
        self.bnt_salvar.setObjectName(u"bnt_salvar")
        self.bnt_salvar.setMinimumSize(QSize(100, 30))
        self.bnt_salvar.setMaximumSize(QSize(131, 41))

        self.horizontalLayout.addWidget(self.bnt_salvar)


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
        self.label_6.setText(QCoreApplication.translate("CadEntregas", u"Valor final", None))
        self.bnt_salvar.setText(QCoreApplication.translate("CadEntregas", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_salvar.setShortcut(QCoreApplication.translate("CadEntregas", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDialog, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_CadProduto(object):
    def setupUi(self, CadProduto):
        if not CadProduto.objectName():
            CadProduto.setObjectName(u"CadProduto")
        CadProduto.resize(901, 677)
        CadProduto.setMinimumSize(QSize(901, 677))
        CadProduto.setMaximumSize(QSize(15000, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/smile.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        CadProduto.setWindowIcon(icon)
        self.verticalLayout_13 = QVBoxLayout(CadProduto)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_3 = QFrame(CadProduto)
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


        self.verticalLayout_13.addWidget(self.frame_3)

        self.frame_2 = QFrame(CadProduto)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 900))
        self.tabWidget.setMaximumSize(QSize(15000, 15000))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_principal = QWidget()
        self.tab_principal.setObjectName(u"tab_principal")
        self.groupBox = QGroupBox(self.tab_principal)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(410, 90, 456, 222))
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

        self.groupBox_2 = QGroupBox(self.tab_principal)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 90, 355, 71))
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_20.addWidget(self.label_8)

        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon2 = QIcon()
        icon2.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setFlat(True)

        self.horizontalLayout_20.addWidget(self.pushButton_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.lineEdit_13 = QLineEdit(self.groupBox_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(71, 100))

        self.verticalLayout_6.addWidget(self.lineEdit_13)


        self.horizontalLayout_19.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_17.addWidget(self.label_9)

        self.pushButton_8 = QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setFlat(True)

        self.horizontalLayout_17.addWidget(self.pushButton_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.lineEdit_14 = QLineEdit(self.groupBox_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(86, 100))

        self.verticalLayout_7.addWidget(self.lineEdit_14)


        self.horizontalLayout_19.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(1500, 16777215))

        self.horizontalLayout_23.addWidget(self.label_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.lineEdit_15 = QLineEdit(self.groupBox_2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMaximumSize(QSize(58, 100))

        self.verticalLayout_9.addWidget(self.lineEdit_15)


        self.horizontalLayout_19.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_24.addWidget(self.label_20)

        self.pushButton_11 = QPushButton(self.groupBox_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setFlat(True)

        self.horizontalLayout_24.addWidget(self.pushButton_11)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.lineEdit_16 = QLineEdit(self.groupBox_2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMaximumSize(QSize(86, 100))

        self.verticalLayout_10.addWidget(self.lineEdit_16)


        self.horizontalLayout_19.addLayout(self.verticalLayout_10)

        self.tableWidget = QTableWidget(self.tab_principal)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 320, 861, 91))
        self.widget = QWidget(self.tab_principal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 11, 790, 35))
        self.horizontalLayout_21 = QHBoxLayout(self.widget)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.lineEdit_8 = QLineEdit(self.widget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(312, 21))
        self.lineEdit_8.setMaximumSize(QSize(312, 21))
        self.lineEdit_8.setClearButtonEnabled(True)

        self.horizontalLayout_12.addWidget(self.lineEdit_8)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(127, 31))
        self.label_18.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_18)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(257, 20))

        self.horizontalLayout_16.addWidget(self.comboBox)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_16)

        self.widget1 = QWidget(self.tab_principal)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 51, 656, 35))
        self.horizontalLayout_22 = QHBoxLayout(self.widget1)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.widget1)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_15)

        self.lineEdit_9 = QLineEdit(self.widget1)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(294, 21))
        self.lineEdit_9.setMaximumSize(QSize(294, 21))
        self.lineEdit_9.setClearButtonEnabled(True)

        self.horizontalLayout_13.addWidget(self.lineEdit_9)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_19 = QLabel(self.widget1)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)
        self.label_19.setMinimumSize(QSize(100, 31))
        self.label_19.setMaximumSize(QSize(100, 16777215))
        self.label_19.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_19)

        self.comboBox_2 = QComboBox(self.widget1)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(150, 20))
        self.comboBox_2.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_18.addWidget(self.comboBox_2)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_18)

        self.widget2 = QWidget(self.tab_principal)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 170, 391, 126))
        self.horizontalLayout_36 = QHBoxLayout(self.widget2)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.widget2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(166, 124))
        self.horizontalLayout_25 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_5 = QFrame(self.groupBox_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(101, 91))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_25.addWidget(self.frame_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(37, 33))
        icon3 = QIcon()
        icon3.addFile(u":/icons/input_file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QSize(25, 25))
        self.pushButton_7.setFlat(True)

        self.verticalLayout_8.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(37, 33))
        icon4 = QIcon()
        icon4.addFile(u":/icons/delete_file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(25, 25))
        self.pushButton_6.setFlat(True)

        self.verticalLayout_8.addWidget(self.pushButton_6)


        self.horizontalLayout_25.addLayout(self.verticalLayout_8)


        self.horizontalLayout_36.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.widget2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(161, 121))
        self.widget3 = QWidget(self.groupBox_5)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 20, 119, 65))
        self.verticalLayout_18 = QVBoxLayout(self.widget3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.widget3)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_18.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_18.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.widget3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_18.addWidget(self.checkBox_3)


        self.horizontalLayout_36.addWidget(self.groupBox_5)

        self.tabWidget.addTab(self.tab_principal, "")
        self.tab_price = QWidget()
        self.tab_price.setObjectName(u"tab_price")
        self.frame_6 = QFrame(self.tab_price)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(9, 9, 857, 141))
        self.frame_6.setMinimumSize(QSize(0, 141))
        self.frame_6.setMaximumSize(QSize(16777215, 141))
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.frame_6)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(260, 10, 211, 108))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_25 = QLabel(self.layoutWidget_3)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_30.addWidget(self.label_25)

        self.lineEdit_21 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_21.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.lineEdit_21.setFrame(True)
        self.lineEdit_21.setDragEnabled(False)
        self.lineEdit_21.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_21.setClearButtonEnabled(True)

        self.horizontalLayout_30.addWidget(self.lineEdit_21)


        self.verticalLayout_12.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_26 = QLabel(self.layoutWidget_3)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_31.addWidget(self.label_26)

        self.lineEdit_22 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_22.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.lineEdit_22.setClearButtonEnabled(True)

        self.horizontalLayout_31.addWidget(self.lineEdit_22)


        self.verticalLayout_12.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_27 = QLabel(self.layoutWidget_3)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_32.addWidget(self.label_27)

        self.lineEdit_23 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_23.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.lineEdit_23.setClearButtonEnabled(True)

        self.horizontalLayout_32.addWidget(self.lineEdit_23)


        self.verticalLayout_12.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_28 = QLabel(self.layoutWidget_3)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_33.addWidget(self.label_28)

        self.lineEdit_24 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_24.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

        self.horizontalLayout_33.addWidget(self.lineEdit_24)


        self.verticalLayout_12.addLayout(self.horizontalLayout_33)

        self.widget4 = QWidget(self.frame_6)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(32, 12, 211, 108))
        self.verticalLayout_11 = QVBoxLayout(self.widget4)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_21 = QLabel(self.widget4)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_26.addWidget(self.label_21)

        self.lineEdit_17 = QLineEdit(self.widget4)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_17.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.lineEdit_17.setFrame(True)
        self.lineEdit_17.setDragEnabled(False)
        self.lineEdit_17.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_17.setClearButtonEnabled(True)

        self.horizontalLayout_26.addWidget(self.lineEdit_17)


        self.verticalLayout_11.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_22 = QLabel(self.widget4)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_27.addWidget(self.label_22)

        self.lineEdit_18 = QLineEdit(self.widget4)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_18.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.lineEdit_18.setClearButtonEnabled(True)

        self.horizontalLayout_27.addWidget(self.lineEdit_18)


        self.verticalLayout_11.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_24 = QLabel(self.widget4)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_28.addWidget(self.label_24)

        self.lineEdit_20 = QLineEdit(self.widget4)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_20.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.lineEdit_20.setClearButtonEnabled(True)

        self.horizontalLayout_28.addWidget(self.lineEdit_20)


        self.verticalLayout_11.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_23 = QLabel(self.widget4)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_29.addWidget(self.label_23)

        self.lineEdit_19 = QLineEdit(self.widget4)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_19.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

        self.horizontalLayout_29.addWidget(self.lineEdit_19)


        self.verticalLayout_11.addLayout(self.horizontalLayout_29)

        self.frame_7 = QFrame(self.tab_price)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(9, 156, 861, 251))
        self.frame_7.setMinimumSize(QSize(861, 251))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tableWidget_2 = QTableWidget(self.frame_7)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_14.addWidget(self.tableWidget_2)

        self.tabWidget.addTab(self.tab_price, "")
        self.tab_estoque = QWidget()
        self.tab_estoque.setObjectName(u"tab_estoque")
        self.verticalLayout_19 = QVBoxLayout(self.tab_estoque)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_4 = QGroupBox(self.tab_estoque)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 225))
        self.groupBox_4.setMaximumSize(QSize(16777215, 225))
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 5, -1, -1)
        self.tableWidget_3 = QTableWidget(self.groupBox_4)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMinimumSize(QSize(861, 192))
        self.tableWidget_3.setFrameShape(QFrame.NoFrame)
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setGridStyle(Qt.DashLine)
        self.tableWidget_3.setCornerButtonEnabled(True)

        self.verticalLayout_15.addWidget(self.tableWidget_3)


        self.verticalLayout_19.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.tab_estoque)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(261, 181))
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.groupBox_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(449, 166))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 855, 610))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tableWidget_4 = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.verticalLayout_17.addWidget(self.tableWidget_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_16.addWidget(self.scrollArea)


        self.verticalLayout_19.addWidget(self.groupBox_6)

        self.tabWidget.addTab(self.tab_estoque, "")
        self.tab_tributacao = QWidget()
        self.tab_tributacao.setObjectName(u"tab_tributacao")
        self.tabWidget.addTab(self.tab_tributacao, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_13.addWidget(self.frame_2)

        self.frame_4 = QFrame(CadProduto)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.widget5 = QWidget(self.frame_4)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(10, 0, 99, 52))
        self.verticalLayout_4 = QVBoxLayout(self.widget5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(15)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_29 = QLabel(self.widget5)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_34.addWidget(self.label_29)

        self.label_30 = QLabel(self.widget5)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_34.addWidget(self.label_30)


        self.verticalLayout_4.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(15)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_31 = QLabel(self.widget5)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_35.addWidget(self.label_31)

        self.label_32 = QLabel(self.widget5)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_35.addWidget(self.label_32)


        self.verticalLayout_4.addLayout(self.horizontalLayout_35)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.frame = QFrame(CadProduto)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(1000, 94))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, 10)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_alterar.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_salvar.setIcon(icon6)
        self.bnt_salvar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.bnt_salvar)

        self.bnt_search = QPushButton(self.frame)
        self.bnt_search.setObjectName(u"bnt_search")
        self.bnt_search.setMinimumSize(QSize(100, 36))
        self.bnt_search.setMaximumSize(QSize(100, 36))
        self.bnt_search.setIcon(icon2)
        self.bnt_search.setIconSize(QSize(17, 17))
        self.bnt_search.setCheckable(False)
        self.bnt_search.setChecked(False)
        self.bnt_search.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_search)

        self.bnt_excluir = QPushButton(self.frame)
        self.bnt_excluir.setObjectName(u"bnt_excluir")
        self.bnt_excluir.setMinimumSize(QSize(100, 30))
        self.bnt_excluir.setMaximumSize(QSize(131, 41))
        icon7 = QIcon()
        icon7.addFile(u":/icons/excluir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_excluir.setIcon(icon7)
        self.bnt_excluir.setIconSize(QSize(25, 25))
        self.bnt_excluir.setCheckable(False)
        self.bnt_excluir.setChecked(False)
        self.bnt_excluir.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_excluir)

        self.bnt_cancelar = QPushButton(self.frame)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")
        self.bnt_cancelar.setMinimumSize(QSize(100, 30))
        self.bnt_cancelar.setMaximumSize(QSize(131, 41))
        icon8 = QIcon()
        icon8.addFile(u":/icons/error.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_cancelar.setIcon(icon8)
        self.bnt_cancelar.setIconSize(QSize(25, 25))
        self.bnt_cancelar.setCheckable(False)
        self.bnt_cancelar.setChecked(False)
        self.bnt_cancelar.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_cancelar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_13.addWidget(self.frame)


        self.retranslateUi(CadProduto)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CadProduto)
    # setupUi

    def retranslateUi(self, CadProduto):
        CadProduto.setWindowTitle(QCoreApplication.translate("CadProduto", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("CadProduto", u"Data Inclus\u00e3o: ", None))
        self.label_3.setText(QCoreApplication.translate("CadProduto", u"10/01/2024", None))
        self.label_6.setText(QCoreApplication.translate("CadProduto", u"Data Altera\u00e7\u00e3o:", None))
        self.label_7.setText(QCoreApplication.translate("CadProduto", u"10/01/2024", None))
        self.label_4.setText(QCoreApplication.translate("CadProduto", u"Usu\u00e1rio Altera\u00e7\u00e3o:", None))
        self.label_5.setText(QCoreApplication.translate("CadProduto", u"Julio Sergio", None))
        self.groupBox.setTitle(QCoreApplication.translate("CadProduto", u"Classifica\u00e7\u00e3o do Produto", None))
        self.label_11.setText(QCoreApplication.translate("CadProduto", u"*Grupo :", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p><span style=\" color:#0055ff;\">Pesquisar.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_12.setText(QCoreApplication.translate("CadProduto", u"*SubGrupo :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p><span style=\" color:#0055ff;\">Pesquisar.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
        self.label_13.setText(QCoreApplication.translate("CadProduto", u"*Categoria :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p><span style=\" color:#0055ff;\">Pesquisar.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
        self.label_16.setText(QCoreApplication.translate("CadProduto", u"Marca :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p><span style=\" color:#0055ff;\">Pesquisar.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText("")
        self.label_17.setText(QCoreApplication.translate("CadProduto", u"Grupo de Pre\u00e7o", None))
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p><span style=\" color:#0055ff;\">Pesquisar.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("CadProduto", u"Outras informa\u00e7\u00f5es", None))
        self.label_8.setText(QCoreApplication.translate("CadProduto", u"Unid.", None))
        self.pushButton_9.setText("")
        self.label_9.setText(QCoreApplication.translate("CadProduto", u"C\u00f3digo F\u00e1b.", None))
        self.pushButton_8.setText("")
        self.label_10.setText(QCoreApplication.translate("CadProduto", u"Qt.Unid.", None))
        self.label_20.setText(QCoreApplication.translate("CadProduto", u"Medida.", None))
        self.pushButton_11.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CadProduto", u"C\u00f3digo de Barra", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CadProduto", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CadProduto", u"Quantidade", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CadProduto", u"%Desc", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CadProduto", u"%Acre", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CadProduto", u"Atacado", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("CadProduto", u"Inativo", None));
        self.label_14.setText(QCoreApplication.translate("CadProduto", u"Descri\u00e7\u00e3o ", None))
        self.label_18.setText(QCoreApplication.translate("CadProduto", u"Tipo do Produto :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CadProduto", u"Mercadoria Revenda", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("CadProduto", u"Material de Consumo", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("CadProduto", u"Mat\u00e9ria Prima", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("CadProduto", u"Bem m\u00f3vel", None))

        self.label_15.setText(QCoreApplication.translate("CadProduto", u"Nome Red. :", None))
        self.label_19.setText(QCoreApplication.translate("CadProduto", u"Situa\u00e7\u00e3o :", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("CadProduto", u"Ativo", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("CadProduto", u"Inativo", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("CadProduto", u"Imagem", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#0000ff;\">Adicionar Imagem...</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p><span style=\" font-weight:600; color:#0000ff;\">Excluir Imagem...</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("CadProduto", u"Parametros", None))
        self.checkBox.setText(QCoreApplication.translate("CadProduto", u"Produto Controlado", None))
        self.checkBox_2.setText(QCoreApplication.translate("CadProduto", u"Imprime Ticket", None))
        self.checkBox_3.setText(QCoreApplication.translate("CadProduto", u"Produto de Risco", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_principal), QCoreApplication.translate("CadProduto", u"Dado Principais", None))
        self.label_25.setText(QCoreApplication.translate("CadProduto", u"Margem Direta (R$):", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("CadProduto", u"0,00", None))
        self.label_26.setText(QCoreApplication.translate("CadProduto", u"Markup (R$):", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("CadProduto", u"0,00", None))
        self.label_27.setText(QCoreApplication.translate("CadProduto", u"Pre\u00e7o (R$):", None))
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("CadProduto", u"0,00", None))
        self.label_28.setText(QCoreApplication.translate("CadProduto", u"Pre\u00e7o sugerido(R$):", None))
        self.lineEdit_24.setPlaceholderText(QCoreApplication.translate("CadProduto", u"0,00", None))
        self.label_21.setText(QCoreApplication.translate("CadProduto", u"Custo Direto (R$):", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("CadProduto", u"0,00", None))
        self.label_22.setText(QCoreApplication.translate("CadProduto", u"Custo Indireto (R$):", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("CadProduto", u"0,00", None))
        self.label_24.setText(QCoreApplication.translate("CadProduto", u"Custo impostos (R$):", None))
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("CadProduto", u"0,00", None))
        self.label_23.setText(QCoreApplication.translate("CadProduto", u"Custo Diff:(R$):", None))
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("CadProduto", u"0,00", None))
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("CadProduto", u"C\u00f3digo", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("CadProduto", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("CadProduto", u"Grupo de Pre\u00e7o", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("CadProduto", u"Custo Total", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("CadProduto", u"Pre\u00e7o", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("CadProduto", u"Margem Final", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_price), QCoreApplication.translate("CadProduto", u"Precifica\u00e7\u00e3o", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("CadProduto", u"Movimenta\u00e7\u00e3o de estoque", None))
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("CadProduto", u"Empresa", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("CadProduto", u"Tipo", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("CadProduto", u"Data", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("CadProduto", u"Quantidade", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("CadProduto", u"Cliente/Fornecedor", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("CadProduto", u"Estoque", None));
        self.groupBox_6.setTitle(QCoreApplication.translate("CadProduto", u"Ultimas Entradas", None))
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("CadProduto", u"Empresa", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("CadProduto", u"C\u00f3digo", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("CadProduto", u"Fornecedor", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("CadProduto", u"Quantidade", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("CadProduto", u"Data", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_estoque), QCoreApplication.translate("CadProduto", u"Estoque", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tributacao), QCoreApplication.translate("CadProduto", u"Tributa\u00e7\u00e3o", None))
        self.label_29.setText(QCoreApplication.translate("CadProduto", u"Estoque Atual :", None))
        self.label_30.setText(QCoreApplication.translate("CadProduto", u"0", None))
        self.label_31.setText(QCoreApplication.translate("CadProduto", u"Pre\u00e7o Atual :", None))
        self.label_32.setText(QCoreApplication.translate("CadProduto", u"0", None))
        self.label_2.setText(QCoreApplication.translate("CadProduto", u"Quantidade de cadastros:", None))
        self.lbl_total.setText(QCoreApplication.translate("CadProduto", u"0", None))
#if QT_CONFIG(tooltip)
        self.bnt_back_full.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p>Ir para o primeiro...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back_full.setText(QCoreApplication.translate("CadProduto", u"<<", None))
#if QT_CONFIG(tooltip)
        self.bnt_back.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p>Voltar...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back.setText(QCoreApplication.translate("CadProduto", u"<", None))
#if QT_CONFIG(tooltip)
        self.bnt_next.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p>Pr\u00f3ximo...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next.setText(QCoreApplication.translate("CadProduto", u">", None))
#if QT_CONFIG(tooltip)
        self.bnt_next_full.setToolTip(QCoreApplication.translate("CadProduto", u"<html><head/><body><p><span style=\" font-weight:600;\">Ir para o fim.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next_full.setText(QCoreApplication.translate("CadProduto", u">>", None))
        self.bnt_alterar.setText(QCoreApplication.translate("CadProduto", u"&Alterar", None))
        self.bnt_adicionar.setText(QCoreApplication.translate("CadProduto", u"&Incluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_adicionar.setShortcut(QCoreApplication.translate("CadProduto", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_salvar.setText(QCoreApplication.translate("CadProduto", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_salvar.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.bnt_search.setText(QCoreApplication.translate("CadProduto", u"&Pesquisar", None))
#if QT_CONFIG(shortcut)
        self.bnt_search.setShortcut(QCoreApplication.translate("CadProduto", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_excluir.setText(QCoreApplication.translate("CadProduto", u"&Excluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_excluir.setShortcut(QCoreApplication.translate("CadProduto", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_cancelar.setText(QCoreApplication.translate("CadProduto", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.bnt_cancelar.setShortcut(QCoreApplication.translate("CadProduto", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


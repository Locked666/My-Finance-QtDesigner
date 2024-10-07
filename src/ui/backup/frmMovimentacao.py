# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmMovimentacao.ui'
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
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(909, 693)
        Dialog.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frmSearch = QFrame(Dialog)
        self.frmSearch.setObjectName(u"frmSearch")
        self.frmSearch.setMinimumSize(QSize(891, 101))
        self.frmSearch.setMaximumSize(QSize(16777215, 101))
        self.frmSearch.setFrameShape(QFrame.StyledPanel)
        self.frmSearch.setFrameShadow(QFrame.Raised)
        self.frmCheckSearch = QFrame(self.frmSearch)
        self.frmCheckSearch.setObjectName(u"frmCheckSearch")
        self.frmCheckSearch.setGeometry(QRect(400, 60, 477, 41))
        self.frmCheckSearch.setFrameShape(QFrame.StyledPanel)
        self.frmCheckSearch.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frmCheckSearch)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = QCheckBox(self.frmCheckSearch)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frmCheckSearch)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frmCheckSearch)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frmCheckSearch)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_2.addWidget(self.checkBox_4)

        self.widget = QWidget(self.frmSearch)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 861, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(130, 0))

        self.verticalLayout.addWidget(self.comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(230, 48))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frmSearch)

        self.frmTable = QFrame(Dialog)
        self.frmTable.setObjectName(u"frmTable")
        self.frmTable.setMinimumSize(QSize(891, 521))
        self.frmTable.setMaximumSize(QSize(891, 16777215))
        self.frmTable.setFrameShape(QFrame.StyledPanel)
        self.frmTable.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frmTable)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.frmTable)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(890, 521))

        self.horizontalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout_3.addWidget(self.frmTable)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(891, 55))
        self.frame.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"font: 75 11pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(630, 20, 47, 13))

        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Ativos", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"N\u00e3o Pagos", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Valores a Receber ", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Vencidos", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filtro :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"C\u00d3DIGO", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"TIPO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"DATA ", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"ATIVO", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Conteudo :", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Pesquisar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"C\u00d3DIGO", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"TIPO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"DATA", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"ATIVO", None));
        self.label_3.setText(QCoreApplication.translate("Dialog", u"TOTAL", None))
    # retranslateUi


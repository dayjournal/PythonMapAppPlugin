# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sample_Menu_02_Base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SampleMenu02Base(object):
    def setupUi(self, SampleMenu02Base):
        SampleMenu02Base.setObjectName("SampleMenu02Base")
        SampleMenu02Base.resize(336, 152)
        self.pushButton_go = QtWidgets.QPushButton(SampleMenu02Base)
        self.pushButton_go.setGeometry(QtCore.QRect(90, 90, 101, 41))
        self.pushButton_go.setObjectName("pushButton_go")
        self.pushButton_cancel = QtWidgets.QPushButton(SampleMenu02Base)
        self.pushButton_cancel.setGeometry(QtCore.QRect(210, 90, 101, 41))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.lineEdit = QtWidgets.QLineEdit(SampleMenu02Base)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 251, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(SampleMenu02Base)
        QtCore.QMetaObject.connectSlotsByName(SampleMenu02Base)

    def retranslateUi(self, SampleMenu02Base):
        _translate = QtCore.QCoreApplication.translate
        SampleMenu02Base.setWindowTitle(_translate("SampleMenu02Base", "Form"))
        self.pushButton_go.setText(_translate("SampleMenu02Base", "OK"))
        self.pushButton_cancel.setText(_translate("SampleMenu02Base", "キャンセル"))


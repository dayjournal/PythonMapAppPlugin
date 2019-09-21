# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Sample
                                 A QGIS plugin
 QGIS Sample Plugin
                              -------------------
        begin                : 2018-12-23
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Yasunori Kirimoto
        email                : contact@day-journal.com
        license              : GNU General Public License v2.0
 ***************************************************************************/
"""

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

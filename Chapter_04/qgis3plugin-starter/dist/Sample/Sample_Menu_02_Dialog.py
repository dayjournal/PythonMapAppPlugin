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

from PyQt5 import uic, QtWidgets, QtCore

#Ui_SampleMenu02Base読み込み
from .Sample_Menu_02_Base import Ui_SampleMenu02Base

class SampleMenu02Dialog(QtWidgets.QDialog, Ui_SampleMenu02Base):
    def __init__(self, parent=None):
        super(SampleMenu02Dialog, self).__init__(parent)
        self.setupUi(self)

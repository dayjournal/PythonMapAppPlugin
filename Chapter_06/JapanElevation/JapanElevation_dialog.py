# -*- coding: utf-8 -*-
"""
/***************************************************************************
 JapanElevation
                                 A QGIS plugin
 Display elevation value of specified position on QGIS.  
 Using Elevation API by Geospatial Information Authority of Japan.  
                              -------------------
        begin                : 2018-03-14
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Yasunori Kirimoto
        email                : contact@day-journal.com
        license              : GNU General Public License v2.0
 ***************************************************************************/
"""

import os

from PyQt5 import uic, QtWidgets, QtCore
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'JapanElevation_dialog_base.ui'))

class JapanElevationDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(JapanElevationDialog, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)

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

from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from qgis.core import *
from qgis.gui import *

from .resources import *
from .JapanElevation_dialog import JapanElevationDialog

import os.path
import os
import sys
import codecs
import urllib.request, urllib.error, urllib.parse
import json

class JapanElevation:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.dlg = JapanElevationDialog()
        self.dlg.hide()  
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'JapanElevation_{}.qm'.format(locale))
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        self.actions = []
        self.menu = self.tr(u'&JapanElevation')
        self.toolbar = self.iface.addToolBar(u'JapanElevation')
        self.toolbar.setObjectName(u'JapanElevation')
    def tr(self, message):
        return QCoreApplication.translate('JapanElevation', message)
    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)
        if status_tip is not None:
            action.setStatusTip(status_tip)
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        if add_to_toolbar:
            self.toolbar.addAction(action)
        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)
        self.actions.append(action)
        return action
    def initGui(self):
        icon_path = ':/plugins/JapanElevation/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'JapanElevation'),
            callback=self.run,
            parent=self.iface.mainWindow())
    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&JapanElevation'),
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar
    def run(self):
        self.toolClick = QgsMapToolClick(self.iface, self.canvas, self.dlg)
        self.canvas.setMapTool(self.toolClick)

class QgsMapToolClick(QgsMapTool):
    def __init__(self, iface, canvas, dlg):
        QgsMapTool.__init__(self, canvas)
        self.iface = iface
        self.canvas = canvas
        self.dlg = dlg
    def canvasPressEvent(self, mouseEvent):
        self.dlg.show()
        dPos = mouseEvent.pos()
        mPosBefore = self.toMapCoordinates(dPos)
        destcrs = self.iface.mapCanvas().mapSettings().destinationCrs()
        Tf = QgsCoordinateTransform(destcrs, QgsCoordinateReferenceSystem(4326), QgsProject.instance())
        mPos = Tf.transform(mPosBefore)
        lon = mPos.x()
        lat = mPos.y()
        URL = "http://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon=" + str(lon) + "&lat=" + str(lat) +"&outtype=JSON"
        data_all = urllib.request.urlopen(URL)
        data = json.loads(data_all.read())
        elevationall = str(data['elevation'])+ u' m'
        elevationtext = data[u'hsrc']
        self.dlg.label.setText(elevationall)
        self.dlg.label_2.setText(elevationtext)
        self.dlg.show()
        data_all.close()

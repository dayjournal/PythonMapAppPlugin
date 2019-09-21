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

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
from .resources import *

#メニュー読み込み
from .Sample_Menu_01 import SampleMenu01
from .Sample_Menu_02 import SampleMenu02

import os
import os.path
import sys
import codecs

QString = str

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Sample:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()

        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Sample_{}.qm'.format(locale))
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        self.actions = []
        self.menu = u'Sample'
        self.toolbar = self.iface.addToolBar(u'Sample')
        self.toolbar.setObjectName(u'Sample')

    def tr(self, message):
        return QCoreApplication.translate('Sample', message)

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
        self.win = self.iface.mainWindow()
        icon_path = ':/plugins/Sample/icon.png'
        #メニュー設定
        self.add_action(
            icon_path=None,
            text=u"Menu01",
            callback=self.Menu01,
            parent=self.win)
        self.add_action(
            icon_path=None,
            text=u"Menu02",
            callback=self.Menu02,
            parent=self.win)

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(
                u'Sample',
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    #Menu01メニュークリック
    def Menu01(self):
        #SampleMenu01読み込み
        self.sample_menu_01 = SampleMenu01(self.iface)
        #Menu01クリックでメッセージ表示
        self.sample_menu_01.message_add()

    #Menu02メニュークリック
    def Menu02(self):
        #SampleMenu02読み込み
        self.sample_menu_02 = SampleMenu02(self.iface)
        #SampleMenu02Dialog表示
        self.sample_menu_02.dlg.show()

    def run(self):
        pass

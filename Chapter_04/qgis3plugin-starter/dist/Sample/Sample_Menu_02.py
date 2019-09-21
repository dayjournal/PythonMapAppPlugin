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

#SampleMenu02Dialog読み込み
from .Sample_Menu_02_Dialog import SampleMenu02Dialog

QString = str

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class SampleMenu02:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        #SampleMenu02Dialog読み込み
        self.dlg = SampleMenu02Dialog()
        #ボタン設定
        self.dlg.pushButton_go.clicked.connect(self.dlg_add)
        self.dlg.pushButton_cancel.clicked.connect(self.dlg_cancel)

    #キャンセルクリック
    def dlg_cancel(self):
        #SampleMenu02Dialog非表示
        self.dlg.hide()

    #OKクリック
    def dlg_add(self):
        #テキストボックス値取得
        text_value = self.dlg.lineEdit.text()
        #テキストボックス値をメッセージ表示
        QMessageBox.information(None, u'ウィンドウ名', str(text_value))

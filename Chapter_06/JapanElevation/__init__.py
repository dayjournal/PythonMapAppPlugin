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

def classFactory(iface):
    from .JapanElevation import JapanElevation
    return JapanElevation(iface)
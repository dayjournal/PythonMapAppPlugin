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

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x06\x22\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x19\x00\x00\x00\x19\x08\x06\x00\x00\x00\xc4\xe9\x85\x63\
\x00\x00\x00\x01\x73\x52\x47\x42\x00\xae\xce\x1c\xe9\x00\x00\x00\
\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\
\x9c\x18\x00\x00\x01\x59\x69\x54\x58\x74\x58\x4d\x4c\x3a\x63\x6f\
\x6d\x2e\x61\x64\x6f\x62\x65\x2e\x78\x6d\x70\x00\x00\x00\x00\x00\
\x3c\x78\x3a\x78\x6d\x70\x6d\x65\x74\x61\x20\x78\x6d\x6c\x6e\x73\
\x3a\x78\x3d\x22\x61\x64\x6f\x62\x65\x3a\x6e\x73\x3a\x6d\x65\x74\
\x61\x2f\x22\x20\x78\x3a\x78\x6d\x70\x74\x6b\x3d\x22\x58\x4d\x50\
\x20\x43\x6f\x72\x65\x20\x35\x2e\x34\x2e\x30\x22\x3e\x0a\x20\x20\
\x20\x3c\x72\x64\x66\x3a\x52\x44\x46\x20\x78\x6d\x6c\x6e\x73\x3a\
\x72\x64\x66\x3d\x22\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\
\x77\x33\x2e\x6f\x72\x67\x2f\x31\x39\x39\x39\x2f\x30\x32\x2f\x32\
\x32\x2d\x72\x64\x66\x2d\x73\x79\x6e\x74\x61\x78\x2d\x6e\x73\x23\
\x22\x3e\x0a\x20\x20\x20\x20\x20\x20\x3c\x72\x64\x66\x3a\x44\x65\
\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x20\x72\x64\x66\x3a\x61\x62\
\x6f\x75\x74\x3d\x22\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\
\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x74\x69\x66\x66\x3d\x22\x68\
\x74\x74\x70\x3a\x2f\x2f\x6e\x73\x2e\x61\x64\x6f\x62\x65\x2e\x63\
\x6f\x6d\x2f\x74\x69\x66\x66\x2f\x31\x2e\x30\x2f\x22\x3e\x0a\x20\
\x20\x20\x20\x20\x20\x20\x20\x20\x3c\x74\x69\x66\x66\x3a\x4f\x72\
\x69\x65\x6e\x74\x61\x74\x69\x6f\x6e\x3e\x31\x3c\x2f\x74\x69\x66\
\x66\x3a\x4f\x72\x69\x65\x6e\x74\x61\x74\x69\x6f\x6e\x3e\x0a\x20\
\x20\x20\x20\x20\x20\x3c\x2f\x72\x64\x66\x3a\x44\x65\x73\x63\x72\
\x69\x70\x74\x69\x6f\x6e\x3e\x0a\x20\x20\x20\x3c\x2f\x72\x64\x66\
\x3a\x52\x44\x46\x3e\x0a\x3c\x2f\x78\x3a\x78\x6d\x70\x6d\x65\x74\
\x61\x3e\x0a\x4c\xc2\x27\x59\x00\x00\x04\x62\x49\x44\x41\x54\x48\
\x0d\xdd\x15\x4d\x6c\x14\x55\xf8\x7b\x6f\xde\xcc\xbe\xd9\x76\xbb\
\xdd\xd2\x1a\xe9\x89\x83\x70\xd8\x06\xe5\xe4\x89\xa8\x90\xe8\x81\
\x04\x49\x0f\x6d\x4c\x9a\x26\x98\x20\x94\xd6\x02\x0d\x6a\x63\x4c\
\xcc\x9c\x80\x8a\x87\x46\x54\xd2\xc6\x44\x91\x16\xe3\x36\x1a\x4e\
\x26\x7a\x42\xe3\xc1\xb3\xa6\x5c\xbc\x70\x30\x94\x94\xc8\xa4\xd9\
\xee\xee\xfc\xbe\xe7\xf7\xbd\xd9\x59\x2a\xb6\xe8\xc1\x8b\xbe\xcd\
\xe6\x7b\xef\xfb\xff\x1f\x80\xff\xcb\x61\xcb\x97\x26\xbf\x05\x8e\
\xe1\x68\xb0\x40\x6b\x06\x8c\xe9\x1d\x83\x23\x3a\x9d\x9c\x27\xe7\
\xcf\x61\x2e\xf8\xf0\xad\x50\xaf\x16\x45\xd7\x79\x89\x68\x4a\xef\
\xac\xdb\xe2\x1c\xed\xeb\xc7\xf2\xe4\xfa\xb7\x42\xce\x32\x9f\x44\
\x14\x27\x90\xa4\xe9\xaf\x60\xf1\x13\x2a\xe1\x1b\xc2\x52\x12\x14\
\x4b\x53\xa5\x32\x0e\x1b\x40\xa4\xb0\xa9\xb8\xb6\xb5\x12\x12\xcd\
\xa9\x0e\x6d\xab\x46\xbc\xa3\x33\x1a\xb8\xb6\x92\x94\x07\x1c\x54\
\x19\x98\xfe\x44\x58\x7c\xaf\xb0\x85\x40\x23\x2a\x18\x7b\xe3\xa3\
\x1f\x1e\x91\xe9\x3c\x97\x2f\x9e\xae\x8c\xcd\x5e\xf5\x3b\x88\x7f\
\x78\x59\x9e\x9b\x0c\x48\x3f\xfb\x6a\xfe\xac\x0e\x82\xe4\x36\x3a\
\x78\x70\xec\xed\xab\xfe\xa7\xde\x71\xb9\x07\xf6\x24\x77\xe0\x8e\
\x78\xd5\xfb\x2c\x58\xbe\x34\x75\x0c\x3d\xba\x89\x7a\x7f\xc2\x7c\
\x1d\x21\x9e\x6f\x3e\x98\x2e\x6c\x3e\x79\x2f\x19\x1d\x5d\x49\x6b\
\xde\x88\xe3\xef\xae\x98\x5c\xef\x5b\x1b\xd4\x1d\x39\x74\x0c\x43\
\xfb\x51\x3a\xa2\x2a\x8c\x53\x4c\x6b\x3b\x60\x31\xdd\xbb\x56\x1b\
\xf1\xa1\x15\x2f\xad\x8d\x8c\x64\x45\xe2\x30\x38\xd8\x5f\x81\xbb\
\xeb\x7e\x55\xa9\x54\x12\xcf\x91\x33\x57\x42\x52\xbe\x34\x37\xbd\
\x7b\x74\xf6\xca\x6f\x84\xcb\x4f\x2e\x67\x87\x2c\x8e\xdd\xac\xd0\
\xd4\x57\x54\x54\x56\x77\x83\xac\x06\x23\x19\xfb\x48\xad\xa6\xe8\
\xd6\x53\x8e\xaf\xad\xad\xfb\x13\xcc\xe2\xc3\xe3\xef\x2c\xae\x2d\
\x2c\x9c\xc4\x2a\x01\x24\xc5\x81\xc3\x0c\xd2\x2f\x28\x2a\x7a\xa3\
\x72\x8b\x20\xb4\xe5\x8d\x3e\xea\x32\x3c\x59\x24\x74\x7b\xe4\x30\
\x6c\x53\xcf\xf3\xf8\xd1\x53\x5e\x13\x49\x0b\x44\x46\xbf\x10\xbd\
\x68\x22\xc6\xfb\x6b\xbb\x7a\xbb\x0f\x3e\xf0\x1b\xc7\x90\x54\x1b\
\x18\x1a\x62\xb0\xb2\x42\x6c\xe6\x94\xba\xa5\x8e\xeb\x59\x32\x76\
\x34\x42\x9c\x68\xc4\x44\x83\x10\xf9\x6e\xc1\xe2\xe2\x3e\xf4\x6c\
\x31\xbe\x7e\x71\xe2\x05\x24\x1f\x0d\xc2\x18\x34\x53\xe7\x31\x75\
\x37\x0f\x79\x5e\x44\x4e\x01\xac\x92\xa8\x39\xf9\x50\x98\x74\xe5\
\xc8\x1c\x66\xcc\xe8\xbe\x77\xb2\x78\x63\x6e\xf2\xfd\xaa\xf4\x07\
\x3d\xef\x56\x52\xa9\xf8\xc6\x28\xe3\x6c\xa6\x28\x1d\xbb\xd1\x0a\
\x22\x59\x70\x9e\x0d\xe5\xc0\x2b\x24\x5b\xad\xae\x66\x29\x6f\x2b\
\xca\x1f\xc6\x48\xfe\xc8\x8d\x20\x34\xf8\x6e\x57\x0c\xf7\xf7\xf5\
\x9c\x8f\x59\x7c\x82\x68\xd4\x4d\x37\x2e\xbf\x7e\x98\x03\x7b\x99\
\xa2\xc0\x69\x36\x87\x33\x98\xa9\x79\x9e\x43\x74\xdf\xaf\xfc\xc5\
\xf1\x0c\x91\xaf\x09\x12\xb9\x3d\x64\x61\x24\xc9\xb5\x0b\x53\xbb\
\xf0\xe5\x35\x9a\x21\x61\x67\x96\x2e\x9c\xaa\xd2\x05\x47\xf1\x2d\
\x57\x3a\x34\xfd\x31\x70\x66\xa3\x31\x55\x70\xec\x03\xb1\xbb\x3e\
\x4e\x74\x67\x2d\x32\x0d\x50\xdf\x6c\x37\x12\xe2\x8c\x11\xea\x2e\
\x2a\x14\x31\xdd\xeb\xfb\xdd\x04\x66\x59\x6a\xb6\xcb\x2d\x3c\xd5\
\x0c\xc2\x56\xa9\xcb\xed\x66\xdc\x7a\x33\x33\xc4\x5e\x0c\xa3\x84\
\x58\x71\xf8\x81\x78\xb3\xd5\xa0\xe1\x2c\xcd\x18\xcd\x16\x11\x4b\
\xad\x4c\x1f\xdd\x1f\x86\x76\x9f\x9e\x00\x67\x70\x06\x96\xdf\x9b\
\x3c\x80\x6b\x72\xda\xa4\x04\x3b\x70\xb3\x19\x00\xb7\xd8\x71\x26\
\xf8\x10\x6e\xc7\x1a\xee\x3b\xe4\xd4\xa9\x11\x40\x1d\x41\x14\x2b\
\x59\xb0\xf7\xcb\xae\xa2\x89\xc6\xe0\x07\xda\x54\x04\xc6\x08\xb5\
\xab\x2f\x93\xac\xcf\x11\xc9\x14\xbc\xeb\xca\x82\xc4\x1d\x45\x5e\
\x71\x8c\x34\xc0\x94\xa0\xcf\x30\xa1\x59\xfa\x61\xbd\x11\x6c\x0a\
\xcb\x72\x30\x8c\x10\x63\xa1\x0c\x44\xb4\x60\x53\xa5\xa7\x3e\xbf\
\x3c\xde\x85\x6f\x68\xdc\x6f\xe2\x3e\xc9\x36\x7a\x27\x5d\x44\xa0\
\xb3\x34\x77\x7a\xa2\xdc\x53\x1c\xa6\x05\x8a\xb9\x97\xd8\x45\x16\
\x41\x1a\x92\x27\xfa\xcb\x38\x80\xd6\xf3\x78\x9f\x2f\x97\x8a\x20\
\xa5\x53\x28\x16\x1c\x0b\x79\x24\xc7\xea\xf7\xf7\x96\x9e\x11\xaa\
\x74\x8e\xf4\xd8\x7d\x25\x5c\xf3\x5b\x86\x11\x57\x32\xcb\xb6\x0f\
\x7d\x2a\x78\x9f\x5f\x6f\x7e\x89\x1f\x96\x0d\xe2\xc5\x8d\x83\xac\
\xf8\xd3\x2c\x69\x86\x71\x0f\x0e\x46\x41\xd8\xfc\xfa\x83\x8d\x46\
\x59\x6b\xd5\x8b\x12\x11\xa6\x0e\x4d\xb0\x24\x08\xa3\x12\xbe\x8d\
\xe3\x4e\x33\x64\x09\x13\xa6\xbe\xec\xeb\xf9\x73\xba\x15\x46\xbf\
\x8c\xcd\x7e\xfc\x34\x79\xf0\x6f\x1e\xdc\xc2\x3f\xbb\x05\x67\xbf\
\x88\x13\xea\x14\x2d\x71\xdb\x3e\xa7\x20\xd9\xc0\x48\x5c\xf3\x5d\
\xd8\xc6\x1a\x7d\x47\xb0\x04\x66\x20\xb1\xb1\xf8\x76\x7c\xc4\x83\
\x11\xb6\x38\x88\x32\xe9\x25\xfd\xc2\xb1\x05\xe0\x7f\x2f\x16\xee\
\xfb\xc7\xac\xb2\x6d\x4c\xfe\x3d\xaa\xf3\x65\x6c\xb4\xa2\xef\x4c\
\x16\x77\xfa\xc6\xb7\x8b\x97\x77\xca\x9f\x54\x13\x8d\x3a\x28\x87\
\x39\x31\x7f\xe3\x9a\xce\xe2\xce\x09\xff\x75\xf8\x07\xb9\xbb\xee\
\x56\x8b\xa2\x7c\xb3\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\
\x82\
"

qt_resource_name = b"\
\x00\x07\
\x07\x3b\xe0\xb3\
\x00\x70\
\x00\x6c\x00\x75\x00\x67\x00\x69\x00\x6e\x00\x73\
\x00\x0e\
\x0c\x18\xec\x3e\
\x00\x4a\
\x00\x61\x00\x70\x00\x61\x00\x6e\x00\x45\x00\x6c\x00\x65\x00\x76\x00\x61\x00\x74\x00\x69\x00\x6f\x00\x6e\
\x00\x08\
\x0a\x61\x5a\xa7\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x36\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x36\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x60\x25\xe4\x75\x44\
"

qt_version = QtCore.qVersion().split('.')
if qt_version < ['5', '8', '0']:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
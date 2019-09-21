@echo off
call "C:\ProgramFolder\QGIS30801\bin\o4w_env.bat"
call "C:\ProgramFolder\QGIS30801\bin\qt5_env.bat"
call "C:\ProgramFolder\QGIS30801\bin\py3_env.bat"

@echo on
pyrcc5 -o resources.py resources.qrc

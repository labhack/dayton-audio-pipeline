# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(626, 499)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.txtFilename = QtGui.QLineEdit(self.centralWidget)
        self.txtFilename.setGeometry(QtCore.QRect(50, 10, 401, 28))
        self.txtFilename.setObjectName(_fromUtf8("txtFilename"))
        self.btnFileBrowser = QtGui.QPushButton(self.centralWidget)
        self.btnFileBrowser.setGeometry(QtCore.QRect(460, 10, 85, 28))
        self.btnFileBrowser.setObjectName(_fromUtf8("btnFileBrowser"))
        self.btnPlayFile = QtGui.QPushButton(self.centralWidget)
        self.btnPlayFile.setGeometry(QtCore.QRect(90, 80, 85, 28))
        self.btnPlayFile.setObjectName(_fromUtf8("btnPlayFile"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 626, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio Pipeline", None))
        self.btnFileBrowser.setText(_translate("MainWindow", "Browse", None))
        self.btnPlayFile.setText(_translate("MainWindow", "Play File", None))


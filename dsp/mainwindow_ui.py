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
        MainWindow.resize(796, 499)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.txtFilename = QtGui.QLineEdit(self.centralWidget)
        self.txtFilename.setGeometry(QtCore.QRect(240, 10, 401, 28))
        self.txtFilename.setObjectName(_fromUtf8("txtFilename"))
        self.btnFileBrowser = QtGui.QPushButton(self.centralWidget)
        self.btnFileBrowser.setGeometry(QtCore.QRect(650, 10, 85, 28))
        self.btnFileBrowser.setObjectName(_fromUtf8("btnFileBrowser"))
        self.btnFilterFile = QtGui.QPushButton(self.centralWidget)
        self.btnFilterFile.setGeometry(QtCore.QRect(380, 160, 85, 28))
        self.btnFilterFile.setObjectName(_fromUtf8("btnFilterFile"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtOutputDir = QtGui.QLineEdit(self.centralWidget)
        self.txtOutputDir.setGeometry(QtCore.QRect(240, 50, 401, 28))
        self.txtOutputDir.setObjectName(_fromUtf8("txtOutputDir"))
        self.btnDirBrowser = QtGui.QPushButton(self.centralWidget)
        self.btnDirBrowser.setGeometry(QtCore.QRect(650, 50, 85, 28))
        self.btnDirBrowser.setObjectName(_fromUtf8("btnDirBrowser"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 131, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 121, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtOutputFilename = QtGui.QLineEdit(self.centralWidget)
        self.txtOutputFilename.setGeometry(QtCore.QRect(240, 90, 401, 28))
        self.txtOutputFilename.setObjectName(_fromUtf8("txtOutputFilename"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 796, 25))
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
        self.btnFilterFile.setText(_translate("MainWindow", "Filter File", None))
        self.label.setText(_translate("MainWindow", "Input File:", None))
        self.btnDirBrowser.setText(_translate("MainWindow", "Browse", None))
        self.label_2.setText(_translate("MainWindow", "Output Directory:", None))
        self.label_3.setText(_translate("MainWindow", "Output Filename:", None))


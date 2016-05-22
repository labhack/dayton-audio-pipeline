import sys
from PyQt4 import QtCore, QtGui
from top_block import top_block

from mainwindow_ui import Ui_MainWindow

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnFileBrowser, QtCore.SIGNAL("clicked()"), self.selectFile)
        QtCore.QObject.connect(self.ui.btnPlayFile, QtCore.SIGNAL("clicked()"), self.playFile)
        QtCore.QObject.connect(self, QtCore.SIGNAL("triggered()"), self.closeWindow)
                
    def selectFile(self):
        self.ui.txtFilename.setText(QtGui.QFileDialog.getOpenFileName())

    def closeWindow(self):
        try:
            tb.stop()
            tb.wait()
        except NameError:
            pass
            
    def playFile(self):
        tb = top_block()
        tb.start()
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

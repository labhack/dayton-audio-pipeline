import sys
import os.path
from PyQt4 import QtCore, QtGui
from top_block import top_block

from mainwindow_ui import Ui_MainWindow

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnFileBrowser, QtCore.SIGNAL("clicked()"), self.selectFile)
        QtCore.QObject.connect(self.ui.btnDirBrowser, QtCore.SIGNAL("clicked()"), self.selectDir)
        QtCore.QObject.connect(self.ui.btnFilterFile, QtCore.SIGNAL("clicked()"), self.playFile)
        QtCore.QObject.connect(self, QtCore.SIGNAL("triggered()"), self.closeWindow)
                
    def selectFile(self):
        self.input_file = QtGui.QFileDialog.getOpenFileName()
        self.ui.txtFilename.setText(self.input_file)

    def selectDir(self):
        self.output_dir = QtGui.QFileDialog.getExistingDirectory(self, 'Select Output Directory')
        self.ui.txtOutputDir.setText(self.output_dir)
        
    def closeWindow(self):
        try:
            tb.stop()
            tb.wait()
        except NameError:
            pass
            
    def playFile(self):
        if os.path.isfile(self.input_file) is not True:
            print("Path is not a file!")
            return
        tb = top_block()
        tb.set_input_file(self.input_file)
        tb.setup_blocks()
        tb.start()
        tb.wait()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

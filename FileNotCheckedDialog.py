from PyQt4 import QtGui, QtCore
 
class FileNotCheckedDialog(QtGui.QDialog):
    def __init__(self, fileNames):
        super(FileNotCheckedDialog, self).__init__()
        self.messageBrowser = QtGui.QTextBrowser(self)
        if len(fileNames) > 1:
            self.messageBrowser.append("Following files have not checked yet:")
        else:
            self.messageBrowser.append("Following file has not checked yet:")
        for fileName in fileNames:
            self.messageBrowser.append(fileName)
        self.messageBrowser.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.resize(500, 400)
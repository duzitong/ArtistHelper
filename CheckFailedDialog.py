from PyQt4 import QtGui, QtCore
 
class CheckFailedDialog(QtGui.QDialog):
    def __init__(self, message):
        super(CheckFailedDialog, self).__init__()
        self.messageBrowser = QtGui.QTextBrowser(self)
        self.messageBrowser.append(message)
        self.messageBrowser.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.resize(500, 400)
        
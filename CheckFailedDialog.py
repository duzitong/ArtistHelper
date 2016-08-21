from PyQt4 import QtGui, QtCore
import json
 
class CheckFailedDialog(QtGui.QDialog):
    def __init__(self, message):
        super(CheckFailedDialog, self).__init__()
        config = json.load(file("Config/DialogWindow.json"))
        self.messageBrowser = QtGui.QTextBrowser(self)
        self.messageBrowser.append(message)
        self.messageBrowser.setGeometry(QtCore.QRect(0, 0, config["Width"], config["Height"]))
        self.resize(config["Width"], config["Height"])
        
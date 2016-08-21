from PyQt4 import QtGui, QtCore
import json
 
class FileNotCheckedDialog(QtGui.QDialog):
    def __init__(self, fileNames):
        super(FileNotCheckedDialog, self).__init__()
        config = json.load(file("Config/DialogWindow.json"))
        self.messageBrowser = QtGui.QTextBrowser(self)
        if len(fileNames) > 1:
            self.messageBrowser.append("Following files have not checked yet:")
        else:
            self.messageBrowser.append("Following file has not checked yet:")
        for fileName in fileNames:
            self.messageBrowser.append("- " + fileName)
        self.messageBrowser.setGeometry(QtCore.QRect(0, 0, config["Width"], config["Height"]))
        self.resize(config["Width"], config["Height"])
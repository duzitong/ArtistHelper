# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArtistHelper.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Copier import Copier
from Checker import Checker
from CheckFailedDialog import *
from FileNotCheckedDialog import *
import json

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
        self.config = json.load(file("Config/MainWindow.json"))
        self.width = self.config["Width"]
        self.height = self.config["Height"]

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(self.width, self.height)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, self.width * 0.4, self.height))
        self.treeView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.fileModel = QtGui.QDirModel()
        self.treeView.setModel(self.fileModel)
        self.treeView.setRootIndex(self.fileModel.index(self.config["RootPath"]))
        self.treeView.doubleClicked.connect(self.addFile)

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(self.width * 0.85, self.height * 0.9, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.onCheck)

        self.tableView  = QtGui.QTableView (self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(self.width * 0.4, 0, self.width * 0.6, self.height * 0.85))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableModel = QtGui.QStandardItemModel(self.tableView)
        self.tableModel.setColumnCount(3)
        self.tableModel.setHeaderData(0, QtCore.Qt.Horizontal,_fromUtf8("Name"))
        self.tableModel.setHeaderData(1, QtCore.Qt.Horizontal,_fromUtf8("Folder"))
        self.tableModel.setHeaderData(2, QtCore.Qt.Horizontal,_fromUtf8("Modified"))
        self.tableView.setModel(self.tableModel)
        self.tableView.setColumnWidth(0, self.width * 0.2)
        self.tableView.setColumnWidth(1, self.width * 0.3)
        self.tableView.setColumnWidth(2, self.width * 0.08)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(self.width * 0.85, self.height * 0.95, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.onCopy)

        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(self.width * 0.45, self.height * 0.95, 75, 23))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        if self.config["PC"]:
            self.checkBox.setCheckState(QtCore.Qt.Checked)

        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(self.width * 0.55, self.height * 0.95, 75, 23))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        if self.config["IOS"]:
            self.checkBox_2.setCheckState(QtCore.Qt.Checked)

        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(self.width * 0.65, self.height * 0.95, 75, 23))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        if self.config["Android"]:
            self.checkBox_3.setCheckState(QtCore.Qt.Checked)


        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.initializeLogicComponents()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ArtistHelper", None))
        self.pushButton.setText(_translate("MainWindow", "Check", None))
        self.pushButton_2.setText(_translate("MainWindow", "Copy", None))
        self.checkBox.setText(_translate("MainWindow", "PC", None))
        self.checkBox_2.setText(_translate("MainWindow", "IOS", None))
        self.checkBox_3.setText(_translate("MainWindow", "Android", None))

    def onCheck(self):
        self.passed = [False for _ in range(self.tableModel.rowCount())]
        checked = [False for _ in range(self.tableModel.rowCount())]
        for cell in self.tableView.selectedIndexes():
            if not checked[cell.row()]:
                name = self.tableModel.item(cell.row()).text()
                path = self.tableModel.item(cell.row(), 1).text()
                isPassed, errorMessage = self.checker.check(path + "/" + name)
                if isPassed:
                    self.passed[cell.row()] = True
                else:
                    dialog = CheckFailedDialog(errorMessage)
                    dialog.exec_()
                checked[cell.row()] = True

    def onCopy(self):
        copied = [False for _ in range(self.tableModel.rowCount())]
        notPassedFiles = []
        for cell in self.tableView.selectedIndexes():
            if not copied[cell.row()]:
                name = self.tableModel.item(cell.row()).text()
                path = self.tableModel.item(cell.row(), 1).text()
                modified = self.tableModel.item(cell.row(), 2).text()
                fileName = path + "/" + name
                if cell.row() < len(self.passed) and self.passed[cell.row()] and \
                self.checker.isLatest(fileName, modified):
                    self.copier.copy(fileName,
                        self.checkBox.isChecked(),
                        self.checkBox_2.isChecked(),
                        self.checkBox_3.isChecked())
                else:
                    notPassedFiles.append(self.tableModel.item(cell.row()).text())
                copied[cell.row()] = True
        if len(notPassedFiles) > 0:
            dialog = FileNotCheckedDialog(notPassedFiles)
            dialog.exec_()

    def addFile(self, index):
        fileInfo = self.fileModel.fileInfo(index)
        if fileInfo.isFile():
            path = fileInfo.dir().path()
            name = fileInfo.fileName()
            modified = fileInfo.lastModified().toString("yyyy/MM/dd hh:mm:ss")
            # TODO: if name.endswith("json")
            self.tableModel.appendRow([QtGui.QStandardItem(name), 
                                       QtGui.QStandardItem(path),
                                       QtGui.QStandardItem(modified)])

    def initializeLogicComponents(self):
        self.copier = Copier()
        self.checker = Checker(self.config["AtlasPath"])
        self.passed = []

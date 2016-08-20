# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArtistHelper.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Copier import Copier
from Checker import Checker

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
        MainWindow.resize(530, 445)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 261, 431))
        self.treeView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.treeView.setObjectName(_fromUtf8("treeView"))

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(260, 0, 271, 431))
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))


        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(180, 370, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.OnCheck)

        self.listView_2 = QtGui.QListView(self.tab)
        self.listView_2.setGeometry(QtCore.QRect(0, 0, 271, 331))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))

        self.tabWidget.addTab(self.tab, _fromUtf8(""))


        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))

        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 370, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.OnCopy)

        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 340, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.checkBox_2 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 360, 71, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.checkBox_3 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 380, 71, 16))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))

        self.listView = QtGui.QListView(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(0, 0, 271, 331))
        self.listView.setObjectName(_fromUtf8("listView"))

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))


        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.initializeLogicComponents()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ArtistHelper", None))
        self.pushButton.setText(_translate("MainWindow", "Check", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Checker", None))
        self.pushButton_2.setText(_translate("MainWindow", "Copy", None))
        self.checkBox.setText(_translate("MainWindow", "PC", None))
        self.checkBox_2.setText(_translate("MainWindow", "IOS", None))
        self.checkBox_3.setText(_translate("MainWindow", "Android", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Copier", None))

    def OnCheck(self):
        print self.checker.check()

    def OnCopy(self):
        print self.copier.copy("",
        self.checkBox.isChecked(),
        self.checkBox_2.isChecked(),
        self.checkBox_3.isChecked())

    def initializeLogicComponents(self):
        self.copier = Copier()
        self.checker = Checker()


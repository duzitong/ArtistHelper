import ArtistHelperUI
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class UI(QWidget, ArtistHelperUI.Ui_MainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
ui = UI()
ui.show()
app.exec_()
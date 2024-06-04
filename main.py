from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pgms.indexLayout import Ui_MainWindow
import pandas as pd
import sys


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

        self.fileLoad.triggered.connect(self.loadfile)
    
    def loadfile(self):
        options = QFileDialog.Options()
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if self.filename.endswith(".xlsx"):
            self.file_contents = pd.ExcelFile(self.filename)
            self.sheets = self.file_contents.sheet_names
            print(self.sheets)
        else:
            self.show_warning_message_box("You Have Opened an Unknow file with Unknown sheets")
        
    
    def show_warning_message_box(self, msg):
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setWindowTitle("Warning")
        warning_box.setText(msg)
        warning_box.setStandardButtons(QMessageBox.Ok)
        warning_box.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    app.exec()
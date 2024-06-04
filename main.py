from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from pgms.indexLayout import Ui_MainWindow
from pgms.database import Database
import pandas as pd
import sys


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        
        # Config
        self.setQTableWidgetConfig()
        self.categoryExportAll.setIcon(QIcon("assets\\word.png"))
        self.categoryExport.setIcon(QIcon("assets\\word.png"))

        # Triggers
        self.fileLoad.triggered.connect(self.loadfile)
        self.deptcomboBox.currentTextChanged.connect(self.comboBoxChanged)
    
    def loadfile(self):
        options = QFileDialog.Options()
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if self.filename.endswith(".xlsx"):
            self.database = Database(self.filename)
            self.update_combo_box(self.database.file_content.sheet_names)
        else:
            self.show_warning_message_box("You Have Opened an Unknow file with Unknown sheets")
    
    # Widget Update Functions
    def update_combo_box(self, sheets):
        self.deptcomboBox.clear()
        for sheet in sheets:
            self.deptcomboBox.addItem(sheet)
    
    def comboBoxChanged(self, value):
        if value:
            self.database.update_table(value, self.maleValueTable, self.femaleValueTable)
    
    
    # Config Functions
    def setQTableWidgetConfig(self):
        self.maleValueTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.femaleValueTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.maleValueTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.maleValueTable.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.femaleValueTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.femaleValueTable.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    
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
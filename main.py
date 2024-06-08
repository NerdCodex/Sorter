from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from pgms.indexLayout import Ui_MainWindow
from pgms.database import Database
from pgms.export import CatagoryExporter
from docx import Document
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
        self.categoryExportAll.clicked.connect(self.exportall)
        self.categoryExport.clicked.connect(self.export)
    
    def loadfile(self):
        options = QFileDialog.Options()
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if self.filename.endswith(".xlsx"):
            self.database = Database(self.filename)
            self.sheet_names = self.database.file_content.sheet_names
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
    
    # Export Functions
    def exportall(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save Data", "", "Word Files (*.docx);;All Files (*)", options=options)
        if filename:
            document = Document()
            table_file = CatagoryExporter(document)
            
            table_file.add_heading("Male")
            male_table = table_file.create_table()
            for index, sheet in enumerate(self.sheet_names):
                table_file.insert_data(self.database.maleDataExporter(sheet, index+1), male_table)
            
            table_file.add_heading("\nFemale")
            female_table = table_file.create_table()
            for index, sheet in enumerate(self.sheet_names):
                table_file.insert_data(self.database.femaleDataExporter(sheet, index+1), female_table)
            document.save(filename)
        
    def export(self):
        current_sheet_name = self.deptcomboBox.currentText()
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save Data", "", "Word Files (*.docx);;All Files (*)", options=options)
        if filename:
            document = Document()
            table_file = CatagoryExporter(document)

            table_file.add_heading("Male")
            male_table = table_file.create_table()
            table_file.insert_data(self.database.maleDataExporter(current_sheet_name, 1), male_table)

            table_file.add_heading("\nFemale")
            female_table = table_file.create_table()
            table_file.insert_data(self.database.femaleDataExporter(current_sheet_name, 1), female_table)
            document.save(filename)
            
        

            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    app.exec()
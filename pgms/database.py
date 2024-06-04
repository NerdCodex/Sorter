import pandas as pd
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class Caste:
    def __init__(self):
        self.oc = 0
        self.sc = 0
        self.st = 0
        self.others = 0
    
    def loadCaste(self, content):
        self.oc = len(content.query('Caste == "OC"').to_numpy().tolist())
        self.sc = len(content.query('Caste == "SC"').to_numpy().tolist())
        self.st = len(content.query('Caste == "ST"').to_numpy().tolist())
        self.others = len(content.query('Caste == "BC"').to_numpy().tolist())
    
class Religion:
    def __init__(self):
        self.hindu = Caste()
        self.christian = Caste()
        self.muslim = Caste()
    
    def loadReligion(self, content):
        self.hindu.loadCaste(content.query('Religion == "Hindu"'))
        self.christian.loadCaste(content.query('Religion == "Christian"'))
        self.muslim.loadCaste(content.query('Religion == "Muslim"'))

class Gender:
    def __init__(self):
        self.male = Religion()
        self.female = Religion()
    
    def loadGender(self, content):
        self.male.loadReligion(content.query('Gender == "Male"'))
        self.female.loadReligion(content.query('Gender == "Female"'))


class Department:
    def __init__(self, sheets, content):
        self.departments = {}
        self.content = content
        self.sheets = sheets
        for sheet in sheets:
            self.departments[sheet] = Gender()
        self.loadDepartment()
    
    def loadDepartment(self):
        for sheet in self.sheets:
            self.departments[sheet].loadGender(self.content.parse(sheet))
        
class CategorySort:
    def __init__(self, fileContent):
        self.fileContent = fileContent
        self.department = Department(self.fileContent.sheet_names, fileContent)

class Database:
    def __init__(self, filename:str):
        self.file_content = pd.ExcelFile(filename)
        self.category_sort = CategorySort(self.file_content)
    
    def update_table(self, dept, maleTable:QTableWidget, femaleTable:QTableWidget):
        # Male Hindu
        maleTable.setItem(0, 0, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.hindu.oc)))
        maleTable.setItem(0, 1, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.hindu.sc)))
        maleTable.setItem(0, 2, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.hindu.st)))
        maleTable.setItem(0, 3, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.hindu.others)))

        # Male Christian
        maleTable.setItem(1, 0, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.christian.oc)))
        maleTable.setItem(1, 1, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.christian.sc)))
        maleTable.setItem(1, 2, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.christian.st)))
        maleTable.setItem(1, 3, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.christian.others)))

        # Male Muslim
        maleTable.setItem(2, 0, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.muslim.oc)))
        maleTable.setItem(2, 1, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.muslim.sc)))
        maleTable.setItem(2, 2, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.muslim.st)))
        maleTable.setItem(2, 3, QTableWidgetItem(str(self.category_sort.department.departments[dept].male.muslim.others)))

        # Female Hindu
        femaleTable.setItem(0, 0, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.hindu.oc)))
        femaleTable.setItem(0, 1, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.hindu.sc)))
        femaleTable.setItem(0, 2, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.hindu.st)))
        femaleTable.setItem(0, 3, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.hindu.others)))

        # Female Christian
        femaleTable.setItem(1, 0, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.christian.oc)))
        femaleTable.setItem(1, 1, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.christian.sc)))
        femaleTable.setItem(1, 2, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.christian.st)))
        femaleTable.setItem(1, 3, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.christian.others)))

        # Female Muslim
        femaleTable.setItem(2, 0, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.muslim.oc)))
        femaleTable.setItem(2, 1, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.muslim.sc)))
        femaleTable.setItem(2, 2, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.muslim.st)))
        femaleTable.setItem(2, 3, QTableWidgetItem(str(self.category_sort.department.departments[dept].female.muslim.others)))

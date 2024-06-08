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
    
    def exportCaste(self):
        return [self.oc, self.sc, self.st, self.others]
    
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

    def maleDataExporter(self, sheet_name, index):

        hindu = [index, sheet_name, "Hindu"]
        christian = [index, sheet_name, "Christian"]
        muslim = [index, sheet_name, "Muslim"]

        hindu.extend(self.category_sort.department.departments[sheet_name].male.hindu.exportCaste())
        christian.extend(self.category_sort.department.departments[sheet_name].male.christian.exportCaste())
        muslim.extend(self.category_sort.department.departments[sheet_name].male.muslim.exportCaste())

        return [hindu, christian, muslim]
    
    def femaleDataExporter(self, sheet_name, index):

        hindu = [index, sheet_name, "Hindu"]
        christian = [index, sheet_name, "Christian"]
        muslim = [index, sheet_name, "Muslim"]

        hindu.extend(self.category_sort.department.departments[sheet_name].female.hindu.exportCaste())
        christian.extend(self.category_sort.department.departments[sheet_name].female.christian.exportCaste())
        muslim.extend(self.category_sort.department.departments[sheet_name].female.muslim.exportCaste())

        return [hindu, christian, muslim]

    
    
    def update_table(self, dept, maleTable:QTableWidget, femaleTable:QTableWidget):
        # Male
        hindu = self.category_sort.department.departments[dept].male.hindu.exportCaste()
        christian = self.category_sort.department.departments[dept].male.christian.exportCaste()
        muslim = self.category_sort.department.departments[dept].male.muslim.exportCaste()

        for x , religion in enumerate([hindu, christian, muslim]):
            for y, value in enumerate(religion):
                maleTable.setItem(x, y, QTableWidgetItem(str(value)))

        # Female
        hindu = self.category_sort.department.departments[dept].female.hindu.exportCaste()
        christian = self.category_sort.department.departments[dept].female.christian.exportCaste()
        muslim = self.category_sort.department.departments[dept].female.muslim.exportCaste()

        for x , religion in enumerate([hindu, christian, muslim]):
            for y, value in enumerate(religion):
                femaleTable.setItem(x, y, QTableWidgetItem(str(value)))

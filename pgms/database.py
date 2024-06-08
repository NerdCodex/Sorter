import pandas as pd
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox

class AwardedTime:
    def __init__(self):
        self.part_time = 0
        self.full_time = 0
    
    def loadTime(self, content):
        self.part_time = len(content.query('`P.T / F.T` == "Part-Time"').to_numpy().tolist())
        self.full_time = len(content.query('`P.T / F.T` == "Full-Time"').to_numpy().tolist())
    
    def getTime(self):
        return [self.part_time, self.full_time]
    
    def __add__(self, object):
        temp = AwardedTime()
        temp.part_time = self.part_time + object.part_time
        temp.full_time = self.full_time + object.full_time
        return temp

class AwardedGender:
    def __init__(self):
        self.male = AwardedTime()
        self.female = AwardedTime()
    
    def loadGender(self, content):
        self.male.loadTime(content.query('Gender == "Male"'))
        self.female.loadTime(content.query('Gender == "Female"'))
    
    def genderExport(self):
        male = self.male.getTime()
        female = self.female.getTime()
        total = male[0] + male[1] + female[1] + female[0]
        male.append(total)
        female.append(total)
        return [male, female]

class AwardedYear:
    def __init__(self, years):
        self.years = {}
        self.years_list = years
        for year in years:
            self.years[year] = AwardedGender()
    
    def loadAwardedYear(self, content):
        content['Commencement Date'] = pd.to_datetime(content['Commencement Date'])
        for year in self.years_list:
            self.years[year].loadGender(content.query(f'Status == "Awarded" and `Commencement Date`.dt.year == {year}'))

class AwardedDepartment:
    def __init__(self, sheets, content):
        self.departments = {}
        self.content = content
        self.sheets = sheets
        for sheet in sheets:
            year = self.getYears(self.content.parse(sheet)["Commencement Date"].to_list())
            self.departments[sheet] = AwardedYear(year)
        self.loadDepartment()
    
    def loadDepartment(self):
        for sheet in self.sheets:
            current_content = self.content.parse(sheet)
            self.departments[sheet].loadAwardedYear(current_content)
    
    def getYears(self, timestamps):
        years = []
        for timestamp in timestamps:
            if pd.notna(timestamp):
                years.append(timestamp.year)
        return list(set(years))

class AwardedSort:
    def __init__(self, fileContent):
        self.fileContent = fileContent
        self.awardedList = AwardedDepartment(self.fileContent.sheet_names, fileContent)


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
    
    def exportReligion(self):
        return [self.hindu.exportCaste(), self.christian.exportCaste(), self.muslim.exportCaste()]

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
        self.awarded_sort = AwardedSort(self.file_content)

    def maleCategoryDataExporter(self, sheet_name, index):

        hindu = [index, sheet_name, "Hindu"]
        christian = [index, sheet_name, "Christian"]
        muslim = [index, sheet_name, "Muslim"]

        religion = self.category_sort.department.departments[sheet_name].male.exportReligion()

        hindu.extend(religion[0])
        christian.extend(religion[1])
        muslim.extend(religion[2])

        return [hindu, christian, muslim]
    
    def femaleCategoryDataExporter(self, sheet_name, index):

        hindu = [index, sheet_name, "Hindu"]
        christian = [index, sheet_name, "Christian"]
        muslim = [index, sheet_name, "Muslim"]

        religion = self.category_sort.department.departments[sheet_name].female.exportReligion()

        hindu.extend(religion[0])
        christian.extend(religion[1])
        muslim.extend(religion[2])

        return [hindu, christian, muslim]
    
    def awardedExporter(self, sheet_name, year, index):
        male = [index, year, "Male"]
        female = [index, year, "Female"]

        Genders = self.awarded_sort.awardedList.departments[sheet_name].years[year].genderExport()

        male.extend(Genders[0])
        female.extend(Genders[1])
        
        return [male, female]
        
    
    def update_male_female_table(self, dept, maleTable:QTableWidget, femaleTable:QTableWidget):
        # Male
        for x , religion in enumerate(self.category_sort.department.departments[dept].male.exportReligion()):
            for y, value in enumerate(religion):
                maleTable.setItem(x, y, QTableWidgetItem(str(value)))

        # Female
        for x , religion in enumerate(self.category_sort.department.departments[dept].female.exportReligion()):
            for y, value in enumerate(religion):
                femaleTable.setItem(x, y, QTableWidgetItem(str(value)))
    
    def update_awarded_table(self, value, table:QTableWidget, start_year, end_year):
        maleTime = AwardedTime()
        femaleTime = AwardedTime()
        if start_year == end_year:
            maleTime = self.awarded_sort.awardedList.departments[value].years[start_year].male
            femaleTime = self.awarded_sort.awardedList.departments[value].years[start_year].female

        elif start_year < end_year:
            years_list = self.awarded_sort.awardedList.departments[value].years_list
            try:
                for year in range(start_year, end_year+1):
                    if year in years_list:
                        maleTime = maleTime + self.awarded_sort.awardedList.departments[value].years[year].male
                        femaleTime = femaleTime + self.awarded_sort.awardedList.departments[value].years[year].female
            except KeyError:
                print("Not Found")

        elif start_year > end_year:
            warning_box = QMessageBox()
            warning_box.setIcon(QMessageBox.Warning)
            warning_box.setWindowTitle("Warning")
            warning_box.setText(f"Starting Year {start_year} is greater than ending year {end_year}")
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.exec_()

        for x, gender in enumerate([maleTime, femaleTime]):
            for y, time in enumerate(gender.getTime()):
                table.setItem(x,y,QTableWidgetItem(str(time)))

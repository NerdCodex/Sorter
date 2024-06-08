# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 800)
        MainWindow.setMinimumSize(QtCore.QSize(630, 800))
        MainWindow.setMaximumSize(QtCore.QSize(630, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.categorysortbox = QtWidgets.QGroupBox(self.centralwidget)
        self.categorysortbox.setGeometry(QtCore.QRect(10, 0, 611, 371))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.categorysortbox.setFont(font)
        self.categorysortbox.setStyleSheet("GroupBox {\n"
"    font: 75 11pt \"Book Antiqua\";\n"
"}")
        self.categorysortbox.setObjectName("categorysortbox")
        self.deptcomboBox = QtWidgets.QComboBox(self.categorysortbox)
        self.deptcomboBox.setGeometry(QtCore.QRect(130, 30, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.deptcomboBox.setFont(font)
        self.deptcomboBox.setObjectName("deptcomboBox")
        self.label = QtWidgets.QLabel(self.categorysortbox)
        self.label.setGeometry(QtCore.QRect(10, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.maleFemaleTab = QtWidgets.QTabWidget(self.categorysortbox)
        self.maleFemaleTab.setGeometry(QtCore.QRect(10, 80, 591, 191))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.maleFemaleTab.setFont(font)
        self.maleFemaleTab.setStyleSheet("QTabBar::tab:hover { \n"
"    background: #D6D6D6; \n"
"    color: #000; \n"
"}\n"
"\n"
"QTabBar::tab:selected { \n"
"    background: #FFFFFF;  \n"
"}")
        self.maleFemaleTab.setObjectName("maleFemaleTab")
        self.maleTab = QtWidgets.QWidget()
        self.maleTab.setObjectName("maleTab")
        self.maleValueTable = QtWidgets.QTableWidget(self.maleTab)
        self.maleValueTable.setGeometry(QtCore.QRect(0, 0, 581, 151))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        self.maleValueTable.setFont(font)
        self.maleValueTable.setStyleSheet("QTableWidget {\n"
"    border: 2px solid black;\n"
"}")
        self.maleValueTable.setObjectName("maleValueTable")
        self.maleValueTable.setColumnCount(4)
        self.maleValueTable.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.maleValueTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.maleValueTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.maleValueTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.maleValueTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.maleValueTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.maleValueTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.maleValueTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.maleValueTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        item.setFont(font)
        self.maleValueTable.setItem(1, 3, item)
        self.maleFemaleTab.addTab(self.maleTab, "")
        self.femaleTab = QtWidgets.QWidget()
        self.femaleTab.setObjectName("femaleTab")
        self.femaleValueTable = QtWidgets.QTableWidget(self.femaleTab)
        self.femaleValueTable.setGeometry(QtCore.QRect(0, 0, 581, 151))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        self.femaleValueTable.setFont(font)
        self.femaleValueTable.setStyleSheet("QTableWidget {\n"
"    border: 2px solid black;\n"
"}")
        self.femaleValueTable.setObjectName("femaleValueTable")
        self.femaleValueTable.setColumnCount(4)
        self.femaleValueTable.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.femaleValueTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.femaleValueTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.femaleValueTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.femaleValueTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.femaleValueTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.femaleValueTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.femaleValueTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.femaleValueTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        item.setFont(font)
        self.femaleValueTable.setItem(1, 3, item)
        self.maleFemaleTab.addTab(self.femaleTab, "")
        self.categoryExportAll = QtWidgets.QPushButton(self.categorysortbox)
        self.categoryExportAll.setGeometry(QtCore.QRect(90, 290, 151, 41))
        self.categoryExportAll.setStyleSheet("")
        self.categoryExportAll.setObjectName("categoryExportAll")
        self.categoryExport = QtWidgets.QPushButton(self.categorysortbox)
        self.categoryExport.setGeometry(QtCore.QRect(340, 290, 151, 41))
        self.categoryExport.setStyleSheet("")
        self.categoryExport.setObjectName("categoryExport")
        self.awardedSortGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.awardedSortGroupBox.setGeometry(QtCore.QRect(10, 370, 611, 371))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.awardedSortGroupBox.setFont(font)
        self.awardedSortGroupBox.setStyleSheet("GroupBox {\n"
"    font: 75 11pt \"Book Antiqua\";\n"
"}")
        self.awardedSortGroupBox.setObjectName("awardedSortGroupBox")
        self.awardedDeptComboBox = QtWidgets.QComboBox(self.awardedSortGroupBox)
        self.awardedDeptComboBox.setGeometry(QtCore.QRect(140, 40, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.awardedDeptComboBox.setFont(font)
        self.awardedDeptComboBox.setObjectName("awardedDeptComboBox")
        self.label_2 = QtWidgets.QLabel(self.awardedSortGroupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.awardedValueTable = QtWidgets.QTableWidget(self.awardedSortGroupBox)
        self.awardedValueTable.setGeometry(QtCore.QRect(10, 140, 591, 151))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        self.awardedValueTable.setFont(font)
        self.awardedValueTable.setStyleSheet("QTableWidget {\n"
"    border: 2px solid black;\n"
"}")
        self.awardedValueTable.setObjectName("awardedValueTable")
        self.awardedValueTable.setColumnCount(2)
        self.awardedValueTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.awardedValueTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.awardedValueTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.awardedValueTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.awardedValueTable.setHorizontalHeaderItem(1, item)
        self.startYearComboBox = QtWidgets.QComboBox(self.awardedSortGroupBox)
        self.startYearComboBox.setGeometry(QtCore.QRect(140, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startYearComboBox.setFont(font)
        self.startYearComboBox.setObjectName("startYearComboBox")
        self.year = QtWidgets.QLabel(self.awardedSortGroupBox)
        self.year.setGeometry(QtCore.QRect(20, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.year.setFont(font)
        self.year.setObjectName("year")
        self.endYearComboBox = QtWidgets.QComboBox(self.awardedSortGroupBox)
        self.endYearComboBox.setGeometry(QtCore.QRect(420, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.endYearComboBox.setFont(font)
        self.endYearComboBox.setObjectName("endYearComboBox")
        self.year_2 = QtWidgets.QLabel(self.awardedSortGroupBox)
        self.year_2.setGeometry(QtCore.QRect(300, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.year_2.setFont(font)
        self.year_2.setObjectName("year_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileLoad = QtWidgets.QAction(MainWindow)
        self.fileLoad.setObjectName("fileLoad")
        self.menuFile.addAction(self.fileLoad)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.maleFemaleTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sorter"))
        self.categorysortbox.setTitle(_translate("MainWindow", "Category-Sort"))
        self.label.setText(_translate("MainWindow", "Department"))
        item = self.maleValueTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hindu"))
        item = self.maleValueTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Christian"))
        item = self.maleValueTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Muslim"))
        item = self.maleValueTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "OC"))
        item = self.maleValueTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SC"))
        item = self.maleValueTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ST"))
        item = self.maleValueTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MBC/ONC/BC"))
        __sortingEnabled = self.maleValueTable.isSortingEnabled()
        self.maleValueTable.setSortingEnabled(False)
        self.maleValueTable.setSortingEnabled(__sortingEnabled)
        self.maleFemaleTab.setTabText(self.maleFemaleTab.indexOf(self.maleTab), _translate("MainWindow", "Male"))
        item = self.femaleValueTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hindu"))
        item = self.femaleValueTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Christian"))
        item = self.femaleValueTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Muslim"))
        item = self.femaleValueTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "OC"))
        item = self.femaleValueTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SC"))
        item = self.femaleValueTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ST"))
        item = self.femaleValueTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MBC/ONC/BC"))
        __sortingEnabled = self.femaleValueTable.isSortingEnabled()
        self.femaleValueTable.setSortingEnabled(False)
        self.femaleValueTable.setSortingEnabled(__sortingEnabled)
        self.maleFemaleTab.setTabText(self.maleFemaleTab.indexOf(self.femaleTab), _translate("MainWindow", "Female"))
        self.categoryExportAll.setText(_translate("MainWindow", "Export All"))
        self.categoryExport.setText(_translate("MainWindow", "Export"))
        self.awardedSortGroupBox.setTitle(_translate("MainWindow", "Awarded-Sort"))
        self.label_2.setText(_translate("MainWindow", "Department"))
        item = self.awardedValueTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Male"))
        item = self.awardedValueTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Female"))
        item = self.awardedValueTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Part-Time"))
        item = self.awardedValueTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Full-Time"))
        self.year.setText(_translate("MainWindow", "Starting Year"))
        self.year_2.setText(_translate("MainWindow", "Ending Year"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.fileLoad.setText(_translate("MainWindow", "Load"))

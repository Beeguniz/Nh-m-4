# Form implementation generated from reading ui file 'd:\Python\Bai tap\LapTrinhHDT\GUI\grammar14.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2362, 1043)
        MainWindow.setStyleSheet("background-color: rgb(255, 248, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.w1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.w1.setGeometry(QtCore.QRect(0, 0, 1011, 1091))
        self.w1.setStyleSheet("border-image:url(:/den/0jbd5157czr1712220724642.jpg);\n"
"")
        self.w1.setObjectName("w1")
        self.w2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.w2.setGeometry(QtCore.QRect(990, 0, 1920, 1080))
        self.w2.setStyleSheet("background-color: rgb(254, 205, 255)")
        self.w2.setObjectName("w2")
        self.ex14 = QtWidgets.QPushButton(parent=self.w2)
        self.ex14.setGeometry(QtCore.QRect(300, 660, 321, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ex14.setFont(font)
        self.ex14.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    background-color: rgb(255, 124, 174);\n"
"    border-radius: 50px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(255, 0, 127); \n"
"}\n"
"")
        self.ex14.setFlat(True)
        self.ex14.setObjectName("ex14")
        self.gra14 = QtWidgets.QPushButton(parent=self.w2)
        self.gra14.setEnabled(True)
        self.gra14.setGeometry(QtCore.QRect(300, 340, 321, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gra14.setFont(font)
        self.gra14.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    background-color: rgb(255, 124, 174);\n"
"    border-radius: 50px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(255, 0, 127); \n"
"}\n"
"")
        self.gra14.setAutoDefault(False)
        self.gra14.setDefault(False)
        self.gra14.setFlat(True)
        self.gra14.setObjectName("gra14")
        self.label = QtWidgets.QLabel(parent=self.w2)
        self.label.setGeometry(QtCore.QRect(740, 0, 201, 91))
        self.label.setStyleSheet("image: url(:/logo/62264bc2694c9812c15d.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.back_home14 = QtWidgets.QPushButton(parent=self.w2)
        self.back_home14.setGeometry(QtCore.QRect(40, 920, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_home14.setFont(font)
        self.back_home14.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    background-color: rgb(255, 124, 174);\n"
"    border-radius: 25px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(255, 0, 127); \n"
"}\n"
"\n"
"")
        self.back_home14.setObjectName("back_home14")
        self.w2.raise_()
        self.w1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home"))
        self.ex14.setText(_translate("MainWindow", "EXERCISES"))
        self.gra14.setText(_translate("MainWindow", "GRAMMAR"))
        self.back_home14.setText(_translate("MainWindow", "Back"))

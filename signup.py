from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Signup(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("QPushButton#loginbt{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgb(255, 204, 229));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#loginbt:hover{\n"
"background-color: rgb(255,243,255);\n"
"color: black;\n"
"}\n"
"QPushButton#loginbt:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color: rgba(150,123,111,255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet("image: url(:/images/img.jpg);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 431, 601))
        self.label_2.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.loginweb = QtWidgets.QLabel(self.widget)
        self.loginweb.setGeometry(QtCore.QRect(290, 230, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.loginweb.setFont(font)
        self.loginweb.setStyleSheet("background-color:white;\n"
"color:rgb(255,204,229);")
        self.loginweb.setObjectName("dangki")
        self.user_input = QtWidgets.QLineEdit(self.widget)
        self.user_input.setGeometry(QtCore.QRect(230, 360, 321, 31))
        self.user_input.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.user_input.setObjectName("user_input")
        self.pass_input = QtWidgets.QLineEdit(self.widget)
        self.pass_input.setGeometry(QtCore.QRect(230, 540, 321, 31))
        self.pass_input.setStyleSheet("background-color: white;\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.pass_input.setObjectName("pass_input")
        self.signup = QtWidgets.QPushButton(self.widget)
        self.signup.setGeometry(QtCore.QRect(300, 630, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setObjectName("signup")
        self.fullname_inp = QtWidgets.QLineEdit(self.widget)
        self.fullname_inp.setGeometry(QtCore.QRect(230, 420, 321, 31))
        self.fullname_inp.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.fullname_inp.setObjectName("fullname_inp")
        self.email_inp = QtWidgets.QLineEdit(self.widget)
        self.email_inp.setGeometry(QtCore.QRect(230, 480, 321, 31))
        self.email_inp.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.email_inp.setObjectName("email_inp")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(350, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginweb.setText(_translate("MainWindow", "Dokugaku"))
        self.user_input.setPlaceholderText(_translate("MainWindow", "Username"))
        self.pass_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signup.setText(_translate("MainWindow", "S i g n  U p"))
        self.fullname_inp.setPlaceholderText(_translate("MainWindow", "Fullname"))
        self.email_inp.setPlaceholderText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Sign up"))
        
    

import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_Signup()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
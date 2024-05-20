from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import home, grammar11, grammar12, grammar13, grammar14, exercises, exercises12, exercises13, exercises14, complete11, complete12, complete13, complete14, topic6lesson11, topic6lesson12, topic7lesson13, topic7lesson14, login, signup
from PyQt5.QtWidgets import QMessageBox

try:
    with open('user_data.txt', 'x') as file:
        pass
except FileExistsError:
    pass

ui = None
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.b_topic11.clicked.connect(grammar11Ui)
    ui.b_topic12.clicked.connect(grammar12Ui)
    ui.b_topic13.clicked.connect(grammar13Ui)
    ui.b_topic14.clicked.connect(grammar14Ui)
    MainWindow.show()

def grammar11Ui():
    global ui
    ui = grammar11.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.gra11.clicked.connect(Lesson11Ui)
    ui.ex11.clicked.connect(exercises11Ui)
    ui.back_home11.clicked.connect(homeUi)
    MainWindow.show()

def grammar12Ui():
    global ui
    ui = grammar12.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.gra12.clicked.connect(Lesson12Ui)
    ui.ex12.clicked.connect(exercises12Ui)
    ui.back_home12.clicked.connect(homeUi)
    MainWindow.show()

def grammar13Ui():
    global ui
    ui = grammar13.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.gra13.clicked.connect(Lesson13Ui)
    ui.ex13.clicked.connect(exercises13Ui)
    ui.back_home13.clicked.connect(homeUi)
    MainWindow.show()

def grammar14Ui():
    global ui
    ui = grammar14.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.gra14.clicked.connect(Lesson14Ui)
    ui.ex14.clicked.connect(exercises14Ui)
    ui.back_home14.clicked.connect(homeUi)
    MainWindow.show()

def exercises11Ui():
    global ui
    ui = exercises.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.nextp2_11.clicked.connect(complete11Ui)
    ui.back_gr11.clicked.connect(grammar11Ui)
    MainWindow.show()

def exercises12Ui():
    global ui
    ui = exercises12.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.nextp2_12.clicked.connect(complete12Ui)
    ui.back_gr12.clicked.connect(grammar12Ui)
    MainWindow.show()

def exercises13Ui():
    global ui
    ui = exercises13.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.nextp2_13.clicked.connect(complete13Ui)
    ui.back_gr13.clicked.connect(grammar13Ui)
    MainWindow.show()

def exercises14Ui():
    global ui
    ui = exercises14.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.nextp2_14.clicked.connect(complete14Ui)
    ui.back_gr14.clicked.connect(grammar14Ui)
    MainWindow.show()

def complete11Ui():
    global ui
    ui = complete11.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back_ex11.clicked.connect(exercises11Ui)
    MainWindow.show()

def complete12Ui():
    global ui
    ui = complete12.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back_ex12.clicked.connect(exercises12Ui)
    MainWindow.show()

def complete13Ui():
    global ui
    ui = complete13.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back_ex13.clicked.connect(exercises13Ui)
    MainWindow.show()

def complete14Ui():
    global ui
    ui = complete14.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back_ex14.clicked.connect(exercises14Ui)
    MainWindow.show()

def Lesson11Ui():
    global ui
    ui = topic6lesson11.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back1.clicked.connect(grammar11Ui)
    MainWindow.show()

def Lesson12Ui():
    global ui
    ui = topic6lesson12.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back2.clicked.connect(grammar12Ui)
    MainWindow.show()

def Lesson13Ui():
    global ui
    ui = topic7lesson13.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back1.clicked.connect(grammar13Ui)
    MainWindow.show()

def Lesson14Ui():
    global ui
    ui = topic7lesson14.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back1.clicked.connect(grammar14Ui)
    MainWindow.show()

def LoginUi():
    global ui
    ui = login.Ui_Signin()
    ui.setupUi(MainWindow)
    ui.signup_bt.clicked.connect(SignUpUi)
    ui.loginbt.clicked.connect(signinUi)
    MainWindow.show()

def SignUpUi():
    global ui
    ui = signup.Ui_Signup()
    ui.setupUi(MainWindow)
    ui.signup.clicked.connect(signupUser)
    MainWindow.show()

def signinUi():
    global ui
    un = ui.user_input.text()
    psw = ui.pass_input.text()

    try:
        with open('user_data.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        with open('user_data.txt', 'w') as file:
            QtWidgets.QMessageBox.information(None, "Dokugaku", "User data file created. Please sign up first.")
        return

    for line in lines:
        data = line.strip().split(',')
        if len(data) == 2 and data[0] == un and data[1] == psw:
            QMessageBox.information(None, "Dokugaku", "Đăng nhập thành công!")
            homeUi()
            return

    QMessageBox.information(None, "Dokugaku", "Đăng nhập thất bại!")

def signupUser():
    global ui
    un = ui.user_input.text()
    fn = ui.fullname_inp.text()
    em = ui.email_inp.text()
    psw = ui.pass_input.text()

    if un == '' or fn == '' or em == '' or psw == '':
        QtWidgets.QMessageBox.information(None, "Sign up output", "Vui lòng điền đầy đủ thông tin!") 
    else:
        try:
            with open('user_data.txt', 'r+') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    if len(data) > 0 and data[0] == un:
                        QtWidgets.QMessageBox.information(None, "Dokugaku", "Tài khoản đã tồn tại") 
                        return

                file.write(f"{un},{psw}\n")
                QtWidgets.QMessageBox.information(None, "Dokugaku", "Đăng kí thành công!")
                LoginUi()
        except FileNotFoundError:
            with open('user_data.txt', 'w') as file:
                file.write(f"{un},{psw}\n")
                QtWidgets.QMessageBox.information(None, "Dokugaku", "Đăng kí thành công!")
                LoginUi()

LoginUi()

sys.exit(app.exec())

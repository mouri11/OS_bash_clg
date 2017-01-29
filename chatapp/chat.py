# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys,socket
from thread import *

    def app_version():
        msg_box("Application Version","P2P Chat v1.0(By Rohit Das)")

    def msg_box(title,data):
        w= QWidget()
        QMessageBox.information(w,title,data)

    def update_list(self,data):
        self.listWidget.addItem(data)
        print "\a"

    def server_socket(self): #simply sets up the socket, binds, listens and accept incoming messages and connections
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.bind(('',6190))
            s.listen(1)
        except socket.error, e:
            msg_box("Socket Error!!", "Unable To Setup Local Socket. Port In Use ")
            return

        while 1:
            conn, addr=s.accept()

            incoming_ip=str(addr[0])
            current_chat_ip=self.lineEdit.text()

            if incoming_ip=self.lineEdit.text()
                conn.close()
            else:
                data=conn.recv(4096)
                update_list(self,data)
                conn.close()
        s.close()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(734, 528)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 721, 61))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 16, 241, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 41, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 16, 251, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 311, 381))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 291, 311))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 330, 121, 37))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 330, 101, 37))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(330, 70, 401, 381))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.listWidget = QtGui.QListWidget(self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 361))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu_Actions = QtGui.QMenu(self.menubar)
        self.menuMenu_Actions.setObjectName(_fromUtf8("menuMenu_Actions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersino = QtGui.QAction(MainWindow)
        self.actionVersino.setObjectName(_fromUtf8("actionVersino"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuMenu_Actions.addAction(self.actionVersino)
        self.menuMenu_Actions.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu_Actions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "IP Address:", None))
        self.label_2.setText(_translate("MainWindow", "User:", None))
        self.pushButton_3.setText(_translate("MainWindow", "Send Message", None))
        self.pushButton_4.setText(_translate("MainWindow", "Clear Logs", None))
        self.menuMenu_Actions.setTitle(_translate("MainWindow", "Menu Actions", None))
        self.actionVersino.setText(_translate("MainWindow", "Version", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

    def start_server(self): #calls a function called server_socket and passes the parameter self to it
        start_new_thread(server_docket,(self,))
        msg_box("Success","Server Started Succeddfully")
        self.pushButton.setEnabled(False)

    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


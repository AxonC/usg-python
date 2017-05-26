# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("usgfavicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.grpMain = QtWidgets.QGroupBox(Dialog)
        self.grpMain.setGeometry(QtCore.QRect(10, 10, 391, 221))
        self.grpMain.setObjectName("grpMain")
        self.txtMessage = QtWidgets.QTextEdit(self.grpMain)
        self.txtMessage.setGeometry(QtCore.QRect(10, 50, 371, 131))
        self.txtMessage.setObjectName("txtMessage")
        self.lblMessage = QtWidgets.QLabel(self.grpMain)
        self.lblMessage.setGeometry(QtCore.QRect(10, 23, 47, 13))
        self.lblMessage.setObjectName("lblMessage")
        self.cboChat = QtWidgets.QComboBox(self.grpMain)
        self.cboChat.setGeometry(QtCore.QRect(200, 20, 181, 22))
        self.cboChat.setObjectName("cboChat")
        self.label = QtWidgets.QLabel(self.grpMain)
        self.label.setGeometry(QtCore.QRect(170, 24, 47, 13))
        self.label.setObjectName("label")
        self.btnClear = QtWidgets.QPushButton(self.grpMain)
        self.btnClear.setGeometry(QtCore.QRect(180, 190, 101, 23))
        self.btnClear.setObjectName("btnClear")
        self.btnSend = QtWidgets.QPushButton(self.grpMain)
        self.btnSend.setGeometry(QtCore.QRect(284, 190, 101, 23))
        self.btnSend.setObjectName("btnSend")
        self.btnDebug = QtWidgets.QPushButton(self.grpMain)
        self.btnDebug.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.btnDebug.setObjectName("btnDebug")

        self.retranslateUi(Dialog)
        self.cboChat.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "USG Bot Tool"))
        self.grpMain.setTitle(_translate("Dialog", "Bot Message Sender"))
        self.txtMessage.setAccessibleName(_translate("Dialog", "txtMessage"))
        self.lblMessage.setText(_translate("Dialog", "Message:"))
        self.label.setText(_translate("Dialog", "Chat:"))
        self.btnClear.setText(_translate("Dialog", "Clear Message"))
        self.btnSend.setText(_translate("Dialog", "Send Message"))
        self.btnDebug.setText(_translate("Dialog", "Send to Axon"))


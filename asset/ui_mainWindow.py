# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowSGiUpw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(502, 343)
        MainWindow.setStyleSheet(u"font: 57 11pt \"Ubuntu\";\n"
"background-color: rgb(61, 56, 70);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(50, 90, 401, 61))
        self.textBrowser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(119, 118, 123);")
        self.runCamera = QPushButton(self.centralwidget)
        self.runCamera.setObjectName(u"runCamera")
        self.runCamera.setGeometry(QRect(320, 200, 111, 51))
        self.runCamera.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.exitBtn = QPushButton(self.centralwidget)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setGeometry(QRect(100, 200, 111, 51))
        self.exitBtn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 502, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:56; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:400;\">Welcome to ColoGAMA</span></p></body></html>", None))
        self.runCamera.setText(QCoreApplication.translate("MainWindow", u"Run Camera", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi


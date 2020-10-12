# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
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
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(3200, 2400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 781, 491))
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setAutoFillBackground(True)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 260, 67, 17))
        self.stackedWidget.addWidget(self.home)
        self.blue = QWidget()
        self.blue.setObjectName(u"blue")
        self.blue.setStyleSheet(u"background-color: blue")
        self.red_btn = QPushButton(self.blue)
        self.red_btn.setObjectName(u"red_btn")
        self.red_btn.setGeometry(QRect(320, 330, 89, 25))
        self.stackedWidget.addWidget(self.blue)
        self.red = QWidget()
        self.red.setObjectName(u"red")
        self.red.setStyleSheet(u"background-color: red")
        self.yellow_btn = QPushButton(self.red)
        self.yellow_btn.setObjectName(u"yellow_btn")
        self.yellow_btn.setGeometry(QRect(340, 270, 89, 25))
        self.stackedWidget.addWidget(self.red)
        self.yellow = QWidget()
        self.yellow.setObjectName(u"yellow")
        self.yellow.setStyleSheet(u"background-color: yellow")
        self.blue_btn = QPushButton(self.yellow)
        self.blue_btn.setObjectName(u"blue_btn")
        self.blue_btn.setGeometry(QRect(330, 280, 89, 25))
        self.stackedWidget.addWidget(self.yellow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"label", None))
        self.red_btn.setText(QCoreApplication.translate("MainWindow", u"red", None))
        self.yellow_btn.setText(QCoreApplication.translate("MainWindow", u"yellow", None))
        self.blue_btn.setText(QCoreApplication.translate("MainWindow", u"blue", None))
    # retranslateUi


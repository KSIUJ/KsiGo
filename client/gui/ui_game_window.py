# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gamewindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GameWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMouseTracking(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.opengl_container = QFrame(self.centralwidget)
        self.opengl_container.setObjectName(u"opengl_container")
        self.opengl_container.setMouseTracking(True)
        self.opengl_container.setFrameShape(QFrame.StyledPanel)
        self.opengl_container.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.opengl_container)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setMouseTracking(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pass_button = QPushButton(self.frame)
        self.pass_button.setObjectName(u"pass_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_button.sizePolicy().hasHeightForWidth())
        self.pass_button.setSizePolicy(sizePolicy)
        self.pass_button.setMouseTracking(True)

        self.horizontalLayout.addWidget(self.pass_button)

        self.resign_button = QPushButton(self.frame)
        self.resign_button.setObjectName(u"resign_button")
        sizePolicy.setHeightForWidth(self.resign_button.sizePolicy().hasHeightForWidth())
        self.resign_button.setSizePolicy(sizePolicy)
        self.resign_button.setMouseTracking(True)

        self.horizontalLayout.addWidget(self.resign_button)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMouseTracking(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pass_button.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.resign_button.setText(QCoreApplication.translate("MainWindow", u"Resign", None))
    # retranslateUi


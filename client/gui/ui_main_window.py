# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(436, 604)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMouseTracking(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMouseTracking(True)
        self.welcome_screen = QWidget()
        self.welcome_screen.setObjectName(u"welcome_screen")
        self.welcome_screen.setMouseTracking(True)
        self.welcome_screen.setStyleSheet(u"QLabel {\n"
"	font-size: 50px\n"
"}\n"
"\n"
"QPushButton {\n"
"	font-size: 25px\n"
"}")
        self.gridLayout = QGridLayout(self.welcome_screen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.start_button = QPushButton(self.welcome_screen)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMouseTracking(True)

        self.gridLayout.addWidget(self.start_button, 2, 0, 1, 1)

        self.ksi_png = QLabel(self.welcome_screen)
        self.ksi_png.setObjectName(u"ksi_png")
        self.ksi_png.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ksi_png.sizePolicy().hasHeightForWidth())
        self.ksi_png.setSizePolicy(sizePolicy)
        self.ksi_png.setMinimumSize(QSize(400, 400))
        self.ksi_png.setBaseSize(QSize(500, 500))
        self.ksi_png.setMouseTracking(True)
        self.ksi_png.setAutoFillBackground(False)
        self.ksi_png.setPixmap(QPixmap(u"res/ksi.png"))
        self.ksi_png.setScaledContents(True)
        self.ksi_png.setAlignment(Qt.AlignCenter)
        self.ksi_png.setMargin(30)

        self.gridLayout.addWidget(self.ksi_png, 0, 0, 1, 1)

        self.ksi_go_text = QLabel(self.welcome_screen)
        self.ksi_go_text.setObjectName(u"ksi_go_text")
        self.ksi_go_text.setMouseTracking(True)
        self.ksi_go_text.setStyleSheet(u"")
        self.ksi_go_text.setScaledContents(False)
        self.ksi_go_text.setAlignment(Qt.AlignCenter)
        self.ksi_go_text.setMargin(20)

        self.gridLayout.addWidget(self.ksi_go_text, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.welcome_screen)
        self.username_screen = QWidget()
        self.username_screen.setObjectName(u"username_screen")
        self.username_screen.setMouseTracking(True)
        self.verticalLayout_2 = QVBoxLayout(self.username_screen)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.username = QLabel(self.username_screen)
        self.username.setObjectName(u"username")
        self.username.setMaximumSize(QSize(16777215, 30))
        self.username.setMouseTracking(True)

        self.verticalLayout_2.addWidget(self.username)

        self.username_input = QTextEdit(self.username_screen)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMaximumSize(QSize(16777215, 50))
        self.username_input.setAcceptRichText(False)

        self.verticalLayout_2.addWidget(self.username_input)

        self.connect_button = QPushButton(self.username_screen)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(0, 50))
        self.connect_button.setMouseTracking(True)

        self.verticalLayout_2.addWidget(self.connect_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.username_screen)
        self.board_size_screen = QWidget()
        self.board_size_screen.setObjectName(u"board_size_screen")
        self.board_size_screen.setMouseTracking(True)
        self.board_size_screen.setStyleSheet(u"QLabel {\n"
"	font-size: 25px\n"
"}")
        self.gridLayout_2 = QGridLayout(self.board_size_screen)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.x9_button = QPushButton(self.board_size_screen)
        self.x9_button.setObjectName(u"x9_button")
        self.x9_button.setMouseTracking(True)

        self.gridLayout_2.addWidget(self.x9_button, 1, 0, 1, 1)

        self.x13_button = QPushButton(self.board_size_screen)
        self.x13_button.setObjectName(u"x13_button")
        self.x13_button.setMouseTracking(True)

        self.gridLayout_2.addWidget(self.x13_button, 2, 0, 1, 1)

        self.x19_button = QPushButton(self.board_size_screen)
        self.x19_button.setObjectName(u"x19_button")
        self.x19_button.setMouseTracking(True)

        self.gridLayout_2.addWidget(self.x19_button, 3, 0, 1, 1)

        self.label = QLabel(self.board_size_screen)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMouseTracking(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.board_size_screen)

        self.verticalLayout.addWidget(self.stackedWidget)

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
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ksi_png.setText("")
        self.ksi_go_text.setText(QCoreApplication.translate("MainWindow", u"KSI GO", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.x9_button.setText(QCoreApplication.translate("MainWindow", u"9 x 9", None))
        self.x13_button.setText(QCoreApplication.translate("MainWindow", u"13 x 13", None))
        self.x19_button.setText(QCoreApplication.translate("MainWindow", u"19 x 19", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose board size", None))
    # retranslateUi


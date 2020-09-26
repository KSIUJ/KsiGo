# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enddialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.end_text = QLabel(self.frame)
        self.end_text.setObjectName(u"end_text")

        self.verticalLayout_3.addWidget(self.end_text)


        self.verticalLayout_2.addWidget(self.frame)

        self.play_again_button = QPushButton(Dialog)
        self.play_again_button.setObjectName(u"play_again_button")

        self.verticalLayout_2.addWidget(self.play_again_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.end_text.setText(QCoreApplication.translate("Dialog", u"Won", None))
        self.play_again_button.setText(QCoreApplication.translate("Dialog", u"Play Again", None))
    # retranslateUi


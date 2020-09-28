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
        Dialog.resize(400, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.end_text = QLabel(self.frame)
        self.end_text.setObjectName(u"end_text")
        sizePolicy.setHeightForWidth(self.end_text.sizePolicy().hasHeightForWidth())
        self.end_text.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.end_text)


        self.verticalLayout_2.addWidget(self.frame)

        self.play_again_button = QPushButton(Dialog)
        self.play_again_button.setObjectName(u"play_again_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.play_again_button.sizePolicy().hasHeightForWidth())
        self.play_again_button.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.play_again_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.end_text.setText(QCoreApplication.translate("Dialog", u"Won", None))
        self.play_again_button.setText(QCoreApplication.translate("Dialog", u"Play Again", None))
    # retranslateUi


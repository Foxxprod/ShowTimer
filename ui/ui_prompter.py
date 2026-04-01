# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prompterZyKEul.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1280, 720)
        font = QFont()
        font.setFamilies([u"Script"])
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color: #00FF00;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.prompt_text = QTextEdit(Dialog)
        self.prompt_text.setObjectName(u"prompt_text")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prompt_text.sizePolicy().hasHeightForWidth())
        self.prompt_text.setSizePolicy(sizePolicy)
        self.prompt_text.setMinimumSize(QSize(0, 400))
        self.prompt_text.setStyleSheet(u"QTextEdit {\n"
"    font-size: 60px;\n"
"    font-weight: bold;\n"
"    color: #B8860B;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    line-height: 80%;\n"
"}")
        self.prompt_text.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.prompt_text.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.prompt_text.setReadOnly(True)

        self.verticalLayout.addWidget(self.prompt_text)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.second_cue = QLabel(Dialog)
        self.second_cue.setObjectName(u"second_cue")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(50)
        font1.setBold(True)
        font1.setItalic(False)
        self.second_cue.setFont(font1)
        self.second_cue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.second_cue)

        self.next_cue = QLabel(Dialog)
        self.next_cue.setObjectName(u"next_cue")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(80)
        font2.setBold(True)
        self.next_cue.setFont(font2)
        self.next_cue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.next_cue)

        self.show_remain_time = QLabel(Dialog)
        self.show_remain_time.setObjectName(u"show_remain_time")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(30)
        font3.setBold(True)
        self.show_remain_time.setFont(font3)
        self.show_remain_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_remain_time)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.second_cue.setText("")
        self.next_cue.setText("")
        self.show_remain_time.setText("")
    # retranslateUi


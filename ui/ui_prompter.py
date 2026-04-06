# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prompterwIhKYF.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

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

        self.second_cue = QWidget(Dialog)
        self.second_cue.setObjectName(u"second_cue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.second_cue.sizePolicy().hasHeightForWidth())
        self.second_cue.setSizePolicy(sizePolicy1)
        self.second_cue.setMinimumSize(QSize(0, 65))

        self.verticalLayout.addWidget(self.second_cue)

        self.next_cue = QWidget(Dialog)
        self.next_cue.setObjectName(u"next_cue")
        sizePolicy1.setHeightForWidth(self.next_cue.sizePolicy().hasHeightForWidth())
        self.next_cue.setSizePolicy(sizePolicy1)
        self.next_cue.setMinimumSize(QSize(0, 120))

        self.verticalLayout.addWidget(self.next_cue)

        self.clock_label = QWidget(Dialog)
        self.clock_label.setObjectName(u"clock_label")
        sizePolicy1.setHeightForWidth(self.clock_label.sizePolicy().hasHeightForWidth())
        self.clock_label.setSizePolicy(sizePolicy1)
        self.clock_label.setMinimumSize(QSize(0, 65))

        self.verticalLayout.addWidget(self.clock_label)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi


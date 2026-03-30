# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operatorkzvkoP.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QProgressBar, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1230, 746)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 698, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pass_time = QLabel(self.verticalLayoutWidget)
        self.pass_time.setObjectName(u"pass_time")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.pass_time.setFont(font)
        self.pass_time.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pass_time.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.pass_time, 0, 2, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(30)
        font1.setItalic(True)
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)

        self.remaining_time = QLabel(self.verticalLayoutWidget)
        self.remaining_time.setObjectName(u"remaining_time")
        self.remaining_time.setFont(font)
        self.remaining_time.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.remaining_time.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.remaining_time, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.BottomToTop)

        self.verticalLayout.addWidget(self.progressBar)

        self.cue_table_widget = QTableWidget(Dialog)
        self.cue_table_widget.setObjectName(u"cue_table_widget")
        self.cue_table_widget.setGeometry(QRect(10, 180, 701, 491))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(730, 290, 481, 221))
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 20, 461, 191))
        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(720, 20, 121, 151))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.timer_play = QToolButton(self.verticalLayoutWidget_2)
        self.timer_play.setObjectName(u"timer_play")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_play.sizePolicy().hasHeightForWidth())
        self.timer_play.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.timer_play.setIcon(icon)

        self.verticalLayout_2.addWidget(self.timer_play)

        self.timer_pause = QToolButton(self.verticalLayoutWidget_2)
        self.timer_pause.setObjectName(u"timer_pause")
        sizePolicy.setHeightForWidth(self.timer_pause.sizePolicy().hasHeightForWidth())
        self.timer_pause.setSizePolicy(sizePolicy)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.timer_pause.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.timer_pause)

        self.timer_stop = QToolButton(self.verticalLayoutWidget_2)
        self.timer_stop.setObjectName(u"timer_stop")
        sizePolicy.setHeightForWidth(self.timer_stop.sizePolicy().hasHeightForWidth())
        self.timer_stop.setSizePolicy(sizePolicy)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.timer_stop.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.timer_stop)

        self.add_cue = QToolButton(Dialog)
        self.add_cue.setObjectName(u"add_cue")
        self.add_cue.setGeometry(QRect(490, 670, 111, 71))
        self.delete_cue = QToolButton(Dialog)
        self.delete_cue.setObjectName(u"delete_cue")
        self.delete_cue.setGeometry(QRect(600, 670, 111, 71))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pass_time.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Temps \u00e9coul\u00e9 :", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Temps restant :", None))
        self.remaining_time.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.progressBar.setFormat("")
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Message du prompteur", None))
        self.timer_play.setText(QCoreApplication.translate("Dialog", u"PLAY", None))
        self.timer_pause.setText(QCoreApplication.translate("Dialog", u"PAUSE", None))
        self.timer_stop.setText(QCoreApplication.translate("Dialog", u"STOP", None))
        self.add_cue.setText(QCoreApplication.translate("Dialog", u"Ajouter un CUE", None))
        self.delete_cue.setText(QCoreApplication.translate("Dialog", u"Suppri un CUE", None))
    # retranslateUi


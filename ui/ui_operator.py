# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operatorliyGzY.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QProgressBar, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1300, 746)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 698, 154))
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
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    height: 30px;\n"
"    border-radius: 5px;\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 5px;\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.BottomToTop)

        self.verticalLayout.addWidget(self.progressBar)

        self.cue_table_widget = QTableWidget(Dialog)
        self.cue_table_widget.setObjectName(u"cue_table_widget")
        self.cue_table_widget.setGeometry(QRect(10, 180, 831, 491))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(870, 150, 421, 261))
        self.prompt_textedit = QTextEdit(self.groupBox)
        self.prompt_textedit.setObjectName(u"prompt_textedit")
        self.prompt_textedit.setGeometry(QRect(10, 20, 401, 191))
        font2 = QFont()
        font2.setPointSize(20)
        self.prompt_textedit.setFont(font2)
        self.prompt_clear = QToolButton(self.groupBox)
        self.prompt_clear.setObjectName(u"prompt_clear")
        self.prompt_clear.setGeometry(QRect(10, 210, 161, 41))
        icon = QIcon()
        icon.addFile(u"icon/32x32_trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prompt_clear.setIcon(icon)
        self.prompt_clear.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.prompt_highlight = QToolButton(self.groupBox)
        self.prompt_highlight.setObjectName(u"prompt_highlight")
        self.prompt_highlight.setGeometry(QRect(260, 210, 151, 41))
        icon1 = QIcon()
        icon1.addFile(u"icon/32x32_alert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prompt_highlight.setIcon(icon1)
        self.prompt_highlight.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
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
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.timer_play.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.timer_play)

        self.timer_pause = QToolButton(self.verticalLayoutWidget_2)
        self.timer_pause.setObjectName(u"timer_pause")
        sizePolicy.setHeightForWidth(self.timer_pause.sizePolicy().hasHeightForWidth())
        self.timer_pause.setSizePolicy(sizePolicy)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.timer_pause.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.timer_pause)

        self.timer_stop = QToolButton(self.verticalLayoutWidget_2)
        self.timer_stop.setObjectName(u"timer_stop")
        sizePolicy.setHeightForWidth(self.timer_stop.sizePolicy().hasHeightForWidth())
        self.timer_stop.setSizePolicy(sizePolicy)
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.timer_stop.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.timer_stop)

        self.add_cue = QToolButton(Dialog)
        self.add_cue.setObjectName(u"add_cue")
        self.add_cue.setGeometry(QRect(510, 670, 111, 71))
        icon5 = QIcon()
        icon5.addFile(u"icon/32x32_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_cue.setIcon(icon5)
        self.add_cue.setIconSize(QSize(32, 32))
        self.add_cue.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.delete_cue = QToolButton(Dialog)
        self.delete_cue.setObjectName(u"delete_cue")
        self.delete_cue.setGeometry(QRect(730, 670, 111, 71))
        icon6 = QIcon()
        icon6.addFile(u"icon/32x32_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_cue.setIcon(icon6)
        self.delete_cue.setIconSize(QSize(32, 32))
        self.delete_cue.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.modify_cue = QToolButton(Dialog)
        self.modify_cue.setObjectName(u"modify_cue")
        self.modify_cue.setGeometry(QRect(620, 670, 111, 71))
        icon7 = QIcon()
        icon7.addFile(u"icon/32x32_configuration.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modify_cue.setIcon(icon7)
        self.modify_cue.setIconSize(QSize(32, 32))
        self.modify_cue.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 680, 221, 20))
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(850, 20, 20, 711))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(870, 20, 421, 121))
        self.formLayoutWidget = QWidget(self.groupBox_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 401, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.choixDeLEcranDeSortieLabel = QLabel(self.formLayoutWidget)
        self.choixDeLEcranDeSortieLabel.setObjectName(u"choixDeLEcranDeSortieLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.choixDeLEcranDeSortieLabel)

        self.screen_selection = QComboBox(self.formLayoutWidget)
        self.screen_selection.setObjectName(u"screen_selection")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.screen_selection)

        self.modeDIncrustationLabel = QLabel(self.formLayoutWidget)
        self.modeDIncrustationLabel.setObjectName(u"modeDIncrustationLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.modeDIncrustationLabel)

        self.key_mode = QComboBox(self.formLayoutWidget)
        self.key_mode.setObjectName(u"key_mode")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.key_mode)

        self.screen_active = QCheckBox(self.groupBox_2)
        self.screen_active.setObjectName(u"screen_active")
        self.screen_active.setGeometry(QRect(10, 90, 141, 20))
        self.fullscreen = QCheckBox(self.groupBox_2)
        self.fullscreen.setObjectName(u"fullscreen")
        self.fullscreen.setGeometry(QRect(160, 90, 141, 20))

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
        self.prompt_clear.setText(QCoreApplication.translate("Dialog", u"VIDER LE MESSAGE (F1)", None))
        self.prompt_highlight.setText(QCoreApplication.translate("Dialog", u"FAIRE CLIGNOTER (F2)", None))
        self.timer_play.setText(QCoreApplication.translate("Dialog", u"PLAY", None))
        self.timer_pause.setText(QCoreApplication.translate("Dialog", u"PAUSE", None))
        self.timer_stop.setText(QCoreApplication.translate("Dialog", u"STOP", None))
        self.add_cue.setText(QCoreApplication.translate("Dialog", u"Ajouter un CUE", None))
        self.delete_cue.setText(QCoreApplication.translate("Dialog", u"Supprimer le CUE", None))
        self.modify_cue.setText(QCoreApplication.translate("Dialog", u"Modifier le CUE", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Activer l'envoi des commandes OSC", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"SORTIE VIDEO", None))
        self.choixDeLEcranDeSortieLabel.setText(QCoreApplication.translate("Dialog", u"Choix de l'ecran de sortie", None))
        self.modeDIncrustationLabel.setText(QCoreApplication.translate("Dialog", u"Mode d'incrustation ", None))
        self.screen_active.setText(QCoreApplication.translate("Dialog", u"Activer la sortie vid\u00e9o", None))
        self.fullscreen.setText(QCoreApplication.translate("Dialog", u"Plein ecran", None))
    # retranslateUi


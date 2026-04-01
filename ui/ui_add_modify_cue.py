# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_modify_cueVPQlxl.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QTimeEdit, QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(455, 302)
        self.validate = QToolButton(Dialog)
        self.validate.setObjectName(u"validate")
        self.validate.setGeometry(QRect(80, 230, 131, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validate.sizePolicy().hasHeightForWidth())
        self.validate.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icon/32x32_ok.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.validate.setIcon(icon)
        self.validate.setIconSize(QSize(32, 32))
        self.validate.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.abort = QToolButton(Dialog)
        self.abort.setObjectName(u"abort")
        self.abort.setGeometry(QRect(230, 230, 132, 61))
        sizePolicy.setHeightForWidth(self.abort.sizePolicy().hasHeightForWidth())
        self.abort.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"icon/32x32_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.abort.setIcon(icon1)
        self.abort.setIconSize(QSize(32, 32))
        self.abort.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 431, 211))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 411, 181))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.titreDuCueLabel = QLabel(self.formLayoutWidget)
        self.titreDuCueLabel.setObjectName(u"titreDuCueLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.titreDuCueLabel)

        self.cue_title = QLineEdit(self.formLayoutWidget)
        self.cue_title.setObjectName(u"cue_title")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cue_title)

        self.descriptionLabel = QLabel(self.formLayoutWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.descriptionLabel)

        self.cue_desc = QLineEdit(self.formLayoutWidget)
        self.cue_desc.setObjectName(u"cue_desc")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cue_desc)

        self.tempsDeDClenchementLabel = QLabel(self.formLayoutWidget)
        self.tempsDeDClenchementLabel.setObjectName(u"tempsDeDClenchementLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tempsDeDClenchementLabel)

        self.time = QTimeEdit(self.formLayoutWidget)
        self.time.setObjectName(u"time")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.time)

        self.commandOSCLabel = QLabel(self.formLayoutWidget)
        self.commandOSCLabel.setObjectName(u"commandOSCLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.commandOSCLabel)

        self.osc_command = QLineEdit(self.formLayoutWidget)
        self.osc_command.setObjectName(u"osc_command")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.osc_command)

        self.couleurDuCueLabel = QLabel(self.formLayoutWidget)
        self.couleurDuCueLabel.setObjectName(u"couleurDuCueLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.couleurDuCueLabel)

        self.cue_color = QComboBox(self.formLayoutWidget)
        self.cue_color.setObjectName(u"cue_color")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cue_color)

        self.argumentOscLabel = QLabel(self.formLayoutWidget)
        self.argumentOscLabel.setObjectName(u"argumentOscLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.argumentOscLabel)

        self.osc_args = QSpinBox(self.formLayoutWidget)
        self.osc_args.setObjectName(u"osc_args")
        self.osc_args.setMaximum(999999999)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.osc_args)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.validate.setText(QCoreApplication.translate("Dialog", u"VALIDER", None))
        self.abort.setText(QCoreApplication.translate("Dialog", u"ANNULER", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Ajouter / modifier un cue", None))
        self.titreDuCueLabel.setText(QCoreApplication.translate("Dialog", u"Titre du cue", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"description ", None))
        self.tempsDeDClenchementLabel.setText(QCoreApplication.translate("Dialog", u"Temps de d\u00e9clenchement", None))
        self.time.setDisplayFormat(QCoreApplication.translate("Dialog", u"mm:ss", None))
        self.commandOSCLabel.setText(QCoreApplication.translate("Dialog", u"command OSC", None))
        self.couleurDuCueLabel.setText(QCoreApplication.translate("Dialog", u"couleur du cue ", None))
        self.argumentOscLabel.setText(QCoreApplication.translate("Dialog", u"argument osc", None))
    # retranslateUi


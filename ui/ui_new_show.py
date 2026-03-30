# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_showeuMGco.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QTimeEdit,
    QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(414, 272)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 391, 121))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 371, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nomDeLEmissionLabel = QLabel(self.formLayoutWidget)
        self.nomDeLEmissionLabel.setObjectName(u"nomDeLEmissionLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomDeLEmissionLabel)

        self.show_name = QLineEdit(self.formLayoutWidget)
        self.show_name.setObjectName(u"show_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.show_name)

        self.descriptionDeLEmissionLabel = QLabel(self.formLayoutWidget)
        self.descriptionDeLEmissionLabel.setObjectName(u"descriptionDeLEmissionLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.descriptionDeLEmissionLabel)

        self.show_description = QLineEdit(self.formLayoutWidget)
        self.show_description.setObjectName(u"show_description")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.show_description)

        self.durEDeLEmissionMmSsLabel = QLabel(self.formLayoutWidget)
        self.durEDeLEmissionMmSsLabel.setObjectName(u"durEDeLEmissionMmSsLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.durEDeLEmissionMmSsLabel)

        self.show_time = QTimeEdit(self.formLayoutWidget)
        self.show_time.setObjectName(u"show_time")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.show_time)

        self.create = QToolButton(Dialog)
        self.create.setObjectName(u"create")
        self.create.setGeometry(QRect(60, 140, 131, 79))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create.sizePolicy().hasHeightForWidth())
        self.create.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icon/32x32_ok.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create.setIcon(icon)
        self.create.setIconSize(QSize(32, 32))
        self.create.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.abort = QToolButton(Dialog)
        self.abort.setObjectName(u"abort")
        self.abort.setGeometry(QRect(200, 140, 132, 79))
        sizePolicy.setHeightForWidth(self.abort.sizePolicy().hasHeightForWidth())
        self.abort.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"icon/32x32_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.abort.setIcon(icon1)
        self.abort.setIconSize(QSize(32, 32))
        self.abort.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Creer une emission", None))
        self.nomDeLEmissionLabel.setText(QCoreApplication.translate("Dialog", u"Nom de l'emission", None))
        self.descriptionDeLEmissionLabel.setText(QCoreApplication.translate("Dialog", u"Description de l'emission", None))
        self.durEDeLEmissionMmSsLabel.setText(QCoreApplication.translate("Dialog", u"Dur\u00e9e de l'emission (mm:ss)", None))
        self.create.setText(QCoreApplication.translate("Dialog", u"Creer", None))
        self.abort.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi


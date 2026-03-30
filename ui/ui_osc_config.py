# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'osc_configsLbZIe.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(366, 175)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 341, 91))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 321, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.adresseIPDuServeurOSCLabel = QLabel(self.formLayoutWidget)
        self.adresseIPDuServeurOSCLabel.setObjectName(u"adresseIPDuServeurOSCLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.adresseIPDuServeurOSCLabel)

        self.osc_ip = QLineEdit(self.formLayoutWidget)
        self.osc_ip.setObjectName(u"osc_ip")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.osc_ip)

        self.portDuServeurOSCLabel = QLabel(self.formLayoutWidget)
        self.portDuServeurOSCLabel.setObjectName(u"portDuServeurOSCLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.portDuServeurOSCLabel)

        self.osc_port = QSpinBox(self.formLayoutWidget)
        self.osc_port.setObjectName(u"osc_port")
        self.osc_port.setMaximum(65535)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.osc_port)

        self.create = QToolButton(Dialog)
        self.create.setObjectName(u"create")
        self.create.setGeometry(QRect(20, 110, 131, 61))
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
        self.abort.setGeometry(QRect(210, 110, 132, 61))
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
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Param\u00e8tre du client OSC", None))
        self.adresseIPDuServeurOSCLabel.setText(QCoreApplication.translate("Dialog", u"Adresse IP du serveur OSC", None))
        self.portDuServeurOSCLabel.setText(QCoreApplication.translate("Dialog", u"Port du serveur OSC", None))
        self.create.setText(QCoreApplication.translate("Dialog", u"VALIDER", None))
        self.abort.setText(QCoreApplication.translate("Dialog", u"ANNULER", None))
    # retranslateUi


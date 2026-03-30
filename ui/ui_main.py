# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingypZGY.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QTableView, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(848, 544)
        self.actionConfig_OSC = QAction(MainWindow)
        self.actionConfig_OSC.setObjectName(u"actionConfig_OSC")
        self.actionConfig_globales = QAction(MainWindow)
        self.actionConfig_globales.setObjectName(u"actionConfig_globales")
        self.actionContact_33_6_52_75_25_29 = QAction(MainWindow)
        self.actionContact_33_6_52_75_25_29.setObjectName(u"actionContact_33_6_52_75_25_29")
        self.actiontitouan_gallin_gmail_com = QAction(MainWindow)
        self.actiontitouan_gallin_gmail_com.setObjectName(u"actiontitouan_gallin_gmail_com")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.show_table_view = QTableView(self.centralwidget)
        self.show_table_view.setObjectName(u"show_table_view")
        self.show_table_view.setGeometry(QRect(10, 10, 821, 421))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 430, 821, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.open_show = QToolButton(self.horizontalLayoutWidget)
        self.open_show.setObjectName(u"open_show")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_show.sizePolicy().hasHeightForWidth())
        self.open_show.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icon/32x32_ok.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_show.setIcon(icon)
        self.open_show.setIconSize(QSize(32, 32))
        self.open_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.open_show)

        self.add_show = QToolButton(self.horizontalLayoutWidget)
        self.add_show.setObjectName(u"add_show")
        sizePolicy.setHeightForWidth(self.add_show.sizePolicy().hasHeightForWidth())
        self.add_show.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"icon/32x32_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_show.setIcon(icon1)
        self.add_show.setIconSize(QSize(32, 32))
        self.add_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.add_show)

        self.modify_show = QToolButton(self.horizontalLayoutWidget)
        self.modify_show.setObjectName(u"modify_show")
        sizePolicy.setHeightForWidth(self.modify_show.sizePolicy().hasHeightForWidth())
        self.modify_show.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u"icon/32x32_configuration.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modify_show.setIcon(icon2)
        self.modify_show.setIconSize(QSize(32, 32))
        self.modify_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.modify_show)

        self.delete_show = QToolButton(self.horizontalLayoutWidget)
        self.delete_show.setObjectName(u"delete_show")
        sizePolicy.setHeightForWidth(self.delete_show.sizePolicy().hasHeightForWidth())
        self.delete_show.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"icon/32x32_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_show.setIcon(icon3)
        self.delete_show.setIconSize(QSize(32, 32))
        self.delete_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.delete_show)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 848, 33))
        self.menuConfig = QMenu(self.menubar)
        self.menuConfig.setObjectName(u"menuConfig")
        self.menuAide = QMenu(self.menubar)
        self.menuAide.setObjectName(u"menuAide")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())
        self.menuConfig.addAction(self.actionConfig_OSC)
        self.menuConfig.addAction(self.actionConfig_globales)
        self.menuAide.addAction(self.actionContact_33_6_52_75_25_29)
        self.menuAide.addAction(self.actiontitouan_gallin_gmail_com)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConfig_OSC.setText(QCoreApplication.translate("MainWindow", u"Config OSC", None))
        self.actionConfig_globales.setText(QCoreApplication.translate("MainWindow", u"Config globales", None))
        self.actionContact_33_6_52_75_25_29.setText(QCoreApplication.translate("MainWindow", u"Contact : +33 6 52 75 25 29", None))
        self.actiontitouan_gallin_gmail_com.setText(QCoreApplication.translate("MainWindow", u"titouan.gallin@gmail.com", None))
        self.open_show.setText(QCoreApplication.translate("MainWindow", u"OUVRIR", None))
        self.add_show.setText(QCoreApplication.translate("MainWindow", u"CREER NOUVEAU", None))
        self.modify_show.setText(QCoreApplication.translate("MainWindow", u"MODIFIER", None))
        self.delete_show.setText(QCoreApplication.translate("MainWindow", u"SUPPRIMER", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Aide", None))
    # retranslateUi


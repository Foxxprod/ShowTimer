# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainCfwGjs.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTableView, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(521, 572)
        MainWindow.setStyleSheet(u"/* ============================================================\n"
"   GLOBAL QSS \u2014 TIMER PCP \u2014 Modern Dark Theme\n"
"   ============================================================ */\n"
"\n"
"/* === BASE === */\n"
"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    color: #e0e0e0;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QMainWindow, QDialog {\n"
"    background-color: #1e1e1e;\n"
"}\n"
"\n"
"/* === MENU BAR === */\n"
"QMenuBar {\n"
"    background-color: #161616;\n"
"    color: #e0e0e0;\n"
"    padding: 2px;\n"
"    border-bottom: 1px solid #2d2d2d;\n"
"}\n"
"QMenuBar::item:selected {\n"
"    background-color: #0078d4;\n"
"    border-radius: 3px;\n"
"}\n"
"QMenu {\n"
"    background-color: #252525;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #3a3a3a;\n"
"    padding: 4px 0px;\n"
"}\n"
"QMenu::item {\n"
"    padding: 6px 20px;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #0078d4;\n"
"}\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    backgr"
                        "ound-color: #3a3a3a;\n"
"    margin: 4px 8px;\n"
"}\n"
"\n"
"/* === TAB WIDGET === */\n"
"QTabWidget::pane {\n"
"    background-color: #252525;\n"
"    border: none;\n"
"    border-top: 2px solid #0078d4;\n"
"}\n"
"QTabBar {\n"
"    background-color: #161616;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: transparent;\n"
"    color: #aaaaaa;\n"
"    padding: 7px 18px;\n"
"    font-size: 12px;\n"
"    border: none;\n"
"    min-width: 70px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background-color: #252525;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border-top: 2px solid #0078d4;\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: rgba(255,255,255,0.06);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* === BOUTONS === */\n"
"QPushButton {\n"
"    background-color: #2d2d2d;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #3a3a3a;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0078d4;\n"
"    bo"
                        "rder-color: #0078d4;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #005a9e;\n"
"    border-color: #005a9e;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #1e1e1e;\n"
"    color: #555555;\n"
"    border-color: #2a2a2a;\n"
"}\n"
"\n"
"/* === CHAMPS TEXTE === */\n"
"QLineEdit, QTextEdit, QPlainTextEdit {\n"
"    background-color: #2a2a2a;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #3a3a3a;\n"
"    border-radius: 4px;\n"
"    padding: 5px 8px;\n"
"    selection-background-color: #0078d4;\n"
"}\n"
"QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {\n"
"    border: 1px solid #0078d4;\n"
"}\n"
"\n"
"/* === LABELS === */\n"
"QLabel {\n"
"    color: #e0e0e0;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* === TABLEAUX === */\n"
"QTableWidget, QTableView {\n"
"    background-color: #252525;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #3a3a3a;\n"
"    gridline-color: #2d2d2d;\n"
"    selection-background-color: #0078d4;\n"
"    selection-color: #"
                        "ffffff;\n"
"    alternate-background-color: #2a2a2a;\n"
"}\n"
"QTableWidget::item, QTableView::item {\n"
"    padding: 4px 6px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #1a1a1a;\n"
"    color: #aaaaaa;\n"
"    border: none;\n"
"    border-right: 1px solid #2d2d2d;\n"
"    border-bottom: 1px solid #3a3a3a;\n"
"    padding: 5px 8px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"/* === COMBOBOX === */\n"
"QComboBox {\n"
"    background-color: #2a2a2a;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #3a3a3a;\n"
"    border-radius: 4px;\n"
"    padding: 5px 8px;\n"
"}\n"
"QComboBox:hover {\n"
"    border-color: #0078d4;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #252525;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #3a3a3a;\n"
"    selection-background-color: #0078d4;\n"
"}\n"
"\n"
"/* === SPINBOX === */\n"
"QSpinBox, QDoubleSpinBox {\n"
"    background-color: #2a2a2a;\n"
""
                        "    color: #e0e0e0;\n"
"    border: 1px solid #3a3a3a;\n"
"    border-radius: 4px;\n"
"    padding: 4px 6px;\n"
"}\n"
"QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border-color: #0078d4;\n"
"}\n"
"\n"
"/* === CHECKBOX === */\n"
"QCheckBox {\n"
"    color: #e0e0e0;\n"
"    spacing: 8px;\n"
"    background-color: transparent;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #555555;\n"
"    border-radius: 3px;\n"
"    background-color: #2a2a2a;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #0078d4;\n"
"    border-color: #0078d4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border-color: #0078d4;\n"
"}\n"
"\n"
"/* === PROGRESS BAR === */\n"
"QProgressBar {\n"
"    background-color: #2a2a2a;\n"
"    border: 1px solid #3a3a3a;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: #e0e0e0;\n"
"    font-size: 11px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #0078d4;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
""
                        "/* === SCROLLBAR === */\n"
"QScrollBar:vertical {\n"
"    background-color: #1e1e1e;\n"
"    width: 10px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #3a3a3a;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #0078d4;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: #1e1e1e;\n"
"    height: 10px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #3a3a3a;\n"
"    border-radius: 5px;\n"
"    min-width: 30px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #0078d4;\n"
"}\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}\n"
"\n"
"/* === SEPARATEURS === */\n"
"QFrame[frameShape=\"4\"],\n"
"QFrame[frameShape=\"5\"] {\n"
"    color: #2d2d2d;\n"
"}\n"
"\n"
"/* === GROUP BOX === "
                        "*/\n"
"QGroupBox {\n"
"    border: 1px solid #3a3a3a;\n"
"    border-radius: 6px;\n"
"    margin-top: 12px;\n"
"    padding-top: 8px;\n"
"    color: #aaaaaa;\n"
"    font-size: 11px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 4px;\n"
"}\n"
"\n"
"/* === TOOLTIP === */\n"
"QToolTip {\n"
"    background-color: #2d2d2d;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #0078d4;\n"
"    border-radius: 3px;\n"
"    padding: 4px 8px;\n"
"}\n"
"")
        self.actionConfig_OSC = QAction(MainWindow)
        self.actionConfig_OSC.setObjectName(u"actionConfig_OSC")
        self.actionConfig_prompter = QAction(MainWindow)
        self.actionConfig_prompter.setObjectName(u"actionConfig_prompter")
        self.actionContact_33_6_52_75_25_29 = QAction(MainWindow)
        self.actionContact_33_6_52_75_25_29.setObjectName(u"actionContact_33_6_52_75_25_29")
        self.actiontitouan_gallin_gmail_com = QAction(MainWindow)
        self.actiontitouan_gallin_gmail_com.setObjectName(u"actiontitouan_gallin_gmail_com")
        self.show_import = QAction(MainWindow)
        self.show_import.setObjectName(u"show_import")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 251, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(460, 10, 51, 31))
        icon = QIcon()
        icon.addFile(u"icon/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u"icon/icon.png", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 510, 191, 16))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 70, 501, 431))
        self.show_table_view = QTableView(self.groupBox)
        self.show_table_view.setObjectName(u"show_table_view")
        self.show_table_view.setEnabled(True)
        self.show_table_view.setGeometry(QRect(10, 20, 481, 311))
        self.show_table_view.setStyleSheet(u"QTableWidget::item:selected {\n"
"    background-color: #2ECC71;\n"
"    color: white;\n"
"}\n"
"")
        self.show_table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.show_table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 340, 481, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.open_show = QToolButton(self.horizontalLayoutWidget)
        self.open_show.setObjectName(u"open_show")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_show.sizePolicy().hasHeightForWidth())
        self.open_show.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"icon/32x32_ok.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_show.setIcon(icon1)
        self.open_show.setIconSize(QSize(32, 32))
        self.open_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.open_show)

        self.add_show = QToolButton(self.horizontalLayoutWidget)
        self.add_show.setObjectName(u"add_show")
        sizePolicy.setHeightForWidth(self.add_show.sizePolicy().hasHeightForWidth())
        self.add_show.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u"icon/32x32_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_show.setIcon(icon2)
        self.add_show.setIconSize(QSize(32, 32))
        self.add_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.add_show)

        self.import_show = QToolButton(self.horizontalLayoutWidget)
        self.import_show.setObjectName(u"import_show")
        sizePolicy.setHeightForWidth(self.import_show.sizePolicy().hasHeightForWidth())
        self.import_show.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"icon/32x32_import.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.import_show.setIcon(icon3)
        self.import_show.setIconSize(QSize(32, 32))
        self.import_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.import_show)

        self.modify_show = QToolButton(self.horizontalLayoutWidget)
        self.modify_show.setObjectName(u"modify_show")
        sizePolicy.setHeightForWidth(self.modify_show.sizePolicy().hasHeightForWidth())
        self.modify_show.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u"icon/32x32_configuration.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modify_show.setIcon(icon4)
        self.modify_show.setIconSize(QSize(32, 32))
        self.modify_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.modify_show)

        self.delete_show = QToolButton(self.horizontalLayoutWidget)
        self.delete_show.setObjectName(u"delete_show")
        sizePolicy.setHeightForWidth(self.delete_show.sizePolicy().hasHeightForWidth())
        self.delete_show.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addFile(u"icon/32x32_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_show.setIcon(icon5)
        self.delete_show.setIconSize(QSize(32, 32))
        self.delete_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.delete_show)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 511, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 521, 37))
        self.menuConfig = QMenu(self.menubar)
        self.menuConfig.setObjectName(u"menuConfig")
        self.menuAide = QMenu(self.menubar)
        self.menuAide.setObjectName(u"menuAide")
        self.menuImport = QMenu(self.menubar)
        self.menuImport.setObjectName(u"menuImport")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())
        self.menuConfig.addAction(self.actionConfig_OSC)
        self.menuConfig.addAction(self.actionConfig_prompter)
        self.menuAide.addAction(self.actionContact_33_6_52_75_25_29)
        self.menuAide.addAction(self.actiontitouan_gallin_gmail_com)
        self.menuImport.addAction(self.show_import)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConfig_OSC.setText(QCoreApplication.translate("MainWindow", u"Config OSC", None))
        self.actionConfig_prompter.setText(QCoreApplication.translate("MainWindow", u"Config du prompteur", None))
        self.actionContact_33_6_52_75_25_29.setText(QCoreApplication.translate("MainWindow", u"Contact : +33 6 52 75 25 29", None))
        self.actiontitouan_gallin_gmail_com.setText(QCoreApplication.translate("MainWindow", u"titouan.gallin@gmail.com", None))
        self.show_import.setText(QCoreApplication.translate("MainWindow", u"Importer un show", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SHOW TIMER V1", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 FoxxProd 2026 - ShowTimer 1.1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Selectionnez une emission a ouvrir / modifier / supprimer", None))
        self.open_show.setText(QCoreApplication.translate("MainWindow", u"OUVRIR", None))
        self.add_show.setText(QCoreApplication.translate("MainWindow", u"CREER NOUVEAU", None))
        self.import_show.setText(QCoreApplication.translate("MainWindow", u"IMPORTER", None))
        self.modify_show.setText(QCoreApplication.translate("MainWindow", u"MODIFIER", None))
        self.delete_show.setText(QCoreApplication.translate("MainWindow", u"SUPPRIMER", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.menuImport.setTitle(QCoreApplication.translate("MainWindow", u"Import", None))
    # retranslateUi


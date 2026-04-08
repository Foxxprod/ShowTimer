# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operatorXCUzjp.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDialog, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QTimeEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1279, 862)
        Dialog.setStyleSheet(u"/* ============================================================\n"
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
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(870, 480, 401, 271))
        self.prompt_textedit = QTextEdit(self.groupBox)
        self.prompt_textedit.setObjectName(u"prompt_textedit")
        self.prompt_textedit.setGeometry(QRect(10, 20, 381, 191))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.prompt_textedit.setFont(font)
        self.prompt_clear = QToolButton(self.groupBox)
        self.prompt_clear.setObjectName(u"prompt_clear")
        self.prompt_clear.setGeometry(QRect(10, 220, 161, 41))
        icon = QIcon()
        icon.addFile(u"icon/32x32_trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prompt_clear.setIcon(icon)
        self.prompt_clear.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.prompt_highlight = QToolButton(self.groupBox)
        self.prompt_highlight.setObjectName(u"prompt_highlight")
        self.prompt_highlight.setGeometry(QRect(240, 220, 151, 41))
        icon1 = QIcon()
        icon1.addFile(u"icon/32x32_alert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prompt_highlight.setIcon(icon1)
        self.prompt_highlight.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(850, 130, 20, 611))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 680, 831, 71))
        self.logs_text = QTextEdit(self.groupBox_3)
        self.logs_text.setObjectName(u"logs_text")
        self.logs_text.setGeometry(QRect(10, 20, 811, 41))
        self.logs_text.setFont(font)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1141, 125))
        self.tabWidget.setStyleSheet(u"/* === BARRE D'ONGLETS (style Office Dark) === */\n"
"QTabWidget::pane {\n"
"    background-color: #2b2b2b;\n"
"    border: none;\n"
"    border-top: 2px solid #0078d4;\n"
"}\n"
"\n"
"QTabBar {\n"
"    background-color: #161616;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: transparent;\n"
"    color: #cccccc;\n"
"    padding: 6px 16px;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    border: none;\n"
"    min-width: 60px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border-top: 3px solid #0078d4;\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: rgba(255, 255, 255, 0.08);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #cccccc;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 3px;\n"
"    padding: 4px 8px;\n"
"    font-size: 11px;\n"
"    min-width: 50px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QPushButton:"
                        "hover {\n"
"    background-color: #2d3a4f;\n"
"    border: 1px solid #0078d4;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0078d4;\n"
"    border: 1px solid #005a9e;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #555555;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #cccccc;\n"
"    font-size: 11px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #2b2b2b;\n"
"    color: #cccccc;\n"
"}\n"
"\n"
"QFrame[frameShape=\"5\"] {\n"
"    color: #3a3a3a;\n"
"    max-width: 1px;\n"
"    margin: 4px 2px;\n"
"}\n"
"")
        self.fichier = QWidget()
        self.fichier.setObjectName(u"fichier")
        self.save_show = QToolButton(self.fichier)
        self.save_show.setObjectName(u"save_show")
        self.save_show.setGeometry(QRect(110, 10, 131, 51))
        icon2 = QIcon()
        icon2.addFile(u"icon/32x32_save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_show.setIcon(icon2)
        self.save_show.setIconSize(QSize(20, 20))
        self.save_show.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.quit = QToolButton(self.fichier)
        self.quit.setObjectName(u"quit")
        self.quit.setGeometry(QRect(10, 10, 71, 51))
        icon3 = QIcon()
        icon3.addFile(u"icon/32x32_quit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quit.setIcon(icon3)
        self.quit.setIconSize(QSize(20, 20))
        self.quit.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.line_17 = QFrame(self.fichier)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(90, 0, 7, 91))
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_17 = QLabel(self.fichier)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(27, 70, 41, 16))
        self.label_18 = QLabel(self.fichier)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(150, 70, 61, 16))
        self.line_18 = QFrame(self.fichier)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(260, 0, 7, 91))
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)
        self.pdf_export = QToolButton(self.fichier)
        self.pdf_export.setObjectName(u"pdf_export")
        self.pdf_export.setGeometry(QRect(285, 10, 81, 51))
        icon4 = QIcon()
        icon4.addFile(u"icon/16x16_pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pdf_export.setIcon(icon4)
        self.pdf_export.setIconSize(QSize(20, 20))
        self.pdf_export.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.label_19 = QLabel(self.fichier)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(270, 70, 121, 16))
        self.line_19 = QFrame(self.fichier)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setGeometry(QRect(390, 0, 7, 91))
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)
        self.lock = QToolButton(self.fichier)
        self.lock.setObjectName(u"lock")
        self.lock.setGeometry(QRect(410, 10, 81, 51))
        icon5 = QIcon()
        icon5.addFile(u"icon/16x16_unlock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lock.setIcon(icon5)
        self.lock.setIconSize(QSize(20, 20))
        self.lock.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.label_20 = QLabel(self.fichier)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(440, 70, 31, 16))
        self.line_20 = QFrame(self.fichier)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setGeometry(QRect(505, 0, 7, 91))
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.fichier, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.add_cue = QToolButton(self.tab)
        self.add_cue.setObjectName(u"add_cue")
        self.add_cue.setGeometry(QRect(10, 10, 91, 51))
        icon6 = QIcon()
        icon6.addFile(u"icon/32x32_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_cue.setIcon(icon6)
        self.add_cue.setIconSize(QSize(20, 20))
        self.add_cue.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.modify_cue = QToolButton(self.tab)
        self.modify_cue.setObjectName(u"modify_cue")
        self.modify_cue.setGeometry(QRect(110, 10, 91, 51))
        icon7 = QIcon()
        icon7.addFile(u"icon/32x32_configuration.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modify_cue.setIcon(icon7)
        self.modify_cue.setIconSize(QSize(20, 20))
        self.modify_cue.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.delete_cue = QToolButton(self.tab)
        self.delete_cue.setObjectName(u"delete_cue")
        self.delete_cue.setGeometry(QRect(210, 10, 101, 51))
        self.delete_cue.setIcon(icon)
        self.delete_cue.setIconSize(QSize(20, 20))
        self.delete_cue.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(320, 0, 7, 91))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 70, 51, 16))
        self.excel_import = QToolButton(self.tab)
        self.excel_import.setObjectName(u"excel_import")
        self.excel_import.setGeometry(QRect(330, 10, 101, 25))
        icon8 = QIcon()
        icon8.addFile(u"icon/AppExcel32x32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.excel_import.setIcon(icon8)
        self.excel_import.setIconSize(QSize(15, 15))
        self.excel_import.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.csv_import = QToolButton(self.tab)
        self.csv_import.setObjectName(u"csv_import")
        self.csv_import.setGeometry(QRect(330, 35, 101, 25))
        icon9 = QIcon()
        icon9.addFile(u"icon/csv.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.csv_import.setIcon(icon9)
        self.csv_import.setIconSize(QSize(15, 15))
        self.csv_import.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.line_9 = QFrame(self.tab)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(440, 0, 7, 91))
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.excel_export = QToolButton(self.tab)
        self.excel_export.setObjectName(u"excel_export")
        self.excel_export.setGeometry(QRect(450, 10, 101, 25))
        self.excel_export.setIcon(icon8)
        self.excel_export.setIconSize(QSize(15, 15))
        self.excel_export.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.csv_export = QToolButton(self.tab)
        self.csv_export.setObjectName(u"csv_export")
        self.csv_export.setGeometry(QRect(450, 35, 101, 25))
        self.csv_export.setIcon(icon9)
        self.csv_export.setIconSize(QSize(15, 15))
        self.csv_export.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.line_10 = QFrame(self.tab)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(560, 0, 7, 91))
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(345, 70, 71, 16))
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(460, 70, 81, 16))
        self.delete_all_cues = QToolButton(self.tab)
        self.delete_all_cues.setObjectName(u"delete_all_cues")
        self.delete_all_cues.setGeometry(QRect(570, 10, 101, 51))
        icon10 = QIcon()
        icon10.addFile(u"icon/32x32_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_all_cues.setIcon(icon10)
        self.delete_all_cues.setIconSize(QSize(20, 20))
        self.delete_all_cues.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.line_11 = QFrame(self.tab)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(680, 0, 7, 91))
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(590, 70, 61, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayoutWidget = QWidget(self.tab_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 401, 51))
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

        self.line_5 = QFrame(self.tab_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(420, 0, 7, 91))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(440, 10, 160, 51))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.screen_active = QCheckBox(self.gridLayoutWidget_2)
        self.screen_active.setObjectName(u"screen_active")

        self.gridLayout_3.addWidget(self.screen_active, 0, 0, 1, 1)

        self.fullscreen = QCheckBox(self.gridLayoutWidget_2)
        self.fullscreen.setObjectName(u"fullscreen")

        self.gridLayout_3.addWidget(self.fullscreen, 1, 0, 1, 1)

        self.line_6 = QFrame(self.tab_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(610, 0, 7, 91))
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.prompter_config = QToolButton(self.tab_2)
        self.prompter_config.setObjectName(u"prompter_config")
        self.prompter_config.setGeometry(QRect(620, 10, 161, 51))
        self.prompter_config.setIcon(icon7)
        self.prompter_config.setIconSize(QSize(32, 32))
        self.prompter_config.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.line_7 = QFrame(self.tab_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(790, 0, 7, 91))
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayoutWidget_3 = QWidget(self.tab_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(800, 10, 160, 52))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.prompt_clear_2 = QToolButton(self.gridLayoutWidget_3)
        self.prompt_clear_2.setObjectName(u"prompt_clear_2")
        self.prompt_clear_2.setIcon(icon)
        self.prompt_clear_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_4.addWidget(self.prompt_clear_2, 0, 0, 1, 1)

        self.prompt_highlight_2 = QToolButton(self.gridLayoutWidget_3)
        self.prompt_highlight_2.setObjectName(u"prompt_highlight_2")
        self.prompt_highlight_2.setIcon(icon1)
        self.prompt_highlight_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_4.addWidget(self.prompt_highlight_2, 1, 0, 1, 1)

        self.line_8 = QFrame(self.tab_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(970, 0, 7, 91))
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(850, 70, 49, 16))
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 70, 81, 16))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 70, 51, 16))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 70, 101, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.osc_active = QCheckBox(self.tab_4)
        self.osc_active.setObjectName(u"osc_active")
        self.osc_active.setGeometry(QRect(10, 10, 221, 20))
        self.line_4 = QFrame(self.tab_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(240, 0, 7, 91))
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.formLayoutWidget_2 = QWidget(self.tab_4)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(250, 10, 221, 51))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.iPDuServeurOSCLabel = QLabel(self.formLayoutWidget_2)
        self.iPDuServeurOSCLabel.setObjectName(u"iPDuServeurOSCLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iPDuServeurOSCLabel)

        self.osc_server_ip = QLineEdit(self.formLayoutWidget_2)
        self.osc_server_ip.setObjectName(u"osc_server_ip")
        self.osc_server_ip.setEnabled(True)
        self.osc_server_ip.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.osc_server_ip)

        self.portDuServeurOSCLabel = QLabel(self.formLayoutWidget_2)
        self.portDuServeurOSCLabel.setObjectName(u"portDuServeurOSCLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.portDuServeurOSCLabel)

        self.osc_server_port = QSpinBox(self.formLayoutWidget_2)
        self.osc_server_port.setObjectName(u"osc_server_port")
        self.osc_server_port.setEnabled(True)
        self.osc_server_port.setReadOnly(True)
        self.osc_server_port.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.osc_server_port.setMaximum(100000)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.osc_server_port)

        self.osc_ping = QToolButton(self.tab_4)
        self.osc_ping.setObjectName(u"osc_ping")
        self.osc_ping.setGeometry(QRect(580, 10, 101, 51))
        icon11 = QIcon()
        icon11.addFile(u"icon/32x32_antenna.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.osc_ping.setIcon(icon11)
        self.osc_ping.setIconSize(QSize(25, 25))
        self.osc_ping.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.osc_config = QToolButton(self.tab_4)
        self.osc_config.setObjectName(u"osc_config")
        self.osc_config.setGeometry(QRect(480, 10, 81, 51))
        icon12 = QIcon()
        icon12.addFile(u"icon/32x32_config.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.osc_config.setIcon(icon12)
        self.osc_config.setIconSize(QSize(25, 25))
        self.osc_config.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.line_13 = QFrame(self.tab_4)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(570, 0, 7, 91))
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_14 = QFrame(self.tab_4)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(690, 0, 7, 91))
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(60, 70, 111, 16))
        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(340, 70, 151, 16))
        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(610, 70, 51, 16))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.open_logs = QToolButton(self.tab_5)
        self.open_logs.setObjectName(u"open_logs")
        self.open_logs.setGeometry(QRect(10, 10, 101, 51))
        icon13 = QIcon()
        icon13.addFile(u"icon/32x32_sos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_logs.setIcon(icon13)
        self.open_logs.setIconSize(QSize(25, 25))
        self.open_logs.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.delete_logs = QToolButton(self.tab_5)
        self.delete_logs.setObjectName(u"delete_logs")
        self.delete_logs.setGeometry(QRect(110, 10, 101, 51))
        self.delete_logs.setIcon(icon)
        self.delete_logs.setIconSize(QSize(25, 25))
        self.delete_logs.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.label_16 = QLabel(self.tab_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(100, 70, 41, 16))
        self.line_16 = QFrame(self.tab_5)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(220, 0, 7, 91))
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.tab_5, "")
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(870, 260, 401, 201))
        self.horizontalLayoutWidget = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 140, 381, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.timer_play = QToolButton(self.horizontalLayoutWidget)
        self.timer_play.setObjectName(u"timer_play")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_play.sizePolicy().hasHeightForWidth())
        self.timer_play.setSizePolicy(sizePolicy)
        icon14 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.timer_play.setIcon(icon14)

        self.horizontalLayout.addWidget(self.timer_play)

        self.timer_pause = QToolButton(self.horizontalLayoutWidget)
        self.timer_pause.setObjectName(u"timer_pause")
        sizePolicy.setHeightForWidth(self.timer_pause.sizePolicy().hasHeightForWidth())
        self.timer_pause.setSizePolicy(sizePolicy)
        icon15 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.timer_pause.setIcon(icon15)

        self.horizontalLayout.addWidget(self.timer_pause)

        self.timer_stop = QToolButton(self.horizontalLayoutWidget)
        self.timer_stop.setObjectName(u"timer_stop")
        sizePolicy.setHeightForWidth(self.timer_stop.sizePolicy().hasHeightForWidth())
        self.timer_stop.setSizePolicy(sizePolicy)
        icon16 = QIcon()
        icon16.addFile(u"icon/chrono32x32_stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.timer_stop.setIcon(icon16)
        self.timer_stop.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.timer_stop)

        self.verticalLayoutWidget = QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 381, 112))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pass_time = QLabel(self.verticalLayoutWidget)
        self.pass_time.setObjectName(u"pass_time")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(True)
        self.pass_time.setFont(font1)
        self.pass_time.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pass_time.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"\n"
"}\n"
"")
        self.pass_time.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.pass_time, 0, 2, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        font2.setItalic(True)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)

        self.remaining_time = QLabel(self.verticalLayoutWidget)
        self.remaining_time.setObjectName(u"remaining_time")
        self.remaining_time.setFont(font1)
        self.remaining_time.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.remaining_time.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"\n"
"}\n"
"")
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

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(870, 130, 401, 121))
        self.formLayoutWidget_3 = QWidget(self.groupBox_4)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 20, 381, 96))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titreLabel = QLabel(self.formLayoutWidget_3)
        self.titreLabel.setObjectName(u"titreLabel")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.titreLabel)

        self.show_title = QLineEdit(self.formLayoutWidget_3)
        self.show_title.setObjectName(u"show_title")
        self.show_title.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.show_title)

        self.descriptionLabel = QLabel(self.formLayoutWidget_3)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.descriptionLabel)

        self.show_desc = QLineEdit(self.formLayoutWidget_3)
        self.show_desc.setObjectName(u"show_desc")
        self.show_desc.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.show_desc)

        self.durETotaleLabel = QLabel(self.formLayoutWidget_3)
        self.durETotaleLabel.setObjectName(u"durETotaleLabel")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.durETotaleLabel)

        self.show_total_time = QTimeEdit(self.formLayoutWidget_3)
        self.show_total_time.setObjectName(u"show_total_time")
        self.show_total_time.setReadOnly(True)
        self.show_total_time.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.show_total_time)

        self.groupBox_5 = QGroupBox(Dialog)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 130, 831, 551))
        self.cue_table_widget = QTableWidget(self.groupBox_5)
        self.cue_table_widget.setObjectName(u"cue_table_widget")
        self.cue_table_widget.setGeometry(QRect(10, 20, 811, 501))
        self.zoom = QToolButton(self.groupBox_5)
        self.zoom.setObjectName(u"zoom")
        self.zoom.setGeometry(QRect(800, 523, 22, 22))
        icon17 = QIcon()
        icon17.addFile(u"icon/vpe32x32_zoom_fit_inc.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoom.setIcon(icon17)
        self.unzoom = QToolButton(self.groupBox_5)
        self.unzoom.setObjectName(u"unzoom")
        self.unzoom.setGeometry(QRect(780, 523, 22, 22))
        icon18 = QIcon()
        icon18.addFile(u"icon/vpe32x32_zoom_fit_dec.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.unzoom.setIcon(icon18)
        self.zoom_spin = QSpinBox(self.groupBox_5)
        self.zoom_spin.setObjectName(u"zoom_spin")
        self.zoom_spin.setGeometry(QRect(710, 523, 67, 24))
        self.zoom_spin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.zoom_spin.setMaximum(1000)
        self.groupBox_6 = QGroupBox(Dialog)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 750, 1261, 101))
        self.TIMELINE = QWidget(self.groupBox_6)
        self.TIMELINE.setObjectName(u"TIMELINE")
        self.TIMELINE.setGeometry(QRect(10, 30, 1241, 61))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(1150, 30, 121, 91))
        icon19 = QIcon()
        icon19.addFile(u"icon/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon19.addFile(u"icon/icon.png", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.pushButton.setIcon(icon19)
        self.pushButton.setIconSize(QSize(100, 100))

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Message du prompteur", None))
        self.prompt_clear.setText(QCoreApplication.translate("Dialog", u"VIDER LE MESSAGE (F1)", None))
        self.prompt_highlight.setText(QCoreApplication.translate("Dialog", u"FAIRE CLIGNOTER (F2)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"LOGS", None))
        self.save_show.setText(QCoreApplication.translate("Dialog", u"Sauvegarde du show", None))
        self.quit.setText(QCoreApplication.translate("Dialog", u"Quitter ", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Quitter", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Sauvegarde", None))
        self.pdf_export.setText(QCoreApplication.translate("Dialog", u"Export PDF", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Export du conducteur", None))
        self.lock.setText(QCoreApplication.translate("Dialog", u"LOCK", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Lock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fichier), QCoreApplication.translate("Dialog", u"Fichier", None))
        self.add_cue.setText(QCoreApplication.translate("Dialog", u"Ajouter un CUE", None))
        self.modify_cue.setText(QCoreApplication.translate("Dialog", u"Modifier le CUE", None))
        self.delete_cue.setText(QCoreApplication.translate("Dialog", u"Supprimer le CUE", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Cues actif", None))
        self.excel_import.setText(QCoreApplication.translate("Dialog", u"Import excel", None))
        self.csv_import.setText(QCoreApplication.translate("Dialog", u"Import CSV", None))
        self.excel_export.setText(QCoreApplication.translate("Dialog", u"Export excel", None))
        self.csv_export.setText(QCoreApplication.translate("Dialog", u"Export CSV", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"import de cue", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"export des cues", None))
        self.delete_all_cues.setText(QCoreApplication.translate("Dialog", u"Tout supprimer", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Supression", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Cues", None))
        self.choixDeLEcranDeSortieLabel.setText(QCoreApplication.translate("Dialog", u"Choix de l'ecran de sortie", None))
        self.modeDIncrustationLabel.setText(QCoreApplication.translate("Dialog", u"Mode d'incrustation ", None))
        self.screen_active.setText(QCoreApplication.translate("Dialog", u"Activer la sortie vid\u00e9o", None))
        self.fullscreen.setText(QCoreApplication.translate("Dialog", u"Plein ecran", None))
        self.prompter_config.setText(QCoreApplication.translate("Dialog", u"Config du prompter", None))
        self.prompt_clear_2.setText(QCoreApplication.translate("Dialog", u"VIDER LE MESSAGE (F1)", None))
        self.prompt_highlight_2.setText(QCoreApplication.translate("Dialog", u"  FAIRE CLIGNOTER (F2)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Message", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Configuration", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Affichage", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Ecran / incrustation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Affichage prompteur", None))
        self.osc_active.setText(QCoreApplication.translate("Dialog", u"Activer l'envoi des commandes OSC", None))
        self.iPDuServeurOSCLabel.setText(QCoreApplication.translate("Dialog", u"IP du serveur OSC", None))
        self.portDuServeurOSCLabel.setText(QCoreApplication.translate("Dialog", u"Port du serveur OSC", None))
        self.osc_ping.setText(QCoreApplication.translate("Dialog", u"Commande /test", None))
        self.osc_config.setText(QCoreApplication.translate("Dialog", u"Config OSC", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Statut de l'envoi OSC", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Configuration serveur cible", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Test OSC", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"OSC", None))
        self.open_logs.setText(QCoreApplication.translate("Dialog", u"Ouvrir les logs", None))
        self.delete_logs.setText(QCoreApplication.translate("Dialog", u"Vider les logs", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Dialog", u"Aide", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Timer global", None))
        self.timer_play.setText(QCoreApplication.translate("Dialog", u"PLAY", None))
        self.timer_pause.setText(QCoreApplication.translate("Dialog", u"PAUSE", None))
        self.timer_stop.setText(QCoreApplication.translate("Dialog", u"STOP", None))
        self.pass_time.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Temps \u00e9coul\u00e9 :", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Temps restant :", None))
        self.remaining_time.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.progressBar.setFormat("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Emission", None))
        self.titreLabel.setText(QCoreApplication.translate("Dialog", u"Titre", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.durETotaleLabel.setText(QCoreApplication.translate("Dialog", u"Dur\u00e9e totale", None))
        self.show_total_time.setDisplayFormat(QCoreApplication.translate("Dialog", u"mm:ss", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Cues actifs", None))
        self.zoom.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.unzoom.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"TIMELINE", None))
        self.pushButton.setText("")
    # retranslateUi


from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QHBoxLayout, QGridLayout, QMessageBox, QDialog, QTimeEdit
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QTime

import database, osc

from ui.ui_new_show import Ui_Dialog
from ui.ui_osc_config import Ui_Dialog as Ui_OSCDialog

class CreateShowDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Créer une nouvelle emmsion")

        self.ui.show_time.setDisplayFormat("mm:ss")
        self.ui.show_time.setTime(QTime(0, 0, 0))  # valeur initiale 00:00

        self.ui.create.clicked.connect(self.create_show)
        self.ui.abort.clicked.connect(self.reject)

    def create_show(self):
        name = self.ui.show_name.text()
        desc = self.ui.show_description.text()

        time = self.ui.show_time.time()
        ms = (time.minute() * 60 + time.second()) * 1000

        if not name or not desc or ms == 0:
            QMessageBox.warning(self, "Config invalide", "Tout les champs ne sont pas remplis, ou le temps de l'emmision est nul.")
            return
        
        database.db.AddShow(name, desc, ms)
        self.accept()

class ModifyShowDialog(QDialog):
    def __init__(self, show_id):
        super().__init__()
        source_show =database.db.GetShowById(show_id)
        self.show_id = show_id

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Modifier une emmsion")

        self.ui.show_time.setDisplayFormat("mm:ss")
        self.ui.show_time.setTime(QTime(0, 0, 0))  # valeur initiale 00:00

        try:
            self.ui.show_name.setText(source_show["nom"])
            self.ui.show_description.setText(source_show["description"])

            total_sec = source_show["duree"] // 1000
            minutes = total_sec // 60
            seconds = total_sec % 60
            self.ui.show_time.setTime(QTime(0, minutes, seconds))

        except Exception as e:
            print(f"Erreur lors du chargement de l'emmsion pour modification: {e}")
            QMessageBox.critical(self, "Erreur", "Impossible de charger les données de l'emmsion pour modification.")
            self.reject()
            return
        
        self.ui.create.clicked.connect(self.modify_show)
        self.ui.abort.clicked.connect(self.reject)

    def modify_show(self):
        name = self.ui.show_name.text()
        desc = self.ui.show_description.text()

        time = self.ui.show_time.time()
        ms = (time.minute() * 60 + time.second()) * 1000

        if not name or not desc or ms == 0:
            QMessageBox.warning(self, "Config invalide", "Tout les champs ne sont pas remplis, ou le temps de l'emmision est nul.")
            return
        
        database.db.ModifyShow(self.show_id, name, desc, ms)
        self.accept()


class ModifyOSCConfigDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OSCDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Configurer la connexion OSC")

        osc_ip, osc_port = database.db.GetOSCConfig()
        if osc_ip and osc_port:
            self.ui.osc_ip.setText(osc_ip)
            self.ui.osc_port.setValue(int(osc_port))

        self.ui.abort.clicked.connect(self.reject)
        self.ui.create.clicked.connect(self.save_config)
        
    def save_config(self):
        osc_port = self.ui.osc_port.value()
        osc_ip = self.ui.osc_ip.text()
        if not osc_ip or not osc_port:
            QMessageBox.warning(self, "Config invalide", "L'IP et le port OSC doivent être saisies.")
            return

        database.db.SetOSCConfig(osc_ip, osc_port)


        #mise a jour de la connexion OSC avec les nouvelles config
        try:
            osc.disconnect_osc_client()
            osc.connect_osc_client()
            
            osc.osc_client.send("/test", "Configuration OSC MAJ") #RETIRER APRES TEST, envoie message bidon pour tester la reconnexion
        except Exception as e:
            print(f"Erreur lors de la mise à jour de la connexion OSC: {e}")
            QMessageBox.critical(self, "Erreur", "La configuration a été sauvegardée, mais la connexion OSC n'a pas pu être mise à jour.")
            self.accept()
            return

        QMessageBox.information(self, "Config sauvegardée", "La configuration OSC a été mise à jour")
        self.accept()


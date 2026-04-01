from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QHBoxLayout, QGridLayout, QMessageBox, QDialog, QTimeEdit
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QTime

import database, osc

from ui.ui_new_show import Ui_Dialog
from ui.ui_osc_config import Ui_Dialog as Ui_OSCDialog
from ui.ui_add_modify_cue import Ui_Dialog as Ui_CueDialog

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


class AddModifyCueDialog(QDialog):
    def __init__(self, action, show_id=None, cue_id=None):
        super().__init__()
        self.ui = Ui_CueDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{action} un cue")

        self.action = action
        self.show_id = show_id
        self.cue_id = cue_id

        self.ui.abort.clicked.connect(self.reject)
        self.ui.validate.clicked.connect(self.save_cue)

        if self.action == 'modifier' and cue_id is not None:
            try:
                cue = database.db.GetCueById(cue_id)
                self.ui.cue_title.setText(cue["nom"])
                self.ui.cue_desc.setText(cue["description"])

                total_sec = cue["temps"] // 1000
                minutes = total_sec // 60
                seconds = total_sec % 60
                self.ui.time.setTime(QTime(0, minutes, seconds))

                self.ui.osc_command.setText(cue["osc_url"])
                try:
                    self.ui.osc_args.setValue(int(cue["osc_args"]))
                except:
                    self.ui.osc_args.setValue(0)
                
                #mettre ici a jour le champs de la couleure du cue 

            except Exception as e:
                print(f"Erreur lors du chargement du cue pour modification: {e}")
                QMessageBox.critical(self, "Erreur", "Impossible de charger les données du cue pour modification.")
                self.reject()
                return
        
    
    def save_cue(self):
        name = self.ui.cue_title.text()
        desc = self.ui.cue_desc.text()
        time = self.ui.time.time()
        ms = (time.minute() * 60 + time.second()) * 1000
        print(f"Temps du cue en ms: {ms}")  # Debug: Affiche le temps converti en millisecondes 
        osc_command = self.ui.osc_command.text()
        osc_args = self.ui.osc_args.value()

        if not name or ms == 0 or not osc_command:
            QMessageBox.warning(self, "Config invalide", "Le nom, le temps et la commande OSC doivent être saisies.")
            return

        if self.action == 'ajouter':
            try:
                database.db.AddCueToShow(database.db.GetActiveShow(), name, desc, ms, osc_command, osc_args, "#161A16")
                self.accept()
            except Exception as e:
                print(f"Erreur lors de l'ajout du cue: {e}")
                QMessageBox.critical(self, "Erreur", "Impossible d'ajouter le cue à la base de données.")
                self.reject()
                return
            
        elif self.action == 'modifier':
            try:
                database.db.ModifyCue(self.cue_id, name, desc, ms, osc_command, osc_args, "#161A16")
                self.accept()
            except Exception as e:
                print(f"Erreur lors de la modification du cue: {e}")
                QMessageBox.critical(self, "Erreur", "Impossible de modifier le cue dans la base de données.")
                self.reject()
                return

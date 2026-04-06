#Projet de prompteur pour le PCP N°... 2026


#Dev : Titouan Gallin
#Contact : titouan.gallin@gmail.com / +33 6 52 75 25 29

#--------------------------------------------------------------------------------------------------------------------

#Fonction a implementer :
# - Interface permetant de creer une emmision OKK
# - Interface de controle de l'emmision : choix de la durée, placement sur le timer de différents événements, lancement des timers... OKK
# - Pour chaques evenements TC, pouvoir envoyer un message OSC a chataigne OKK
# - Preview de l'affichage du prompteur dans la fenetre principale 
# - Saisie d'un message pour l'envoyer au prompteur, affichage en direct (en meme temps que l'on ecrit sur le clavier) OKK
# - Fenetre d'affichage du prompteur en double écran (avec fond pour chromakey ou lumakey) OKK
# - Pour chaques timer, on affiche au dessus un label avec un message du genre "Retour plateau dans..." OKK
# - Possibilitée d'affciher en meme temps plusieurs timers OKK -- RETIREE ENFAIT DANS LA DERNIERE VERSION
# - Pouvoir faire clignoter le texte du prompteur quand un nouveau message a été saisie OKK
# - Rendre plus visible le timers quand le temps arrive au bout (changement de couleur, clignotement...)
# - Avoir contour sur les texte du prompteur -- VOIR COMMENT FAIRE CAR PAS POSSIBLE SUR QT
# - Pouvoir importer depuis excel un conducteur 
# - pas pouvoir modifier tableau d'ajout des shows



#--------------------------------------------------------------------------------------------------------------------
import database, utils, osc
import sys, threading
from ui.ui_main import Ui_MainWindow
from ui.ui_operator import Ui_Dialog as Ui_OperatorDialog
from prompter import PrompterWindow
from prompter_settings_dialog import PrompterSettingsDialog

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QHBoxLayout, QGridLayout, QMessageBox, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtGui import QIcon






class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SHOW TIMER - PCP 2026")
        self.setWindowIcon(QIcon("icon/icon.png"))

        self.update_shows_table() #a la première ouverture, on insere les emmision depuis la base de donnée dans le tableau 
        
        
        self.selected_show_id = None

        ######BARRE DE MENUS######
        self.ui.actionConfig_OSC.triggered.connect(self.change_osc_config) #quand on clique sur le menu de configuration OSC, on affiche la fenetre de configuration OSC
        self.ui.actionConfig_prompter.triggered.connect(self.change_prompter_config) #quand on clique sur le menu de configuration du prompteur, on affiche la fenetre de configuration du prompteur

        ######BOUTON#######
        self.ui.delete_show.clicked.connect(self.delete_show) #quand on clique sur le bouton de suppression d'une emmsion, on appelle la fonction de suppression d'une emmsion dans la db, en lui passant l'id de l'emmsion selectionné.
        self.ui.add_show.clicked.connect(self.create_show) #quand on clique sur le bouton de création d'une emmsion, on affiche la fenetre de création d'une emmsion
        self.ui.modify_show.clicked.connect(self.modify_show) #quand on clique sur le bouton de modification d'une emmsion, on affiche la fenetre de modification d'une emmsion, en lui passant l'id de l'emmsion selectionné.
        self.ui.open_show.clicked.connect(self.open_show) #quand on clique sur le bouton d'ouverture d'une emmsion, on affiche l'interface de controle de l'emmsion

    def update_shows_table(self):
        # Supprime le modèle existant avant de reconstruire
        old_model = self.ui.show_table_view.model()
        if old_model is not None:
            old_model.clear()

        data = database.db.GetAllShows()
        
        if not data:
            return

        columns = list(data[0].keys())

        model = QStandardItemModel(len(data), len(columns))
        model.setHorizontalHeaderLabels(columns)

        for row_idx, row_data in enumerate(data):
            for col_idx, col_name in enumerate(columns):
                value = row_data[col_name]
                
                if col_name == "duree" and value is not None:
                    total_sec = value // 1000
                    minutes = total_sec // 60
                    seconds = total_sec % 60
                    value = f"{minutes:02d}:{seconds:02d}"
                
                item = QStandardItem(str(value))
                model.setItem(row_idx, col_idx, item)

                self.ui.show_table_view.setModel(model)
                self.ui.show_table_view.horizontalHeader().setStretchLastSection(True)
                self.ui.show_table_view.resizeColumnsToContents()

        self.ui.show_table_view.selectionModel().selectionChanged.connect(self.on_show_selected) #reconnecte le signal apres MAJ, sinon plus possible de selec un show...

    def on_show_selected(self): #a chaques clique sur une ligne du tableau, l'id de l'emmision est sauvegardé.
        indexes = self.ui.show_table_view.selectedIndexes()
        if not indexes:
            return

        model = self.ui.show_table_view.model()
        selected_row = indexes[0].row()

        col_names = [model.horizontalHeaderItem(i).text() for i in range(model.columnCount())]
        id_col_index = col_names.index("id")

        self.selected_show_id = model.item(selected_row, id_col_index).text()
        print(f"Emmission sélectionné - ID : {self.selected_show_id}")
    
    def delete_show(self): #fonction appelé quand on clique sur le bouton de suppression d'une emmsion.
        if self.selected_show_id is None:
            QMessageBox.warning(self, "Aucune emmsion sélectionnée", "Veuillez sélectionner une emmsion à supprimer.")
            return
        reply = QMessageBox.question(
        self,
        "Tu confirme chef ?",
        f"Voulez-vous vraiment supprimer l'emmission avec l'id {self.selected_show_id} ?",
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No
    )

        if reply == QMessageBox.Yes:
            print("Suppression confirmée.")
            database.db.DeleteShow(self.selected_show_id)
            self.update_shows_table() #apres la suppression, on met a jour le tableau pour que la suppression soit visible
        else:
            print("Suppression annulée.")

    def create_show(self): #fonction appelé quand on clique sur le bouton de création d'une emmsion, elle affiche la fenetre de création d'une emmsion, et si la creation est validé, on met a jour le tableau pour que la nouvelle emmsion soit visible.

        dialog = utils.CreateShowDialog()
        self.hide()
        if dialog.exec() == QDialog.Accepted:
            self.update_shows_table()
            self.show()
        else:
            print("Création d'emmission annulée.")
            self.show()

    def modify_show(self): #fonction appelé quand on clique sur le bouton de modification d'une emmsion
        if self.selected_show_id is None:
                QMessageBox.warning(self, "Aucune emmsion sélectionnée", "Veuillez sélectionner une emmsion à modifier.")
                return
        dialog = utils.ModifyShowDialog(self.selected_show_id)
        self.hide()
        if dialog.exec() == QDialog.Accepted:
            self.update_shows_table()
            self.show()
        else:
            print("Modification d'emmission annulée.")
            self.show()
    
    def open_show(self):
        if self.selected_show_id is None:
            QMessageBox.warning(self, "Aucune emmsion sélectionnée", "Veuillez sélectionner une emmsion à ouvrir.")
            return
        
        database.db.SetActiveShow(self.selected_show_id)
        self.operator_dialog = OperatorDialog()  
        self.hide()
        self.operator_dialog.show()

    def change_osc_config(self): #interface de changement de la config OSC
        dialog = utils.ModifyOSCConfigDialog()
        #self.hide()
        if dialog.exec() == QDialog.Accepted:
            print("Configuration OSC mise à jour.")
            #self.show()
        else:
            print("Modification de la configuration OSC annulée.")
            #self.show()

    def change_prompter_config(self): #interface de changement des couleurs, timer, etc du prompteur
        dialog = PrompterSettingsDialog(parent=self)
        dialog.exec()

class OperatorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_OperatorDialog()
        self.setWindowFlags(Qt.Window)
        self.ui.setupUi(self)
        self.setWindowTitle("Interface opérateur - SHOW TIMER - PCP 2026")
        self.setWindowIcon(QIcon("icon/icon.png"))
        self.setModal(False)
        

        self.duree_totale_ms = self.get_total_time()
        self.derniere_seconde_affichee = -1
        self.last_next_cues = [] 

        self.load_screens()

        self.config_table()
        self.config_timer()
        self.fill_table()
        self.update_buttons_state("stopped")  # état initial

        self.ui.osc_active.toggled.connect(self.change_osc_activ_state)

        self.load_osc_active_in_ui()


        self.ui.cue_table_widget.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: #00E32A;
                color: white;
            }
        """)



        self.prompteur_window = PrompterWindow(self.timer, self.duree_totale_ms) #fenetre du prompteur
        self.ui.screen_active.toggled.connect(self.checkbox_screen_active) #activer / desactiver l'affichage du prompteur
        self.ui.screen_selection.currentIndexChanged.connect(self.screen_selection_changed) #changer l'ecran d'affichage du prompteur 
        self.ui.fullscreen.toggled.connect(self.fullscreen_state_changed) #activer / desactiver le plein ecran du prompteur

        self.prompteur_window.closed_window.connect(
            lambda: self.ui.screen_active.setChecked(False)
        )

        self.prompteur_window.fullscreen_changed.connect(
            lambda checked: self.ui.fullscreen.setChecked(checked)
        )

        self.ui.prompt_textedit.textChanged.connect(
            lambda: self.prompteur_window.set_prompt_text(self.ui.prompt_textedit.toPlainText())
        )

        #choix de la couleur de fond = mode chroma avec vert et mode luma avec noir
        self.ui.key_mode.addItem("Chroma key (fond vert)", userData="#00FF00")
        self.ui.key_mode.addItem("Luma key (fond noir)",   userData="#000000")

        self.ui.key_mode.currentIndexChanged.connect(self.key_mode_changed)

        #######bouton d'envoie de texte au prompteur########
        self.ui.prompt_highlight.clicked.connect(self.prompteur_window.start_blink)
        self.ui.prompt_clear.clicked.connect(lambda: self.ui.prompt_textedit.clear())

        #########Raccourcis clavier##########
        QShortcut(QKeySequence("F1"), self).activated.connect(self.ui.prompt_textedit.clear)  # Efface le texte du prompteur
        QShortcut(QKeySequence("F2"), self).activated.connect(self.prompteur_window.start_blink)  # Fait clignoter le prompteur


        ########BOURON GESTION DES CUES#############"
        self.ui.add_cue.clicked.connect(lambda: self.add_cue_function())
        self.ui.modify_cue.clicked.connect(lambda: self.modify_cue_function())
        self.ui.delete_cue.clicked.connect(lambda: self.delete_cue_function())

    ###################PARAMETRE DU PROMPTEUR########################################3
    def checkbox_screen_active(self, checked):
        if checked:
            self.prompteur_window.show()
        else:
            self.prompteur_window.hide()

    def screen_selection_changed(self, index):
        self.prompteur_window.set_screen(self.ui.screen_selection.currentData())

    def fullscreen_state_changed(self, checked):
        self.prompteur_window.set_fullscreen(checked)

    def key_mode_changed(self, index):
        color = self.ui.key_mode.currentData()
        self.prompteur_window.set_background_color(color)


    ##################ACTIVATION OU NON DE L'ENVOIE OSC#################################
    def change_osc_activ_state(self, state):
        state = self.ui.osc_active.isChecked()
        if state == True:
            database.db.SetOSCState("True")
        else:
            database.db.SetOSCState("False")

    def load_osc_active_in_ui(self):
        state = database.db.GetOSCState()
        if state == "True":
            state = True
            self.ui.osc_active.setChecked(state)
        else:
            state = False
            self.ui.osc_active.setChecked(state)





    #####################################################################################
    def add_cue_function(self):
        if utils.AddModifyCueDialog("ajouter").exec():
            cues = database.db.GetAllCuesFromShow(database.db.GetActiveShow()) or []
            self.timer.set_cues(cues)
            self.fill_table()  # rafraîchit le tableau après l'ajout d'un cue

    def modify_cue_function(self):
        if self.selected_cue_id is None:
            QMessageBox.warning(self, "Aucun cue sélectionné", "Veuillez sélectionner un cue à modifier.")
            return

        dialog = utils.AddModifyCueDialog("modifier", cue_id=self.selected_cue_id)
        if dialog.exec():
            cues = database.db.GetAllCuesFromShow(database.db.GetActiveShow()) or []
            self.timer.set_cues(cues)
            self.fill_table()  # rafraîchit le tableau après la modification d'un cue

    def delete_cue_function(self):
        if self.selected_cue_id is None:
            QMessageBox.warning(self, "Aucun cue sélectionné", "Veuillez sélectionner un cue à supprimer.")
            return

        reply = QMessageBox.question(
            self,
            "Confirmer la suppression",
            f"Voulez-vous vraiment supprimer le cue avec l'id {self.selected_cue_id} ?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            print("Suppression confirmée.")
            database.db.DeleteCue(self.selected_cue_id)
            cues = database.db.GetAllCuesFromShow(database.db.GetActiveShow()) or []
            self.timer.set_cues(cues)
            self.fill_table()  # rafraîchit le tableau après la suppression d'un cue
        else:
            print("Suppression annulée.")

    
    def update_buttons_state(self, etat):
        """
        Gère l'état des boutons selon la situation du timer.
        etat possible : "stopped", "running", "paused"
        """
        if etat == "stopped":
            self.ui.timer_play.setEnabled(True)
            self.ui.timer_pause.setEnabled(False)
            self.ui.timer_stop.setEnabled(False)

        elif etat == "running":
            self.ui.timer_play.setEnabled(False)
            self.ui.timer_pause.setEnabled(True)
            self.ui.timer_stop.setEnabled(True)

        elif etat == "paused":
            self.ui.timer_play.setEnabled(True)   # permet de reprendre
            self.ui.timer_pause.setEnabled(False)
            self.ui.timer_stop.setEnabled(True)

    def config_table(self):
        from PySide6.QtWidgets import QTableWidget, QHeaderView
        self.ui.cue_table_widget.setColumnCount(6)
        self.ui.cue_table_widget.setHorizontalHeaderLabels(["Nom", "Description", "Déclenchement", "URL OSC", "Args OSC", "Dans"])
        self.ui.cue_table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.ui.cue_table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.cue_table_widget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.ui.cue_table_widget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.ui.cue_table_widget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.ui.cue_table_widget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.ui.cue_table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.cue_table_widget.setSelectionBehavior(QTableWidget.SelectRows)

        self.selected_cue_id = None
        self.ui.cue_table_widget.itemSelectionChanged.connect(self.on_cue_selected)

    def config_timer(self):
        from timer import PrompteurTimer
        self.timer = PrompteurTimer(self)

        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(self.duree_totale_ms)
        self.ui.progressBar.setValue(0)

        show_id = database.db.GetActiveShow()
        if show_id is not None:
            cues = database.db.GetAllCuesFromShow(show_id) or []
            self.timer.set_cues(cues)

        self.timer.updated_time.connect(self.on_timer_updated)
        self.timer.two_next_cues.connect(self.on_next_cue)
        self.timer.fired_cue.connect(self.on_cue_fired)

        self.ui.timer_play.clicked.connect(self.on_play_clicked)
        self.ui.timer_pause.clicked.connect(self.on_pause_clicked)
        self.ui.timer_stop.clicked.connect(self.on_stop_clicked)

    def fill_table(self):
        from PySide6.QtWidgets import QTableWidgetItem
        from PySide6.QtGui import QColor

        self.ui.cue_table_widget.setRowCount(0)

        show_id = database.db.GetActiveShow()
        if show_id is None:
            return

        cues = database.db.GetAllCuesFromShow(show_id) or []

        for cue in sorted(cues, key=lambda c: c["temps"]):
            ligne = self.ui.cue_table_widget.rowCount()
            self.ui.cue_table_widget.insertRow(ligne)

            h = cue["temps"] // 3600000
            m = (cue["temps"] % 3600000) // 60000
            s = (cue["temps"] % 60000) // 1000

            self.ui.cue_table_widget.setItem(ligne, 0, QTableWidgetItem(cue["nom"]))
            self.ui.cue_table_widget.setItem(ligne, 1, QTableWidgetItem(cue.get("description", "")))
            self.ui.cue_table_widget.setItem(ligne, 2, QTableWidgetItem(f"{h:02d}:{m:02d}:{s:02d}"))
            self.ui.cue_table_widget.setItem(ligne, 3, QTableWidgetItem(cue.get("osc_url", "") or ""))
            self.ui.cue_table_widget.setItem(ligne, 4, QTableWidgetItem(str(cue.get("osc_args", "") or "")))
            self.ui.cue_table_widget.setItem(ligne, 5, QTableWidgetItem("--:--:--"))

            self.ui.cue_table_widget.item(ligne, 0).setData(Qt.UserRole,     cue["temps"])
            self.ui.cue_table_widget.item(ligne, 0).setData(Qt.UserRole + 1, cue["cue_id"])

            if cue.get("color"):
                couleur = QColor(cue["color"])
                for colonne in range(self.ui.cue_table_widget.columnCount()):
                    self.ui.cue_table_widget.item(ligne, colonne).setBackground(couleur)

            #les bouton sont par defaut desactivé
            self.ui.modify_cue.setEnabled(False)
            self.ui.delete_cue.setEnabled(False)

    def on_cue_selected(self):
        ligne = self.ui.cue_table_widget.currentRow()
        if ligne < 0:
            self.selected_cue_id = None
            return
        item_nom = self.ui.cue_table_widget.item(ligne, 0)
        if item_nom:
            self.selected_cue_id = item_nom.data(Qt.UserRole + 1)
            print(f"Cue sélectionné - ID : {self.selected_cue_id}")

            #quand un cue est sélectionné, on active les boutons de modification et de suppression de cue
            self.ui.modify_cue.setEnabled(True)
            self.ui.delete_cue.setEnabled(True)

    ###################################BOUTON###############################################3

    def on_play_clicked(self):
        if self.timer.running:
            return

        if self.timer.timeline_time > 0:
            self.timer.resume()
        else:
            self.last_next_cues = []  # ← reset pour forcer le re-coloriage
            self.fill_table()         # ← reremplit le tableau
            self.timer.start(0)

        self.update_buttons_state("running")

    def on_pause_clicked(self):
        """Demande une confirmation avant de mettre en pause."""
        if not self.timer.running:
            return

        reponse = QMessageBox.question(
            self,
            "Mettre en pause ?",
            "Voulez-vous mettre le timer en pause ?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reponse == QMessageBox.Yes:
            self.timer.pause()
            self.update_buttons_state("paused")

    def on_stop_clicked(self):
        reponse = QMessageBox.question(
                self,
                "Arrêter le timer ?",
                "Voulez-vous arrêter et remettre le timer à zéro ?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

        if reponse == QMessageBox.No:
            return

        self.timer.stop()
        self.update_buttons_state("stopped")
        self.derniere_seconde_affichee = -1
        self.ui.pass_time.setText("00:00:00")
        self.ui.remaining_time.setText("00:00:00")
        self.ui.remaining_time.setStyleSheet("")
        self.ui.progressBar.setValue(0)

        show_id = database.db.GetActiveShow()
        if show_id is not None:
            cues = database.db.GetAllCuesFromShow(show_id) or []
            self.timer.set_cues(cues)  # ← recharge les cues après le stop

        self.fill_table()

    #######################TIMER############################################3

    def on_timer_updated(self, temps_ms):
        from PySide6.QtGui import QColor

        seconde_actuelle = temps_ms // 1000

        self.ui.progressBar.setValue(temps_ms)

        if seconde_actuelle == self.derniere_seconde_affichee:
            return
        self.derniere_seconde_affichee = seconde_actuelle

        h = temps_ms // 3600000
        m = (temps_ms % 3600000) // 60000
        s = (temps_ms % 60000) // 1000
        self.ui.pass_time.setText(f"{h:02d}:{m:02d}:{s:02d}")

        restant = max(0, self.duree_totale_ms - temps_ms)
        h = restant // 3600000
        m = (restant % 3600000) // 60000
        s = (restant % 60000) // 1000
        self.ui.remaining_time.setText(f"{h:02d}:{m:02d}:{s:02d}")

        if restant < 60_000:
            self.ui.remaining_time.setStyleSheet("color: red;")
        else:
            self.ui.remaining_time.setStyleSheet("")

        if restant == 0:
            self.timer.stop()
            self.update_buttons_state("stopped")

        self.ui.cue_table_widget.setUpdatesEnabled(False)

        for ligne in range(self.ui.cue_table_widget.rowCount()):
            item_nom = self.ui.cue_table_widget.item(ligne, 0)
            if item_nom is None:
                continue
            temps_cue = item_nom.data(Qt.UserRole)
            dans_ms   = temps_cue - temps_ms
            if dans_ms <= 0:
                self.ui.cue_table_widget.item(ligne, 5).setText("passé")
            else:
                h = dans_ms // 3600000
                m = (dans_ms % 3600000) // 60000
                s = (dans_ms % 60000) // 1000
                self.ui.cue_table_widget.item(ligne, 5).setText(f"{h:02d}:{m:02d}:{s:02d}")


        self.ui.cue_table_widget.setUpdatesEnabled(True)

    def on_cue_fired(self, cue):
        from PySide6.QtGui import QColor

        for ligne in range(self.ui.cue_table_widget.rowCount()):
            item_nom = self.ui.cue_table_widget.item(ligne, 0)
            if item_nom and item_nom.data(Qt.UserRole) == cue["temps"]:
                # On grise définitivement le fond de ce cue
                for colonne in range(self.ui.cue_table_widget.columnCount()):
                    item = self.ui.cue_table_widget.item(ligne, colonne)
                    if item:
                        item.setBackground(QColor("gray"))
                        item.setForeground(QColor("white"))
                self.ui.cue_table_widget.scrollToItem(item_nom)
                break

        print(f"[CUE] {cue['nom']} déclenché à {cue['temps']}ms")

    def on_next_cue(self, cues):
        from PySide6.QtGui import QColor

        new_ids = [c["cue_id"] for c in cues]
        old_ids = [c["cue_id"] for c in self.last_next_cues]
        if new_ids == old_ids:
            return

        self.last_next_cues = cues

        self.ui.cue_table_widget.setUpdatesEnabled(False)

        temps_actuel = self.timer.actual_time()

        for ligne in range(self.ui.cue_table_widget.rowCount()):
            item_nom = self.ui.cue_table_widget.item(ligne, 0)
            if item_nom is None:
                continue

            temps_cue = item_nom.data(Qt.UserRole)

            for colonne in range(self.ui.cue_table_widget.columnCount()):
                item = self.ui.cue_table_widget.item(ligne, colonne)
                if item:
                    if temps_cue <= temps_actuel:
                        item.setForeground(QColor("darkGray"))
                    else:
                        item.setForeground(QColor("white"))

        for cue in cues:
            for ligne in range(self.ui.cue_table_widget.rowCount()):
                item_nom = self.ui.cue_table_widget.item(ligne, 0)
                if item_nom and item_nom.data(Qt.UserRole) == cue["temps"]:
                    for colonne in range(self.ui.cue_table_widget.columnCount()):
                        item = self.ui.cue_table_widget.item(ligne, colonne)
                        if item:
                            item.setForeground(QColor("orange"))

        self.ui.cue_table_widget.setUpdatesEnabled(True)

    def get_total_time(self):
        show_id = database.db.GetActiveShow()
        if show_id is None:
            return 0
        show = database.db.GetShowById(show_id)
        return show["duree"] if show else 0
    
    def load_screens(self): #charge les ecran disponibles

        ecrans = QApplication.screens()
        
        self.ui.screen_selection.clear()
        
        for i, ecran in enumerate(ecrans):
            nom = ecran.name()
            resolution = ecran.geometry()
            self.ui.screen_selection.addItem(
                f"Écran {i} - {nom} ({resolution.width()}x{resolution.height()})",
                userData=i  # on stocke le numéro de l'écran dans le userData
            )

    def closeEvent(self, event):
        reponse = QMessageBox.question(
            self,
            "Fermer ?",
            "Voulez-vous fermer l'interface opérateur ?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reponse == QMessageBox.Yes:
            if self.timer.running:
                self.timer.stop()
            self.prompteur_window.hide()
            from PySide6.QtWidgets import QApplication
            for widget in QApplication.topLevelWidgets():
                if isinstance(widget, MainWindow):
                    widget.show()
                    break
            event.accept()
        else:
            event.ignore()
    

if __name__ == "__main__":
    database.connect_db() #Connexion a la base de donnée sqlite
    osc.connect_osc_client() #Connexion au client OSC, pour pouvoir envoyer des messages OSC a chataigne

    #database.db.AddCueToShow(1, "Test Cue 2", "Description du cue 2", 130000, "/test/cue2", "arg1 arg2", "#189E35") #ajout de cue de test dans la base de donnée, pour pouvoir tester l'interface de controle et le timer



    



    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon/icon.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

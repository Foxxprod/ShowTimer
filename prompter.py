from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMenu
from ui.ui_prompter import Ui_Dialog as Ui_PrompterDialog
from PySide6.QtCore import Signal
from PySide6.QtCore import QTimer
import database
from utils import LabelWithOutline

#classe de la fenetre du prompteur
#v modif avec  plus de label classique pour avoir des contours
#Par contre pas reussi a appliquer la meme chose pour le texte de message...
class PrompterWindow(QWidget):
    closed_window = Signal()
    fullscreen_changed = Signal(bool)

    def __init__(self, timer, duree_totale_ms, parent=None):
        super().__init__(parent)
        self.ui = Ui_PrompterDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window)

        self.ui.prompt_text.setAlignment(Qt.AlignCenter)

        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint) #permet de ne pas avoir les bouton en haut de la fenetre pour ne pas avoir de bouton de fermeture

        self.timer = timer #instance du timer de l'emission, passé a la creation de la fenetre
        self.duree_totale_ms = duree_totale_ms #duree totale du show, present dans la bdd

        self._setup_custom_labels() #remplace les widget vide par les custom avec lignes de contour
        self._connecter_signaux() #connecte les signauc pour recevoir les infos du timer

        for widget in self.findChildren(QWidget):
            widget.setContextMenuPolicy(Qt.NoContextMenu)

        ######GESTION DU CLIGNOTEMENT (prompt_text)###################
        self.blink_timer = QTimer(self)
        self.blink_timer.setInterval(300)
        self.blink_timer.timeout.connect(self._on_blink_tick)

        self.blink_stop_timer = QTimer(self)
        self.blink_stop_timer.setSingleShot(True)
        self.blink_stop_timer.timeout.connect(self._stop_blink)

        self.blink_state = False
        self._cfg_text_size = "60"
        self._cfg_text_color = "#B8860B"

        ######GESTION DU CLIGNOTEMENT (next_cue_label)###############
        self.cue_blink_timer = QTimer(self)
        self.cue_blink_timer.timeout.connect(self._on_cue_blink_tick)
        self.cue_blink_state = False
        self.cue_blink_mode = None   # None | "first" | "second" | "third"
        self.cue_blink_color = QColor("white")

        # Valeurs de config chargées depuis la BDD à chaque ouverture, ca c'est des val par defaut
        self.cfg_blink_first_time  = 20000
        self.cfg_blink_second_time = 10000
        self.cfg_blink_third_time  = 5000
        self.cfg_blink_first_color  = QColor("#00CC00")
        self.cfg_blink_second_color = QColor("#FF8800")
        self.cfg_blink_third_color  = QColor("#FF0000")
        self.cfg_next_cue_base_color = QColor("white")

        self._reset_affichage() #remet a zero l'affichage

    ######################CHARGEMENT CONFIG BDD##############################

    def showEvent(self, event):
        self._apply_config()
        super().showEvent(event)

    def _apply_config(self): #appluqe la config depuis la bdd
        c = database.db.GetPrompterConfig()

        self._cfg_text_size = c['prompter_text_size']
        self._cfg_text_color = c['prompter_text_color']

        # Texte principal
        self.ui.prompt_text.setStyleSheet(f"""
            QTextEdit {{
                font-size: {self._cfg_text_size}px;
                font-weight: bold;
                color: {self._cfg_text_color};
                background-color: transparent;
                border: none;
                line-height: 80%;
            }}
        """)

        # Labels avec contour
        self.next_cue_label.set_font_size(int(c["next_cue_text_size"]))
        self.next_cue_label.set_outline_width(int(c["next_cue_outline_width"]))
        self.cfg_next_cue_base_color = QColor(c["next_cue_text_color"])
        if self.cue_blink_mode is None:
            self.next_cue_label.set_color(self.cfg_next_cue_base_color)

        self.second_cue_label.set_font_size(int(c["second_cue_text_size"]))
        self.second_cue_label.set_color(QColor(c["second_cue_text_color"]))
        self.second_cue_label.set_outline_width(int(c["second_cue_outline_width"]))

        self.clock_label.set_font_size(int(c["clock_text_size"]))
        self.clock_label.set_color(QColor(c["clock_text_color"]))
        self.clock_label.set_outline_width(int(c["clock_outline_width"]))

        # Seuils et couleurs de clignotement
        self.cfg_blink_first_time   = int(c["blink_first_time"])
        self.cfg_blink_second_time  = int(c["blink_second_time"])
        self.cfg_blink_third_time   = int(c["blink_third_time"])
        self.cfg_blink_first_color  = QColor(c["blink_first_color"])
        self.cfg_blink_second_color = QColor(c["blink_second_color"])
        self.cfg_blink_third_color  = QColor(c["blink_third_color"])

        # Reset du mode de clignotement pour appliquer les nouvelles couleurs
        self.cue_blink_mode = None

    ######################REMPLACEMENT DES WIDGETS GENERIQUES################

    def _replace_widget(self, old_widget, new_widget):
        layout = self.ui.verticalLayout
        idx = layout.indexOf(old_widget)
        sp = old_widget.sizePolicy()
        min_h = old_widget.minimumHeight()
        layout.removeWidget(old_widget)
        old_widget.deleteLater()
        new_widget.setSizePolicy(sp)
        new_widget.setMinimumHeight(min_h)
        layout.insertWidget(idx, new_widget)

    def _setup_custom_labels(self):
        self.second_cue_label = LabelWithOutline("", QColor("#aaaaaa"), 28, parent=self)
        self._replace_widget(self.ui.second_cue, self.second_cue_label)

        self.next_cue_label = LabelWithOutline("", QColor("white"), 42, parent=self)
        self._replace_widget(self.ui.next_cue, self.next_cue_label)

        self.clock_label = LabelWithOutline("", QColor("white"), 28, parent=self)
        self._replace_widget(self.ui.clock_label, self.clock_label)

    ######################CONFIG DU PROMPTEUR################################

    def set_screen(self, screen_index): #permet de choisir sur quel ecran on affiche a partir de l'index de l'ecran 
        ecrans = QApplication.screens()

        if screen_index < len(ecrans):
            ecran_cible = ecrans[screen_index]
        else:
            print(f"Pas reussi a trouve l'ecran {screen_index}, utilisation de l'écran principal.")
            ecran_cible = ecrans[0]

        self.setGeometry(ecran_cible.geometry())

    def set_fullscreen(self, fullscreen): #permet de mettre la fenetre en plein ecran, bien sans les bordures 
        if fullscreen:
            self.showFullScreen()
        else:
            self.showNormal()
        self.fullscreen_changed.emit(fullscreen)

    def set_background_color(self, couleur): #changer la couleure de fond entre vert ou noir
        #soit on veut faire du chroma ou du luma
        #Faire en sorte de pouvoir chganger la couleure de fond du chroma plus tard, si on veut par ex du bleu a la place du vert
        #Car actuellement j'ai peur que en clignotant vert, le texte soit incrusté
        self.setStyleSheet(f"background-color: {couleur};")

    def contextMenuEvent(self, event): #petit menu clic droit pour fermer ou passer en plein ecran 
        #avant ca c'etait pas simple de fermer si on metait en plein ecran par erreur sur le meme ecran que l'ope ui
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: #2b2b2b;
                color: white;
                border: 1px solid #555555;
            }
            QMenu::item:selected {
                background-color: #505050;
            }
        """)

        action_fullscreen = menu.addAction("Activer plein écran" if not self.isFullScreen() else "Désactiver plein écran")
        action_fullscreen.triggered.connect(lambda: self.set_fullscreen(not self.isFullScreen()))

        menu.addSeparator()

        action_fermer = menu.addAction("Fermer")
        action_fermer.triggered.connect(self.hide)

        menu.exec(event.globalPos())

    def hideEvent(self, event):
        self.closed_window.emit()
        super().hideEvent(event)

    def _connecter_signaux(self): #connecter les signaux du timer
        self.timer.updated_time.connect(self.on_updated_time)
        self.timer.two_next_cues.connect(self.on_two_next_cues)

    def _reset_affichage(self): #remet a zero l'affichage
        self.cue_blink_timer.stop()
        self.cue_blink_mode = None
        self.cue_blink_state = False
        self.next_cue_label.set_color(self.cfg_next_cue_base_color)
        self.next_cue_label.set_text("")
        self.second_cue_label.set_text("")
        self.clock_label.set_text("")

    def set_prompt_text(self, texte): #changer le texte de message du prompt
        self.ui.prompt_text.setPlainText(texte)
        self.ui.prompt_text.setAlignment(Qt.AlignCenter)

    @Slot(int) #met a jour le temps ecoulé et restant 
    def on_updated_time(self, temps_ms):
        #c'est le ecoulé qui est passé en paramètre 
        h_e = temps_ms // 3600000
        m_e = (temps_ms % 3600000) // 60000
        s_e = (temps_ms % 60000) // 1000

        #faut recalculer le restant a partir du temps total
        restant = max(0, self.duree_totale_ms - temps_ms)
        h_r = restant // 3600000
        m_r = (restant % 3600000) // 60000
        s_r = (restant % 60000) // 1000

        self.clock_label.set_text(
            f"Écoulé : {h_e:02d}:{m_e:02d}:{s_e:02d}     Restant : {h_r:02d}:{m_r:02d}:{s_r:02d}"
        )

    #afficher les deux cues suivants
    #Au final on a enlevé un des deux label, ca faisait trop d'infos a l'ecran
    #si besoin de remettre suffit de decommenter
    @Slot(list)
    def on_two_next_cues(self, cues):
        if len(cues) >= 1:
            cue1 = cues[0]
            temps_dans = max(0, cue1["temps"] - self.timer.actual_time())
            h = temps_dans // 3600000
            m = (temps_dans % 3600000) // 60000
            s = (temps_dans % 60000) // 1000
            self.next_cue_label.set_text(f"{cue1['nom']} : {h:02d}:{m:02d}:{s:02d}")
            self._update_cue_blink(temps_dans)
        else:
            self.next_cue_label.set_text("")
            self._update_cue_blink(None)
        """
        if len(cues) >= 2:
            cue2 = cues[1]
            temps_dans = max(0, cue2["temps"] - self.timer.actual_time())
            h = temps_dans // 3600000
            m = (temps_dans % 3600000) // 60000
            s = (temps_dans % 60000) // 1000
            self.second_cue_label.set_text(f"{cue2['nom']} : {h:02d}:{m:02d}:{s:02d}")
        else:
            self.second_cue_label.set_text("")
        """

    def _update_cue_blink(self, temps_dans_ms): #fais le clignotement des cues
        """Détermine le mode de clignotement selon le temps restant avant le cue."""
        if temps_dans_ms is None or temps_dans_ms > self.cfg_blink_first_time:
            new_mode = None
            interval = None
        elif temps_dans_ms <= self.cfg_blink_third_time:
            new_mode = "third"
            interval = 250
        elif temps_dans_ms <= self.cfg_blink_second_time:
            new_mode = "second"
            interval = 450
        else:
            new_mode = "first"
            interval = 800

        if new_mode == self.cue_blink_mode:
            return

        self.cue_blink_mode = new_mode
        self.cue_blink_state = False
        self.cue_blink_timer.stop()

        if new_mode is None:
            self.next_cue_label.set_color(self.cfg_next_cue_base_color)
        else:
            colors = {
                "first":  self.cfg_blink_first_color,
                "second": self.cfg_blink_second_color,
                "third":  self.cfg_blink_third_color,
            }
            self.cue_blink_color = colors[new_mode]
            self.cue_blink_timer.setInterval(interval)
            self.cue_blink_timer.start()

    def _on_cue_blink_tick(self):
        self.cue_blink_state = not self.cue_blink_state
        if self.cue_blink_state:
            self.next_cue_label.set_color(self.cue_blink_color)
        else:
            self.next_cue_label.set_color(self.cfg_next_cue_base_color)

    ######################GESTION DU CLIGNOTEMENT###########################
    def start_blink(self): #permet de faire clignoter le message pendant 5s
        self.blink_state = False
        self.blink_timer.start()
        self.blink_stop_timer.start(5000)

    def _on_blink_tick(self):
        self.blink_state = not self.blink_state
        if self.blink_state:
            self.ui.prompt_text.setStyleSheet(f"""
                QTextEdit {{
                    font-size: {self._cfg_text_size}px;
                    font-weight: bold;
                    color: #000000;
                    background-color: #FF0000;
                    border: none;
                    line-height: 80%;
                }}
            """)
        else:
            #reprend bien les valeure de la base dans l'etat normal
            self.ui.prompt_text.setStyleSheet(f"""
                QTextEdit {{
                    font-size: {self._cfg_text_size}px;
                    font-weight: bold;
                    color: {self._cfg_text_color};
                    background-color: transparent;
                    border: none;
                    line-height: 80%;
                }}
            """)

    def _stop_blink(self): #quand on arrete on reprend les valeure de la base
        self.blink_timer.stop()
        self.blink_state = False
        self.ui.prompt_text.setStyleSheet(f"""
            QTextEdit {{
                font-size: {self._cfg_text_size}px;
                font-weight: bold;
                color: {self._cfg_text_color};
                background-color: transparent;
                border: none;
                line-height: 80%;
            }}
        """)
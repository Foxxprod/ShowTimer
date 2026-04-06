from PySide6.QtWidgets import QDialog, QApplication, QWidget
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QContextMenuEvent
from PySide6.QtWidgets import QMenu
from zope import event
from ui.ui_prompter import Ui_Dialog as Ui_PrompterDialog
from PySide6.QtCore import Signal
from PySide6.QtCore import QTimer


class PrompterWindow(QWidget):
    closed_window = Signal()
    fullscreen_changed = Signal(bool)

    def __init__(self, timer, duree_totale_ms, parent=None):
        super().__init__(parent)
        self.ui = Ui_PrompterDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window)

        self.ui.prompt_text.setAlignment(Qt.AlignCenter)

        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint)


        self.timer = timer
        self.duree_totale_ms = duree_totale_ms

        self._connecter_signaux()
        self._reset_affichage()

        for widget in self.findChildren(QWidget):
            widget.setContextMenuPolicy(Qt.NoContextMenu)



        ######GESTION DU CLOGNOTEMENT###################
        self.blink_timer = QTimer(self)
        self.blink_timer.setInterval(300)  # clignote toutes les 300ms
        self.blink_timer.timeout.connect(self._on_blink_tick)
        
        self.blink_stop_timer = QTimer(self)
        self.blink_stop_timer.setSingleShot(True)
        self.blink_stop_timer.timeout.connect(self._stop_blink)
        
        self.blink_state = False  # état actuel du clignotement

    ######################CONFIG DU PROMPTEUR################################

    def set_screen(self, screen_index):
        """Change l'écran sur lequel la fenêtre est affichée."""
        ecrans = QApplication.screens()

        if screen_index < len(ecrans):
            ecran_cible = ecrans[screen_index]
        else:
            print(f"Pas reussi a trouve l'ecran {screen_index}, utilisation de l'écran principal.")
            ecran_cible = ecrans[0]

        self.setGeometry(ecran_cible.geometry())

    def set_fullscreen(self, fullscreen):
        if fullscreen:
            self.showFullScreen()
        else:
            self.showNormal()
        self.fullscreen_changed.emit(fullscreen)

    def set_background_color(self, couleur): #changement de la couleur de fond du prompteur, pour le mode chroma key ou luma key
        self.setStyleSheet(f"background-color: {couleur};")

    
    #clic droit permet de la fermer 
    def contextMenuEvent(self, event):
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
        self.closed_window.emit()  # ← émis à chaque hide()
        super().hideEvent(event)

    #affichage des données du timer
    def _connecter_signaux(self):
        self.timer.updated_time.connect(self.on_updated_time)
        self.timer.two_next_cues.connect(self.on_two_next_cues)

    def _reset_affichage(self):
        self.ui.next_cue.setText("")
        self.ui.second_cue.setText("")
        self.ui.show_remain_time.setText("")

    def set_prompt_text(self, texte): #changement du texte du prompteur
        self.ui.prompt_text.setPlainText(texte)

    @Slot(int)
    def on_updated_time(self, temps_ms):
        # Temps écoulé
        h_e = temps_ms // 3600000
        m_e = (temps_ms % 3600000) // 60000
        s_e = (temps_ms % 60000) // 1000

        # Temps restant
        restant = max(0, self.duree_totale_ms - temps_ms)
        h_r = restant // 3600000
        m_r = (restant % 3600000) // 60000
        s_r = (restant % 60000) // 1000

        self.ui.show_remain_time.setText(
            f"Écoulé : {h_e:02d}:{m_e:02d}:{s_e:02d}     Restant : {h_r:02d}:{m_r:02d}:{s_r:02d}"
        )

    @Slot(list)
    def on_two_next_cues(self, cues):
        if len(cues) >= 1:
            cue1 = cues[0]
            temps_dans = max(0, cue1["temps"] - self.timer.actual_time())
            h = temps_dans // 3600000
            m = (temps_dans % 3600000) // 60000
            s = (temps_dans % 60000) // 1000
            self.ui.next_cue.setText(f"{cue1['nom']} : {h:02d}:{m:02d}:{s:02d}")
        else:
            self.ui.next_cue.setText("")
        """
        if len(cues) >= 2:
            cue2 = cues[1]
            temps_dans = max(0, cue2["temps"] - self.timer.actual_time())
            h = temps_dans // 3600000
            m = (temps_dans % 3600000) // 60000
            s = (temps_dans % 60000) // 1000
            self.ui.second_cue.setText(f"{cue2['nom']} : {h:02d}:{m:02d}:{s:02d}")
        else:
            self.ui.second_cue.setText("")

        """

    ######################GESTION DU CLIGNOTEMENT###########################
    def start_blink(self):
        """Démarre le clignotement pendant 5 secondes."""
        self.blink_state = False
        self.blink_timer.start()
        self.blink_stop_timer.start(5000)  # arrête après 5 secondes

    def _on_blink_tick(self):
        self.blink_state = not self.blink_state
        if self.blink_state:
            self.ui.prompt_text.setStyleSheet("""
                QTextEdit {
                    font-size: 60px;
                    font-weight: bold;
                    color: #000000;
                    background-color: #FF0000;
                    border: none;
                    line-height: 80%;
                }
            """)
        else:
            self.ui.prompt_text.setStyleSheet("""
                QTextEdit {
                    font-size: 60px;
                    font-weight: bold;
                    color: #B8860B;
                    background-color: transparent;
                    border: none;
                    line-height: 80%;
                }
            """)

    def _stop_blink(self):
        self.blink_timer.stop()
        self.blink_state = False
        self.ui.prompt_text.setStyleSheet("""
            QTextEdit {
                font-size: 60px;
                font-weight: bold;
                color: #B8860B;
                background-color: transparent;
                border: none;
                line-height: 80%;
            }
        """)
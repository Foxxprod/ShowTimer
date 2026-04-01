import time
from PySide6.QtCore import QObject, QTimer, Signal


class PrompteurTimer(QObject):

    updated_time = Signal(int)   # temps courant en ms
    two_next_cues = Signal(list)  # liste des 2 prochains cues à venir, utilsé dans l'interface pour affichage des deux lign
    fired_cue = Signal(dict)  # cue qui vient d'être déclenché

    def __init__(self, parent=None):
        super().__init__(parent)

        self.cues_list = [] #liste des cues provenenant de la bdd
        self.system_start_hour = None #heure pc au declanchement ou reprise, pour s'assurer de ne pas avoir de derive du timer
        self.timeline_time = 0 #position actuelle dans la timeline
        self.last_verified_time = -1 #dernier temps en memoire, utilisé pour reverifer le cu a declencher a partir de ce temps
        self.running = False #etat du timer, pour savoir si on est en pause ou en marche


        self.timer = QTimer(self) #timer 
        self.timer.setInterval(50) #tick toutes les 50ms 
        self.timer.timeout.connect(self.on_tick) #appel de la fonction on_tick a chaque tick du timer, le temps est calculé depuis l'heure systeme


    def set_cues(self, cues): #ajouter les cues dans la classe timer
        sorted_cues = sorted(cues, key=lambda c: c["temps"])

        #on retire les cue deja passé dans le timer
        #sinon quand on ajoute des cue bah ca declenche ceux deja passé
        self.cues_list = [
            cue for cue in sorted_cues
            if cue["temps"] > self.timeline_time
        ]

    def start(self, start_offset_ms=0):
        self.system_start_hour = time.perf_counter()
        self.timeline_time = start_offset_ms   
        self.last_verified_time = start_offset_ms - 1
        self.running = True
        self.timer.start()

    
    def stop(self): #stop complet du timer, remet a zero. 
        #!!!!! faire en sorte que l'interface demande une confirmation avant de faire ca, pour eviter les fausse manip de l'op / script
        position_actuelle = self.actual_time()  # on sauvegarde avant d'arrêter
        self.timer.stop()
        self.running = False
        self.system_start_hour = None
        self.last_verified_time = position_actuelle  
        self.timeline_time = 0    


    def pause(self): #pause, c'est juste un stop mais on garde en memoire le temps actuel du timer pour pouvoir reprendre ensuite
        if self.running:
            self.timeline_time = self.actual_time()
            self.system_start_hour = None
            self.timer.stop()
            self.running = False

    def resume(self): #reprendre le timer a partir du temps de pause 
        if not self.running:
            self.system_start_hour = time.perf_counter()
            self.running = True
            self.timer.start()

    def actual_time(self):
        """
            temps courant = timeline_time + (heure systeme actuelle - heure systeme au demarrage) * 1000
        """
        if self.running and self.system_start_hour is not None:
            time_passed = time.perf_counter() - self.system_start_hour
            return self.timeline_time + int(time_passed * 1000)

        return self.timeline_time

    def on_tick(self):

        if not self.running:
            return

        time_now = self.actual_time()

        # temps actuel emis a l'ui
        self.updated_time.emit(time_now)

        for cue in self.cues_list:
            if self.last_verified_time < cue["temps"] <= time_now:
                self.fired_cue.emit(cue)
                print(f"Cue déclenché: {cue['nom']} à {cue['temps']} ms")

        #temps actu
        self.last_verified_time = time_now

        #les deux prochain cue a venir
        self.two_next_cues.emit(self.find_next_cues(time_now))

    def find_next_cues(self, actual_time_ms, number=2):
        resultat = []
        for cue in self.cues_list:
            if cue["temps"] > actual_time_ms:
                resultat.append(cue)
                if len(resultat) >= number:
                    break
        return resultat
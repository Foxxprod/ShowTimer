import sqlite3, threading, sys, os

db = None

def _internal_path():
    """Dossier _internal/ (ressources embarquées : tables.sql, icons…)."""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def _userdata_path():
    """Dossier inscriptible pour les données utilisateur (db, stpass…)."""
    if getattr(sys, 'frozen', False):
        return os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
                            "Foxx Production", "ShowTimer")
    return os.path.dirname(os.path.abspath(__file__))

def connect_db():
    global db
    userdata = _userdata_path()
    os.makedirs(userdata, exist_ok=True)
    db = Database(os.path.join(userdata, "database.db"))
    db.connect()


#Classe de gestion de la base de donnée
#Ne pas faire de requetes SQL sans passer par une instance de cette classe
#Instancier une seule fois la classe dans le projet pour eviter les conflit de base de donnée
class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self._lock = threading.RLock()  
    

    #Connexion a la base de donnée
    def connect(self):
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(self.db_name, check_same_thread=False)
                #Faire ici requete sql de creation de table si elle n'existe pas deja
                with self._lock:
                    with open(os.path.join(_internal_path(), "tables.sql"), "r", encoding="utf-8") as f:
                        self.connection.executescript(f.read())
                print("Connexion a la base de donnée sqlite effectuee.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la connexion a la base de donnée: {e}")



    ######################################GESTION DES EMMISIONS#####################################################################

    #permet de mettre a jour l'emmision actuellement active, permet de recuperer ensuite tout les cues correspondant a cette emmision
    def SetActiveShow(self, show_id):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT OR REPLACE INTO config (parameter, value) VALUES ('active_show', ?)", (show_id,))
                self.connection.commit()
                print(f"Emmission active mise a jour dans la base de donnée: {show_id}")
            except sqlite3.Error as e:
                print(f"Erreur de la mise a jour de l'emmsion active dans la base de donnée: {e}")

    #renvoie l'id de l'emmision active, a utiliser dans toutes les requetes qui necessite l'id de l'emmision
    def GetActiveShow(self):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT value FROM config WHERE parameter = 'active_show'") #recup la valeur de l'emison active
                result = cursor.fetchone()
                if result:
                    return int(result[0]) #renvoie l'id sous forme d'int
                else:
                    print("Aucune emmission active trouvee dans la base de donnée.")
                    return None #si pas d'emmsion trouvé on retourne None
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation de l'emmsion active dans la base de donnée: {e}")
                return None
            
    #Ajouter une emmision dans la abse de donnée, la duree de l'emmission est en milliseconde
    def AddShow(self, name, desc, total_time):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO shows (nom, description, duree) VALUES (?, ?, ?)", (name, desc, total_time))
                self.connection.commit()
                print(f"Emmission {name} ajoutee a la base de donnée.")
            except sqlite3.Error as e:
                print(f"Erreur lors de l'ajout d'une emmission dans la base de donnée: {e}")
    
    #Modifier une emmision a partir de son id
    def ModifyShow(self, show_id, name, desc, total_time):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("UPDATE shows SET nom = ?, description = ?, duree = ? WHERE id = ?", (name, desc, total_time, show_id))
                self.connection.commit()
                print(f"Emmission {show_id} modifiee dans la base de donnée.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la modification d'une emmission dans la base de donnée: {e}")

    #supprimer une emmision a partir de son id
    def DeleteShow(self, show_id):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM shows WHERE id = ?", (show_id,))
                self.connection.commit()
                cursor.execute("DELETE FROM cues WHERE show_id = ?", (show_id,)) #supprime aussi les cues correspondant a l'emmsion
                self.connection.commit()
                print(f"Emmission {show_id} supprimee de la base de donnée.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la suppression d'une emmission dans la base de donnée: {e}")

    def GetAllShows(self):
        with self._lock:
            try:
                cursor = self.connection.cursor() #dictionnary pour renvoyer une dictionnaire.
                cursor.row_factory = sqlite3.Row
                cursor.execute("SELECT * FROM shows") #recup tout les emmsions
                results = [dict(row) for row in cursor.fetchall()]
                return results
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation de tout les emmsions dans la base de donnée: {e}")
                return None
            
    def GetShowById(self, show_id):
        with self._lock:
            try:
                cursor = self.connection.cursor() #dictionnary pour renvoyer une dictionnaire.
                cursor.row_factory = sqlite3.Row
                cursor.execute("SELECT * FROM shows WHERE id = ?", (show_id,)) #recup l'emmsion correspondant a l'id
                result = cursor.fetchone()
                if result:
                    return dict(result) #renvoie l'emmsion sous forme de dictionnaire
                else:
                    print(f"Aucune emmission trouvee dans la base de donnée avec l'id {show_id}.")
                    return None #si pas d'emmsion trouvé on retourne None
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation de l'emmsion dans la base de donnée: {e}")
                return None
            
    def DeleteAllCuesFromShow(self, show_id):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM cues WHERE show_id = ?", (show_id,)) #supprime aussi les cues correspondant a l'emmsion
                self.connection.commit()
                print(f"Tous les cues de l'emmsion {show_id} ont ete supprime de la base de donnée.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la suppression de tout les cues de l'emmsion dans la base de donnée: {e}")
            



    ########################################GESTION DES CUES#####################################################################

    #Ajouter un cue a l'emmsion, le cue doit avoir comme parametre de temps, le temps de declenchement en ms
    def AddCueToShow(self, show_id, title, desc, time, osc_command, osc_args, color):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO cues (show_id, nom, description, temps, osc_url, osc_args, color) VALUES (?, ?, ?, ?, ?, ?, ?)", (show_id, title, desc, time, osc_command, osc_args, color))
                self.connection.commit()
                print(f"Cue ajoute a l'emmsion {show_id} dans la base")
            except sqlite3.Error as e:
                print(f"Erreur lors de l'ajout d'un cue a l'emmsion dans la base de donnée: {e}")

    #supprimer un cue a partir de son id
    def DeleteCue(self, cue_id):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM cues WHERE cue_id = ?", (cue_id,))
                self.connection.commit()
                print(f"Cue {cue_id} supprime de la base de donnée.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la suppression d'un cue dans la base de donnée: {e}")


    #renvoie tout les cus d'une emmission sous forme d'un dictionnaire
    def GetAllCuesFromShow(self, show_id):
        with self._lock:
            try:
                cursor = self.connection.cursor() #dictionnary pour renvoyer une dictionnaire.
                cursor.row_factory = sqlite3.Row
                cursor.execute("SELECT * FROM cues WHERE show_id = ?", (show_id,)) #recup tout les cues correspondant a l'emmsion active
                results = [dict(row) for row in cursor.fetchall()]
                return results
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation des cues de l'emmsion active dans la base de donnée: {e}")
                return None

    def GetCueById(self, cue_id):
        with self._lock:
            try:
                cursor = self.connection.cursor() #dictionnary pour renvoyer une dictionnaire.
                cursor.row_factory = sqlite3.Row
                cursor.execute("SELECT * FROM cues WHERE cue_id = ?", (cue_id,)) #recup le cue correspondant a l'id
                result = cursor.fetchone()
                if result:
                    return dict(result) #renvoie le cue sous forme de dictionnaire
                else:
                    print(f"Aucun cue trouve dans la base de donnée avec l'id {cue_id}.")
                    return None #si pas de cue trouvé on retourne None
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation du cue dans la base de donnée: {e}")
                return None
            
    def ModifyCue(self, cue_id, title, desc, time, osc_command, osc_args, color):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("UPDATE cues SET nom = ?, description = ?, temps = ?, osc_url = ?, osc_args = ?, color = ? WHERE cue_id = ?", (title, desc, time, osc_command, osc_args, color, cue_id))
                self.connection.commit()
                print(f"Cue {cue_id} modifie dans la base de donnée.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la modification d'un cue dans la base de donnée: {e}")
    
    #####################################CONFIGURATION PROMPTEUR#########################################

    def GetPrompterConfig(self): #renvoie la config du prompteur 
        #si la config n'existe pas, on renvoi une config par defaut
        defaults = {
            "prompter_text_size":       "60",
            "prompter_text_color":      "#B8860B",
            "next_cue_text_size":       "42",
            "next_cue_text_color":      "#FFFFFF",
            "next_cue_outline_width":   "4",
            "second_cue_text_size":     "28",
            "second_cue_text_color":    "#AAAAAA",
            "second_cue_outline_width": "4",
            "clock_text_size":          "28",
            "clock_text_color":         "#FFFFFF",
            "clock_outline_width":      "4",
            "blink_first_time":         "20000",
            "blink_second_time":        "10000",
            "blink_third_time":         "5000",
            "blink_first_color":        "#00CC00",
            "blink_second_color":       "#FF8800",
            "blink_third_color":        "#FF0000",
        }
        with self._lock:
            try:
                placeholders = ",".join("?" * len(defaults))
                cursor = self.connection.cursor()
                cursor.execute(
                    f"SELECT parameter, value FROM config WHERE parameter IN ({placeholders})",
                    list(defaults.keys())
                )
                for parameter, value in cursor.fetchall():
                    if value is not None:
                        defaults[parameter] = value
                return defaults
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation de la config prompteur: {e}")
                return defaults


    def SetPrompterConfig(self, **kwargs): #met a jour la config du prompteur, insere si inexistant MAIS normalement mnt c'est dans la base de donnee 
        with self._lock:
            try:
                cursor = self.connection.cursor()
                for parameter, value in kwargs.items():
                    cursor.execute(
                        "INSERT OR REPLACE INTO config (parameter, value) VALUES (?, ?)",
                        (parameter, value)
                    )
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erreur lors de la mise a jour de la config prompteur: {e}")

    #####################################CONFIGURATION OSC##############################################""
    def SetOSCConfig(self, osc_ip, osc_port):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT OR REPLACE INTO config (parameter, value) VALUES ('osc_ip', ?)", (osc_ip,))
                cursor.execute("INSERT OR REPLACE INTO config (parameter, value) VALUES ('osc_port', ?)", (osc_port,))
                self.connection.commit()
                print(f"Configuration OSC mise a jour dans la base de donnée.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la mise a jour de la configuration OSC dans la base de donnée: {e}")

    def GetOSCConfig(self):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT value FROM config WHERE parameter = 'osc_ip'") #recup la valeur de l'ip OSC
                osc_ip_result = cursor.fetchone()
                cursor.execute("SELECT value FROM config WHERE parameter = 'osc_port'") #recup la valeur du port OSC
                osc_port_result = cursor.fetchone()

                if osc_ip_result and osc_port_result:
                    return osc_ip_result[0], int(osc_port_result[0]) #renvoie l'ip et le port 
                else:
                    print("Aucune configuration OSC trouvee dans la base de donnée.")
                    return None, None #si pas de config trouvé on retourne None
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation de la configuration OSC dans la base de donnée: {e}")
                return None, None
            
    def SetOSCState(self, state):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT OR REPLACE INTO config (parameter, value) VALUES ('osc_active', ?)", (state,))
                print(f"L'etat  OSC a ete mis a jour dans la base de donnée. Etat: {state}")
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erreur lors de la mise a jour de la configuration OSC dans la base de donnée: {e}")

    
    def GetOSCState(self):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT value FROM config WHERE parameter = 'osc_active'") #recup la valeur de l'etat OSC
                result = cursor.fetchone()
                if result:
                    return result[0] #renvoie l'etat
                else:
                    print("Aucune configuration OSC trouvee dans la base de donnée.")
                    return None #si pas de config gezocht on retourne None
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation de la configuration OSC dans la base de donnée: {e}")
                return None
            

    #ajout d'une variable de retour a zero, permet de revenir a zero dans la commande OSC 
    #sinon dans chataigne la condition est toujours = et les action ne peuvent pas etre redeclenché un deuxième fois
    def SetOSCreturntozero(self, state):
        with self._lock:
            if state == True:
                state = "True"
            else:
                state = "False"

            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT OR REPLACE INTO config (parameter, value) VALUES ('OSC_RTZ', ?)", (state,))
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erreur lors de la mise a jour de la configuration OSC dans la base de donnée: {e}")

    def GetOSCreturntozero(self):
        with self._lock:
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT value FROM config WHERE parameter = 'OSC_RTZ'") #recup la valeur de l'etat OSC
                result = cursor.fetchone()
                if result:
                    if result[0] == "True":
                        return True
                    else:
                        return False
                else:
                    print("Aucune configuration OSC trouvee dans la base de donnée.")
                    return False #si pas de config gezocht on retourne false
            except sqlite3.Error as e:
                print(f"Erreur lors de la recuperation de la configuration OSC dans la base de donnée: {e}")
                return False
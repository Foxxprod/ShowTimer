import sqlite3, threading

db = None

def connect_db():
    global db
    db = Database("database.db")
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
                    with open("tables.sql", "r", encoding="utf-8") as f:
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
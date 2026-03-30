from pythonosc.udp_client import SimpleUDPClient
import database

osc_client = None


class OSCClient:
    def __init__(self, ip, port):
        self.client = None
        self.ip = ip
        self.port = port

    def connect(self):
        self.ip = self.ip
        self.port = self.port
        self.client = SimpleUDPClient(self.ip, self.port)
        print(f"Connecté à {self.ip}:{self.port} - Client OSC ")

    def disconnect(self):
        if self.client is None:
            print("Aucune connexion active.")
            return
        self.client = None
        print("Déconnecté.")

    def send(self, address, *args):

        if self.client is None:
            raise ConnectionError("Le client n'est pas connecté")
        self.client.send_message(address, list(args))
        print(f"Message envoyé → {address} : {args}")

def connect_osc_client():
        global osc_client
        osc_ip, osc_port = database.db.GetOSCConfig()
        if not osc_ip or not osc_port:
            print("Configuration OSC non trouvée. Veuillez configurer l'IP et le port OSC dans les paramètres.")
            return

        osc_client = OSCClient(osc_ip, osc_port)
        osc_client.connect()
        print("Client OSC connecté.")
    
def disconnect_osc_client():
        global osc_client
        if osc_client:
            osc_client.disconnect()
            osc_client = None
            print("Client OSC déconnecté.")
        else:
            print("Aucun client OSC à déconnecter.")
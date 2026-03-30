from pythonosc import dispatcher, osc_server

def print_message(address, *args):
    print(f"{address} : {args}")

d = dispatcher.Dispatcher()
d.set_default_handler(print_message)  # capture tous les messages

server = osc_server.ThreadingOSCUDPServer(("0.0.0.0", 9000), d)
print("Serveur OSC en écoute sur le port 9000...")
server.serve_forever()
import serial
import serial.tools.list_ports
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

import pystray
from PIL import Image, ImageDraw

# ── Configuration par défaut ──────────────────────────────────────────────────
BAUD_RATE = 19200
TIMEOUT   = 1
OSC_IP    = "0.0.0.0"

# État global
osc_server    = None
server_thread = None
selected_port = None
contact_delay = 0.5
tray_icon     = None


# ── Fonctions GPIO ────────────────────────────────────────────────────────────

def send_command(ser_port, command):
    ser_port.write(command.encode())
    return ser_port.read(25).decode()

def fermer_contact(pin: int):
    if not isinstance(pin, int) or not (0 <= pin <= 7):
        raise ValueError(f"Pin invalide : {pin}")
    with serial.Serial(selected_port, BAUD_RATE, timeout=TIMEOUT) as sp:
        send_command(sp, f"gpio clear {pin}\r")
    log(f"[GPIO {pin}] Contact FERME")

def ouvrir_contact(pin: int):
    if not isinstance(pin, int) or not (0 <= pin <= 7):
        raise ValueError(f"Pin invalide : {pin}")
    with serial.Serial(selected_port, BAUD_RATE, timeout=TIMEOUT) as sp:
        send_command(sp, f"gpio set {pin}\r")
    log(f"[GPIO {pin}] Contact OUVERT")


# ── Handler OSC ───────────────────────────────────────────────────────────────

def osc_gpio_handler(address, *args):
    log(f"[OSC] Message recu sur {address} - args : {args}")
    if len(args) < 1 or not isinstance(args[0], int):
        log("[OSC] Argument invalide (int attendu)")
        return
    pin = args[0]
    try:
        fermer_contact(pin)
        time.sleep(contact_delay)
        ouvrir_contact(pin)
        log(f"[OSC] Pulse termine sur pin {pin}")
    except Exception as e:
        log(f"[OSC] Erreur : {e}")


# ── Serveur OSC ───────────────────────────────────────────────────────────────

def start_server():
    global osc_server, server_thread, selected_port, contact_delay

    port = combo_port.get()
    if not port:
        messagebox.showerror("Erreur", "Veuillez selectionner un port COM.")
        return

    try:
        contact_delay = float(entry_delay.get())
    except ValueError:
        messagebox.showerror("Erreur", "Le delai doit etre un nombre decimal (ex: 0.5)")
        return

    try:
        osc_port = int(entry_osc_port.get())
        if not (1 <= osc_port <= 65535):
            raise ValueError()
    except ValueError:
        messagebox.showerror("Erreur", "Le port OSC doit etre un entier entre 1 et 65535.")
        return

    selected_port = port.split(" ")[0]

    dispatcher = Dispatcher()
    dispatcher.map("/gpo", osc_gpio_handler)
    try:
        osc_server = BlockingOSCUDPServer((OSC_IP, osc_port), dispatcher)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de demarrer le serveur OSC :\n{e}")
        return

    server_thread = threading.Thread(target=osc_server.serve_forever, daemon=True)
    server_thread.start()

    btn_start.config(state="disabled")
    btn_stop.config(state="normal")
    combo_port.config(state="disabled")
    entry_delay.config(state="disabled")
    entry_osc_port.config(state="disabled")
    btn_refresh.config(state="disabled")
    osc_info_var.set(f"/gpo   UDP:{osc_port}   arg: int (pin 0-7)")
    status_var.set("EN LIGNE")
    status_dot.config(fg=COLOR_GREEN)
    status_label.config(fg=COLOR_GREEN)
    update_tray_icon()
    log(f"Serveur OSC demarre - COM : {selected_port} | delai : {contact_delay}s | UDP : {osc_port}")

def stop_server():
    global osc_server
    if osc_server:
        osc_server.shutdown()
        osc_server = None

    btn_start.config(state="normal")
    btn_stop.config(state="disabled")
    combo_port.config(state="readonly")
    entry_delay.config(state="normal")
    entry_osc_port.config(state="normal")
    btn_refresh.config(state="normal")
    status_var.set("HORS LIGNE")
    status_dot.config(fg=COLOR_RED)
    status_label.config(fg=COLOR_RED)
    update_tray_icon()
    log("Serveur OSC arrete.")


# ── Utilitaires UI ────────────────────────────────────────────────────────────

def refresh_ports():
    ports = serial.tools.list_ports.comports()
    values = [f"{p.device}  -  {p.description}" for p in ports]
    combo_port["values"] = values
    if values:
        combo_port.current(0)
        log(f"{len(values)} port(s) detecte(s).")
    else:
        combo_port.set("")
        log("Aucun port COM detecte.")

def log(msg):
    txt_log.config(state="normal")
    txt_log.insert("end", f"{time.strftime('%H:%M:%S')}  {msg}\n")
    txt_log.see("end")
    txt_log.config(state="disabled")


# ── Systray ───────────────────────────────────────────────────────────────────

def make_tray_image():
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([2, 2, size - 2, size - 2], fill="#1a1d27")
    color = "#39ff9a" if osc_server else "#ff4f5e"
    draw.ellipse([14, 14, size - 14, size - 14], fill=color)
    return img

def update_tray_icon():
    if tray_icon:
        tray_icon.icon = make_tray_image()
        server_label = "Serveur : EN LIGNE" if osc_server else "Serveur : HORS LIGNE"
        tray_icon.menu = pystray.Menu(
            pystray.MenuItem(server_label, None, enabled=False),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Ouvrir", tray_open, default=True),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Quitter", tray_quit),
        )

def tray_open(icon=None, item=None):
    root.after(0, _do_show)

def _do_show():
    root.deiconify()
    root.lift()
    root.focus_force()

def tray_quit(icon=None, item=None):
    root.after(0, _do_quit)

def _do_quit():
    if osc_server:
        osc_server.shutdown()
    if tray_icon:
        tray_icon.stop()
    root.destroy()

def on_close():
    """Croix → réduit dans la zone de notification, sans confirmation."""
    root.withdraw()

def start_tray():
    global tray_icon
    menu = pystray.Menu(
        pystray.MenuItem("Serveur : HORS LIGNE", None, enabled=False),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Ouvrir", tray_open, default=True),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Quitter", tray_quit),
    )
    tray_icon = pystray.Icon("NumatoGPIO", make_tray_image(), "Numato GPIO", menu)
    threading.Thread(target=tray_icon.run, daemon=True).start()


# ── Interface Tkinter ─────────────────────────────────────────────────────────

BG          = "#0f1117"
PANEL       = "#1a1d27"
BORDER      = "#2a2d3e"
COLOR_GREEN = "#39ff9a"
COLOR_RED   = "#ff4f5e"
COLOR_BLUE  = "#4f9eff"
FG          = "#e8eaf0"
FG_DIM      = "#6b6f85"
FONT_MONO   = ("Courier New", 9)
FONT_LABEL  = ("Segoe UI", 9)
FONT_TITLE  = ("Segoe UI", 13, "bold")
FONT_BTN    = ("Segoe UI", 9, "bold")

root = tk.Tk()
root.title("Numato GPO  -  Serveur OSC")
root.configure(bg=BG)
root.resizable(False, False)
root.geometry("480x580")
root.protocol("WM_DELETE_WINDOW", on_close)

# ── Titre ─────────────────────────────────────────────────────────────────────
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=20, pady=(18, 4))

tk.Label(header, text="NUMATO GPO", font=FONT_TITLE, bg=BG, fg=FG).pack(side="left")

status_frame = tk.Frame(header, bg=BG)
status_frame.pack(side="right")
status_dot = tk.Label(status_frame, text="●", font=FONT_LABEL, bg=BG, fg=COLOR_RED)
status_dot.pack(side="left")
status_var = tk.StringVar(value="HORS LIGNE")
status_label = tk.Label(status_frame, textvariable=status_var, font=FONT_LABEL, bg=BG, fg=COLOR_RED)
status_label.pack(side="left", padx=(3, 0))

tk.Frame(root, height=1, bg=BORDER).pack(fill="x", padx=20)

# ── Panneau config ────────────────────────────────────────────────────────────
panel = tk.Frame(root, bg=PANEL, bd=0, highlightthickness=1, highlightbackground=BORDER)
panel.pack(fill="x", padx=20, pady=14)

def entry_style():
    return dict(font=FONT_LABEL, bg=BG, fg=FG, insertbackground=FG,
                relief="flat", highlightthickness=1,
                highlightbackground=BORDER, highlightcolor=COLOR_BLUE)

def lbl(parent, text):
    return tk.Label(parent, text=text, font=FONT_LABEL, bg=PANEL, fg=FG_DIM, anchor="w")

# ── Port COM ──────────────────────────────────────────────────────────────────
tk.Frame(panel, bg=PANEL).pack(pady=2)

row_com_lbl = tk.Frame(panel, bg=PANEL)
row_com_lbl.pack(fill="x", padx=14, pady=(6, 0))
lbl(row_com_lbl, "Port COM").pack(fill="x")

row_com = tk.Frame(panel, bg=PANEL)
row_com.pack(fill="x", padx=14, pady=(4, 0))

combo_port = ttk.Combobox(row_com, state="readonly", font=FONT_LABEL, width=36)
combo_port.pack(side="left", fill="x", expand=True)

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox",
    fieldbackground=BG, background=BG, foreground=FG,
    selectbackground=BG, selectforeground=FG,
    bordercolor=BORDER, arrowcolor=FG_DIM)

btn_refresh = tk.Button(row_com, text="  Actualiser  ", font=FONT_BTN, command=refresh_ports,
    bg=BORDER, fg=FG, relief="flat", cursor="hand2",
    activebackground=COLOR_BLUE, activeforeground=BG, padx=6, pady=2)
btn_refresh.pack(side="left", padx=(6, 0))

# ── Séparateur ────────────────────────────────────────────────────────────────
tk.Frame(panel, height=1, bg=BORDER).pack(fill="x", padx=14, pady=(14, 0))

# ── Ligne : Durée du contact + Port OSC ──────────────────────────────────────
row_labels = tk.Frame(panel, bg=PANEL)
row_labels.pack(fill="x", padx=14, pady=(10, 0))

lbl_left = tk.Frame(row_labels, bg=PANEL)
lbl_left.pack(side="left", expand=True, fill="x")
lbl(lbl_left, "Duree du contact").pack(anchor="w")

lbl_right = tk.Frame(row_labels, bg=PANEL)
lbl_right.pack(side="left", expand=True, fill="x", padx=(16, 0))
lbl(lbl_right, "Port d'ecoute OSC").pack(anchor="w")

row_fields = tk.Frame(panel, bg=PANEL)
row_fields.pack(fill="x", padx=14, pady=(4, 14))

field_left = tk.Frame(row_fields, bg=PANEL)
field_left.pack(side="left", expand=True, fill="x")
inner_left = tk.Frame(field_left, bg=PANEL)
inner_left.pack(anchor="w")
entry_delay = tk.Entry(inner_left, width=8, **entry_style())
entry_delay.insert(0, "0.5")
entry_delay.pack(side="left")
tk.Label(inner_left, text=" secondes", font=FONT_LABEL, bg=PANEL, fg=FG_DIM).pack(side="left")

field_right = tk.Frame(row_fields, bg=PANEL)
field_right.pack(side="left", expand=True, fill="x", padx=(16, 0))
inner_right = tk.Frame(field_right, bg=PANEL)
inner_right.pack(anchor="w")
entry_osc_port = tk.Entry(inner_right, width=8, **entry_style())
entry_osc_port.insert(0, "5005")
entry_osc_port.pack(side="left")
tk.Label(inner_right, text=" UDP", font=FONT_LABEL, bg=PANEL, fg=FG_DIM).pack(side="left")

# ── Boutons start / stop ──────────────────────────────────────────────────────
btn_row = tk.Frame(root, bg=BG)
btn_row.pack(fill="x", padx=20, pady=(0, 10))

btn_start = tk.Button(btn_row, text="  DEMARRER", font=FONT_BTN,
    command=start_server,
    bg=COLOR_GREEN, fg=BG, relief="flat", cursor="hand2",
    activebackground="#2ecc71", activeforeground=BG,
    padx=18, pady=9)
btn_start.pack(side="left", expand=True, fill="x", padx=(0, 6))

btn_stop = tk.Button(btn_row, text="  ARRETER", font=FONT_BTN,
    command=stop_server, state="disabled",
    bg=COLOR_RED, fg=BG, relief="flat", cursor="hand2",
    activebackground="#c0392b", activeforeground=BG,
    padx=18, pady=9)
btn_stop.pack(side="left", expand=True, fill="x")

# ── Info OSC ──────────────────────────────────────────────────────────────────
info_frame = tk.Frame(root, bg=PANEL, highlightthickness=1, highlightbackground=BORDER)
info_frame.pack(fill="x", padx=20, pady=(0, 10))

info_inner = tk.Frame(info_frame, bg=PANEL)
info_inner.pack(fill="x", padx=14, pady=8)

tk.Label(info_inner, text="Adresse OSC :", font=FONT_LABEL, bg=PANEL, fg=FG_DIM).pack(side="left")
osc_info_var = tk.StringVar(value="/gpo   UDP:5005   arg: int (pin 0-7)")
tk.Label(info_inner, textvariable=osc_info_var, font=FONT_MONO, bg=PANEL, fg=COLOR_BLUE).pack(side="left", padx=6)

# ── Journal ───────────────────────────────────────────────────────────────────
tk.Label(root, text="Journal", font=FONT_LABEL, bg=BG, fg=FG_DIM, anchor="w").pack(fill="x", padx=20)

log_frame = tk.Frame(root, bg=PANEL, highlightthickness=1, highlightbackground=BORDER)
log_frame.pack(fill="both", expand=True, padx=20, pady=(2, 16))

txt_log = tk.Text(log_frame, font=FONT_MONO, bg=PANEL, fg=FG_DIM,
    insertbackground=FG, relief="flat", state="disabled",
    wrap="word", padx=10, pady=8)
txt_log.pack(fill="both", expand=True)

# ── Init ──────────────────────────────────────────────────────────────────────
refresh_ports()
log("Interface prete. Selectionnez un port COM et demarrez le serveur.")
start_tray()

root.mainloop()
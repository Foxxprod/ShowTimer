import logging, os, sys
from datetime import datetime

_logger = None
_log_file_path = None
_ui_callback = None  # appelé à chaque nouvelle ligne de log


class _CallbackHandler(logging.Handler):
    def emit(self, record):
        if _ui_callback:
            try:
                _ui_callback(self.format(record))
            except Exception:
                pass


def _get_userdata_dir():
    if getattr(sys, 'frozen', False):
        return os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
                            "Foxx Production", "ShowTimer")
    return os.path.dirname(os.path.abspath(__file__))

def _get_logs_dir():
    return os.path.join(_get_userdata_dir(), "logs")


def setup():
    """Initialise le système de logs. À appeler une seule fois au démarrage."""
    global _logger, _log_file_path

    logs_dir = _get_logs_dir()
    os.makedirs(logs_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    _log_file_path = os.path.join(logs_dir, f"session_{timestamp}.txt")

    _logger = logging.getLogger("ShowTimer")
    _logger.setLevel(logging.DEBUG)
    _logger.handlers.clear()

    fmt = logging.Formatter("%(asctime)s  [%(levelname)s]  %(message)s", "%H:%M:%S")

    # Handler fichier
    fh = logging.FileHandler(_log_file_path, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    _logger.addHandler(fh)

    # Handler console (visible en mode dev)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(fmt)
    _logger.addHandler(ch)

    # Handler callback UI
    cb = _CallbackHandler()
    cb.setLevel(logging.DEBUG)
    cb.setFormatter(fmt)
    _logger.addHandler(cb)

    _logger.info("=== Session démarrée ===")


def set_ui_callback(fn):
    """Enregistre une fonction appelée à chaque nouvelle ligne de log."""
    global _ui_callback
    _ui_callback = fn


def clear_ui_callback():
    global _ui_callback
    _ui_callback = None


def info(msg):
    if _logger:
        _logger.info(msg)

def warning(msg):
    if _logger:
        _logger.warning(msg)

def error(msg):
    if _logger:
        _logger.error(msg)

def debug(msg):
    if _logger:
        _logger.debug(msg)


def get_log_file_path():
    return _log_file_path

def get_logs_dir():
    return _get_logs_dir()

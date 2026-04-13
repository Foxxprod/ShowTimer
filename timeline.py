from PySide6.QtWidgets import QWidget, QToolTip
from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics

#Classe de la timeline en bas de l'interface de l'operateur
#!!!! Ce code a été fait avec l'IA, peut etre verifier en detail
#okk



class TimelineWidget(QWidget):
    def __init__(self, duree_totale_ms, parent=None):
        super().__init__(parent)
        self.duree_totale_ms = max(duree_totale_ms, 1)
        self.position_ms = 0
        self.cues = []
        self.setMouseTracking(True)
        self._hovered_cue = None

    def set_cues(self, cues):
        self.cues = sorted(cues, key=lambda c: c["temps"])
        self.update()

    def set_position(self, ms):
        self.position_ms = ms
        self.update()

    def _x_for_ms(self, ms):
        return int(ms / self.duree_totale_ms * self.width())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()

        # Fond
        painter.fillRect(0, 0, w, h, QColor("#1a1a1a"))

        # Barre de progression (temps écoulé)
        progress_x = self._x_for_ms(self.position_ms)
        painter.fillRect(0, 0, progress_x, h, QColor("#1a3a5a"))

        # Marqueurs de cues
        font = QFont("Segoe UI", 8)
        painter.setFont(font)
        fm = QFontMetrics(font)
        label_h = fm.height()

        # Deux rangées de labels : haut (y1) et bas (y2)
        y_top = label_h + 2
        y_bot = h - 4
        niveaux = [y_top, y_bot]

        # Dernier x utilisé par niveau pour éviter les chevauchements
        last_x = [-(10**6), -(10**6)]
        MIN_ESPACE = 55  # px minimum entre deux labels du même niveau

        for cue in self.cues:
            x = self._x_for_ms(cue["temps"])
            est_passe = cue["temps"] <= self.position_ms
            couleur = QColor("#555555") if est_passe else QColor("#0078d4")

            # Trait vertical
            painter.setPen(QPen(couleur, 2))
            painter.drawLine(x, 10, x, h - label_h - 4)

            # Triangle marqueur en haut
            painter.setBrush(couleur)
            painter.setPen(Qt.NoPen)
            painter.drawPolygon([
                QPoint(x - 5, 0),
                QPoint(x + 5, 0),
                QPoint(x, 8),
            ])

            # Choisir le niveau avec le plus d'espace disponible
            niveau = 0 if (x - last_x[0]) >= (x - last_x[1]) else 1
            if x - last_x[niveau] < MIN_ESPACE:
                continue  # trop serré, on saute ce label

            nom = cue.get("nom", "")
            nom_affiche = fm.elidedText(nom, Qt.ElideRight, MIN_ESPACE + 20)
            painter.setPen(couleur)
            painter.drawText(x + 3, niveaux[niveau], nom_affiche)
            last_x[niveau] = x

        # Tête de lecture
        painter.setPen(QPen(QColor("#ffffff"), 2))
        painter.drawLine(progress_x, 0, progress_x, h)
        painter.setBrush(QColor("#ffffff"))
        painter.setPen(Qt.NoPen)
        tete = [
            QPoint(progress_x - 6, 0),
            QPoint(progress_x + 6, 0),
            QPoint(progress_x, 10),
        ]
        painter.drawPolygon(tete)

        # Bordure
        painter.setPen(QPen(QColor("#3a3a3a"), 1))
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(0, 0, w - 1, h - 1)

    def mouseMoveEvent(self, event):
        self._hovered_cue = None
        for cue in self.cues:
            x = self._x_for_ms(cue["temps"])
            if abs(event.x() - x) <= 6:
                self._hovered_cue = cue
                h = cue["temps"] // 3600000
                m = (cue["temps"] % 3600000) // 60000
                s = (cue["temps"] % 60000) // 1000
                texte = f"{cue.get('nom', '')}  —  {h:02d}:{m:02d}:{s:02d}"
                QToolTip.showText(event.globalPosition().toPoint(), texte, self)
                break
        if self._hovered_cue is None:
            QToolTip.hideText()

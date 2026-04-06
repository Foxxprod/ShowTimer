from PySide6.QtWidgets import (
    QDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QGroupBox,
    QPushButton, QSpinBox, QLabel, QDialogButtonBox, QWidget,
    QScrollArea, QColorDialog, QSizePolicy
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QPainter, QPainterPath, QFont, QPen

import database


class LabelWithOutline(QWidget):
    def __init__(self, text="", color=None, font_size=36, outline_width=4, parent=None):
        super().__init__(parent)
        self._text = text
        self._color = QColor(color) if isinstance(color, str) else (color or QColor("white"))
        self._font_size = int(font_size)
        self._outline_width = int(outline_width)

    def set_text(self, text):
        self._text = text
        self.update()

    def set_color(self, color):
        self._color = QColor(color) if isinstance(color, str) else color
        self.update()

    def set_font_size(self, size):
        self._font_size = int(size)
        self.update()

    def set_outline_width(self, width):
        self._outline_width = int(width)
        self.update()

    def paintEvent(self, event):
        if not self._text:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        font = QFont("Arial", self._font_size, QFont.Bold)
        path = QPainterPath()
        path.addText(0, 0, font, self._text)
        text_rect = path.boundingRect()
        if text_rect.width() == 0 or text_rect.height() == 0:
            return
        scale_x = self.width() / text_rect.width() if text_rect.width() > self.width() else 1.0
        scale_y = self.height() / text_rect.height() if text_rect.height() > self.height() else 1.0
        scale = min(scale_x, scale_y)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(scale, scale)
        painter.translate(-text_rect.center())
        painter.setPen(QPen(QColor("black"), self._outline_width / scale))
        painter.setBrush(self._color)
        painter.drawPath(path)


class ColorButton(QPushButton):
    color_changed = Signal(str)

    def __init__(self, color="#FFFFFF", parent=None):
        super().__init__(parent)
        self._color = QColor(color)
        self._refresh()
        self.clicked.connect(self._pick)

    def _refresh(self):
        self.setText(self._color.name().upper())
        fg = "#000000" if self._color.lightness() > 128 else "#FFFFFF"
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self._color.name()};
                color: {fg};
                border: 1px solid #888;
                padding: 4px 10px;
                border-radius: 3px;
                font-weight: bold;
            }}
        """)

    def _pick(self):
        c = QColorDialog.getColor(self._color, self, "Choisir une couleur")
        if c.isValid():
            self._color = c
            self._refresh()
            self.color_changed.emit(self._color.name())

    def get_color(self):
        return self._color.name()

    def set_color(self, color_str):
        self._color = QColor(color_str)
        self._refresh()


class PrompterSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configuration du Prompteur")
        self.setMinimumSize(950, 620)
        self.resize(1150, 700)

        self.config = database.db.GetPrompterConfig()
        self._build_ui()
        self._load_config()
        self._update_preview()

    def _build_ui(self):
        outer = QVBoxLayout(self)

        content = QHBoxLayout()
        content.setSpacing(12)

        # --- GAUCHE : formulaire scrollable ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFixedWidth(440)
        scroll.setStyleSheet("QScrollArea { border: none; }")

        form_widget = QWidget()
        form_vbox = QVBoxLayout(form_widget)
        form_vbox.setSpacing(10)
        form_vbox.addWidget(self._group_prompt_text())
        form_vbox.addWidget(self._group_next_cue())
        form_vbox.addWidget(self._group_second_cue())
        form_vbox.addWidget(self._group_clock())
        form_vbox.addWidget(self._group_blink())
        form_vbox.addStretch()

        scroll.setWidget(form_widget)
        content.addWidget(scroll)

        # --- DROITE : aperçu ---
        content.addWidget(self._build_preview(), 1)

        outer.addLayout(content)

        btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btn_box.button(QDialogButtonBox.Ok).setText("Enregistrer")
        btn_box.button(QDialogButtonBox.Cancel).setText("Annuler")
        btn_box.accepted.connect(self._save)
        btn_box.rejected.connect(self.reject)
        outer.addWidget(btn_box)

    def _make_group(self, title):
        group = QGroupBox(title)
        form = QFormLayout(group)
        form.setLabelAlignment(Qt.AlignRight)
        form.setSpacing(8)
        return group, form

    def _make_spinbox(self, min_val, max_val, suffix=""):
        sb = QSpinBox()
        sb.setRange(min_val, max_val)
        if suffix:
            sb.setSuffix(suffix)
        sb.valueChanged.connect(self._update_preview)
        return sb

    def _group_prompt_text(self):
        group, form = self._make_group("Texte principal")
        self.sb_prompter_text_size = self._make_spinbox(8, 300, " px")
        self.cb_prompter_text_color = ColorButton()
        self.cb_prompter_text_color.color_changed.connect(self._update_preview)
        form.addRow("Taille :", self.sb_prompter_text_size)
        form.addRow("Couleur :", self.cb_prompter_text_color)
        return group

    def _group_next_cue(self):
        group, form = self._make_group("Next Cue")
        self.sb_next_cue_text_size = self._make_spinbox(8, 300, " px")
        self.cb_next_cue_text_color = ColorButton()
        self.cb_next_cue_text_color.color_changed.connect(self._update_preview)
        self.sb_next_cue_outline = self._make_spinbox(0, 20, " px")
        form.addRow("Taille :", self.sb_next_cue_text_size)
        form.addRow("Couleur :", self.cb_next_cue_text_color)
        form.addRow("Contour :", self.sb_next_cue_outline)
        return group

    def _group_second_cue(self):
        group, form = self._make_group("Second Cue")
        self.sb_second_cue_text_size = self._make_spinbox(8, 300, " px")
        self.cb_second_cue_text_color = ColorButton()
        self.cb_second_cue_text_color.color_changed.connect(self._update_preview)
        self.sb_second_cue_outline = self._make_spinbox(0, 20, " px")
        form.addRow("Taille :", self.sb_second_cue_text_size)
        form.addRow("Couleur :", self.cb_second_cue_text_color)
        form.addRow("Contour :", self.sb_second_cue_outline)
        return group

    def _group_clock(self):
        group, form = self._make_group("Horloge")
        self.sb_clock_text_size = self._make_spinbox(8, 300, " px")
        self.cb_clock_text_color = ColorButton()
        self.cb_clock_text_color.color_changed.connect(self._update_preview)
        self.sb_clock_outline = self._make_spinbox(0, 20, " px")
        form.addRow("Taille :", self.sb_clock_text_size)
        form.addRow("Couleur :", self.cb_clock_text_color)
        form.addRow("Contour :", self.sb_clock_outline)
        return group

    def _group_blink(self):
        group, form = self._make_group("Clignotements du Next Cue")

        self.sb_blink_first_time = self._make_spinbox(1, 60, " s")
        self.cb_blink_first_color = ColorButton()
        self.cb_blink_first_color.color_changed.connect(self._update_preview)

        self.sb_blink_second_time = self._make_spinbox(1, 60, " s")
        self.cb_blink_second_color = ColorButton()
        self.cb_blink_second_color.color_changed.connect(self._update_preview)

        self.sb_blink_third_time = self._make_spinbox(1, 60, " s")
        self.cb_blink_third_color = ColorButton()
        self.cb_blink_third_color.color_changed.connect(self._update_preview)

        form.addRow("Seuil 1 (lent) :", self.sb_blink_first_time)
        form.addRow("Couleur 1 :", self.cb_blink_first_color)
        form.addRow("Seuil 2 :", self.sb_blink_second_time)
        form.addRow("Couleur 2 :", self.cb_blink_second_color)
        form.addRow("Seuil 3 (urgent) :", self.sb_blink_third_time)
        form.addRow("Couleur 3 :", self.cb_blink_third_color)
        return group

    def _build_preview(self):
        container = QWidget()
        container.setStyleSheet("background-color: #111111; border-radius: 8px;")

        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(14, 14, 14, 14)
        vbox.setSpacing(6)

        lbl_title = QLabel("Aperçu")
        lbl_title.setStyleSheet("color: #555555; font-size: 11px; background: transparent;")
        lbl_title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbl_title)

        # Texte principal
        self.preview_prompt = QLabel("Texte du prompteur — exemple affiché à l'écran")
        self.preview_prompt.setWordWrap(True)
        self.preview_prompt.setAlignment(Qt.AlignCenter)
        self.preview_prompt.setMinimumHeight(100)
        self.preview_prompt.setStyleSheet("background: transparent;")
        vbox.addWidget(self.preview_prompt)

        vbox.addStretch()

        # Second cue
        lbl_s = QLabel("Second Cue")
        lbl_s.setStyleSheet("color: #444444; font-size: 10px; background: transparent;")
        vbox.addWidget(lbl_s)

        self.preview_second_cue = LabelWithOutline("Suite émission : 00:08:30")
        self.preview_second_cue.setMinimumHeight(55)
        vbox.addWidget(self.preview_second_cue)

        # Next cue
        lbl_n = QLabel("Next Cue")
        lbl_n.setStyleSheet("color: #444444; font-size: 10px; background: transparent;")
        vbox.addWidget(lbl_n)

        self.preview_next_cue = LabelWithOutline("Plateau 1 : 00:02:15")
        self.preview_next_cue.setMinimumHeight(90)
        vbox.addWidget(self.preview_next_cue)

        # Horloge
        lbl_c = QLabel("Horloge")
        lbl_c.setStyleSheet("color: #444444; font-size: 10px; background: transparent;")
        vbox.addWidget(lbl_c)

        self.preview_clock = LabelWithOutline("Écoulé : 00:10:30     Restant : 01:49:30")
        self.preview_clock.setMinimumHeight(55)
        vbox.addWidget(self.preview_clock)

        # Clignotements
        lbl_blink = QLabel("Couleurs de clignotement")
        lbl_blink.setStyleSheet("color: #444444; font-size: 10px; background: transparent;")
        vbox.addWidget(lbl_blink)

        blink_row = QHBoxLayout()
        blink_row.setSpacing(6)
        self.preview_blink1 = QLabel()
        self.preview_blink2 = QLabel()
        self.preview_blink3 = QLabel()
        for lbl in [self.preview_blink1, self.preview_blink2, self.preview_blink3]:
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setMinimumHeight(32)
            lbl.setStyleSheet("border-radius: 4px; font-weight: bold; font-size: 12px;")
            blink_row.addWidget(lbl)
        vbox.addLayout(blink_row)

        return container

    def _load_config(self):
        c = self.config
        self.sb_prompter_text_size.setValue(int(c["prompter_text_size"]))
        self.cb_prompter_text_color.set_color(c["prompter_text_color"])

        self.sb_next_cue_text_size.setValue(int(c["next_cue_text_size"]))
        self.cb_next_cue_text_color.set_color(c["next_cue_text_color"])
        self.sb_next_cue_outline.setValue(int(c["next_cue_outline_width"]))

        self.sb_second_cue_text_size.setValue(int(c["second_cue_text_size"]))
        self.cb_second_cue_text_color.set_color(c["second_cue_text_color"])
        self.sb_second_cue_outline.setValue(int(c["second_cue_outline_width"]))

        self.sb_clock_text_size.setValue(int(c["clock_text_size"]))
        self.cb_clock_text_color.set_color(c["clock_text_color"])
        self.sb_clock_outline.setValue(int(c["clock_outline_width"]))

        self.sb_blink_first_time.setValue(int(c["blink_first_time"]) // 1000)
        self.cb_blink_first_color.set_color(c["blink_first_color"])
        self.sb_blink_second_time.setValue(int(c["blink_second_time"]) // 1000)
        self.cb_blink_second_color.set_color(c["blink_second_color"])
        self.sb_blink_third_time.setValue(int(c["blink_third_time"]) // 1000)
        self.cb_blink_third_color.set_color(c["blink_third_color"])

    def _update_preview(self):
        # Texte principal
        size = self.sb_prompter_text_size.value()
        color = self.cb_prompter_text_color.get_color()
        self.preview_prompt.setStyleSheet(f"""
            color: {color};
            font-size: {size}px;
            font-weight: bold;
            background-color: transparent;
        """)

        # Next cue
        self.preview_next_cue.set_font_size(self.sb_next_cue_text_size.value())
        self.preview_next_cue.set_color(self.cb_next_cue_text_color.get_color())
        self.preview_next_cue.set_outline_width(self.sb_next_cue_outline.value())

        # Second cue
        self.preview_second_cue.set_font_size(self.sb_second_cue_text_size.value())
        self.preview_second_cue.set_color(self.cb_second_cue_text_color.get_color())
        self.preview_second_cue.set_outline_width(self.sb_second_cue_outline.value())

        # Horloge
        self.preview_clock.set_font_size(self.sb_clock_text_size.value())
        self.preview_clock.set_color(self.cb_clock_text_color.get_color())
        self.preview_clock.set_outline_width(self.sb_clock_outline.value())

        # Swatches clignotements
        for lbl, btn, sb in [
            (self.preview_blink1, self.cb_blink_first_color,  self.sb_blink_first_time),
            (self.preview_blink2, self.cb_blink_second_color, self.sb_blink_second_time),
            (self.preview_blink3, self.cb_blink_third_color,  self.sb_blink_third_time),
        ]:
            c = btn.get_color()
            fg = "#000000" if QColor(c).lightness() > 128 else "#FFFFFF"
            lbl.setStyleSheet(
                f"background-color: {c}; color: {fg}; border-radius: 4px; "
                f"font-weight: bold; font-size: 12px; padding: 4px;"
            )
            lbl.setText(f"< {sb.value()} s")

    def _save(self):
        database.db.SetPrompterConfig(
            prompter_text_size=str(self.sb_prompter_text_size.value()),
            prompter_text_color=self.cb_prompter_text_color.get_color(),
            next_cue_text_size=str(self.sb_next_cue_text_size.value()),
            next_cue_text_color=self.cb_next_cue_text_color.get_color(),
            next_cue_outline_width=str(self.sb_next_cue_outline.value()),
            second_cue_text_size=str(self.sb_second_cue_text_size.value()),
            second_cue_text_color=self.cb_second_cue_text_color.get_color(),
            second_cue_outline_width=str(self.sb_second_cue_outline.value()),
            clock_text_size=str(self.sb_clock_text_size.value()),
            clock_text_color=self.cb_clock_text_color.get_color(),
            clock_outline_width=str(self.sb_clock_outline.value()),
            blink_first_time=str(self.sb_blink_first_time.value() * 1000),
            blink_first_color=self.cb_blink_first_color.get_color(),
            blink_second_time=str(self.sb_blink_second_time.value() * 1000),
            blink_second_color=self.cb_blink_second_color.get_color(),
            blink_third_time=str(self.sb_blink_third_time.value() * 1000),
            blink_third_color=self.cb_blink_third_color.get_color(),
        )
        self.accept()

from PyQt5 import QtWidgets

formats = [
    "mp3",
    "mp4",
    "m4a",
    "wav",
    "ogg"
]


class DropLine(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.changed = False

    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        self.changed = True

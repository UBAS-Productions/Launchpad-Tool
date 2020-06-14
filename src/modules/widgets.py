from PyQt5 import QtWidgets
from PyQt5.QtCore import QMimeData

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

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        self.changed = True


class ItemList(QtWidgets.QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def mimeData(self, items):
        mimedata = QMimeData()
        mimedata.setText(items[0].text())
        return mimedata

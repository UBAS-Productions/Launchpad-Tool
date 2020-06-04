"""

The window handler.
"""
from sys import argv, exit

from PyQt5 import QtWidgets

from modules.ui import Ui_window


# TODO:
#   Launchpad selection

class Window:
    def __init__(self, width, height):
        self.app = QApplication(argv)
        self.widget = QWidget()
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        self.widget.resize(self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        self.widget.resize(self.__width, self.__height)


app = QtWidgets.QApplication(argv)
window = QtWidgets.QMainWindow()
ui = Ui_window()
ui.setupUi(window)
window.show()
exit(app.exec_())

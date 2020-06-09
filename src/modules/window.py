"""

The window handler.
"""
from sys import argv, exit

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

from modules.ui import Ui_window


# TODO:
#   Launchpad selection
#   Button assignment
#   Drag'n'Drop
#   Volume apply
#   Configfsiles

class Window:
    def __init__(self, width, height):
        self.app = QApplication(argv)
        self.window = QtWidgets.QMainWindow()
        self.widget = QWidget()
        self.__width = width
        self.__height = height
        self.ui = Ui_window()
        self.ui.setupUi(self.window)

    @property
    def height(self):
        """

        :return:
        """
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        self.widget.resize(self.__width, self.__height)

    @property
    def width(self):
        """

        :return:
        """
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        self.widget.resize(self.__width, self.__height)


if __name__ == "__main__":
    w = Window(640, 480)
    w.window.show()
    exit(w.app.exec_())

"""

The window handler.
"""
from sys import argv

from PyQt5.QtWidgets import QApplication, QWidget
# TODO:
#   Launchpad selection

class Window:
    def __init__(self, width, height):
        self.app = QApplication(argv)
        self.widget = QWidget()
        self.__width = width
        self.__height = height

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


if __name__ == '__main__':
    app = QApplication(argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('')
    w.show()

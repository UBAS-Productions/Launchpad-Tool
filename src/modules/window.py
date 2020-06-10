"""

The window handler.
"""
from sys import argv, exit

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from modules.ui import Ui_window


# TODO:
#   Launchpad selection
#   Button assignment
#   Drag'n'Drop
#   Volume apply
#   Configfiles

class Window:
    def __init__(self, width, height):
        self.app = QApplication(argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_window()
        self.ui.setupUi(self.window)
        # print(self.ui.configbuttons.Open., self.ui.configbuttons.Reset, self.ui.configbuttons.Close, )
        self.__width = width
        self.__height = height
        self.width = width
        self.height = height
        self.running = True
        # self.handler = Thread(target=self.__handler, name="windowhandler")

    @property
    def height(self):
        """

        :return:
        """
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        self.window.resize(self.__width, self.__height)

    @property
    def width(self):
        """

        :return:
        """
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        self.window.resize(self.__width, self.__height)

    # def __handler(self):
    #     while True:
    #         if self.running:
    #             if self.ui.configbuttons.:
    #                 print(self.ui.configfile.text())
    #         else:
    #             exit(1)


if __name__ == "__main__":
    w = Window(640, 480)
    w.window.show()
    # w.handler.start()
    exit(w.app.exec_())
    w.running = False

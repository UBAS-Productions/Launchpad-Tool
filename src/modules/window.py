"""

The window handler.
"""
import json
from os import path
from sys import argv, exit

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from modules.ui import Ui_window


# TODO:
#   ✓ Launchpad selection
#   Button assignment
#   ✓ Drag'n'Drop
#   Volume apply
#   Audiofilelist
#   Active
#   Configfiles

class Window:
    def __init__(self, width, height):
        self.app = QApplication(argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_window()
        self.ui.setupUi(self.window)
        self.ui.launchpadselection.currentIndexChanged.connect(self.selectlaunchpad)
        self.ui.configbuttons.buttons()[0].clicked.connect(self.saveconfig)
        self.ui.configbuttons.buttons()[1].clicked.connect(self.openconfig)
        self.ui.configbuttons.buttons()[2].clicked.connect(self.resetconfig)
        self.config = {}
        self.__button = 1
        self.launchpad = None
        self.changed = False
        self.__width = width
        self.__height = height
        self.width = width
        self.height = height
        self.running = True
        # self.handler = Thread(target=self.__handler, name="windowhandler")

    def addaudio(self):
        self.ui.audiofiles.addItem(
            path.abspath(self.ui.addaudio.text().replace("file://", "").replace("\r", "").replace("\n", "")))

    def selectlaunchpad(self):
        self.launchpad = self.ui.launchpadselection.currentIndex()
        self.changed = True

    def openconfig(self):
        try:
            self.config = json.load(
                open(
                    path.abspath(
                        self.ui.configfile.text().replace("file://", "").replace("\r", "").replace("\n", ""))))
            self.changed = True
        except:
            pass

    def saveconfig(self):
        try:
            json.dump(self.config, open(
                path.abspath(self.ui.configfile.text().replace("file://", "").replace("\r", "").replace("\n", "")),
                "w"),
                      sort_keys=True)
            self.changed = True
        except:
            pass

    def resetconfig(self):
        self.config = {}
        self.changed = True

    @property
    def launchpads(self):
        pass

    @launchpads.setter
    def launchpads(self, launchpads):
        self.ui.launchpadselection.addItems(launchpads)

    @property
    def button(self):
        return self.__button

    @button.setter
    def button(self, button):
        self.__button = button
        self.ui.buttonnumber.setText(f"Button {button}")

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

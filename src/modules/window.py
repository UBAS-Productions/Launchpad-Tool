"""

The window handler.
"""
import json
from os import path
from sys import argv, exit

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from modules.ui import Ui_window


# TODO:
#   ✓ Launchpad selection
#   Button assignment
#   ✓ Drag'n'Drop
#   Volume apply
#   Audiofilelist
#   Activesettings
#   Configfiles
#   Buttonmatrix
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
        self.ui.addbutton.clicked.connect(self.addaudio)
        self.ui.volume.editingFinished.connect(self.edit)
        self.ui.activated.clicked.connect(self.edit)
        self.config = {}
        self.changed = False
        self.button = 16
        self.launchpad = None
        self.__width = width
        self.__height = height
        self.width = width
        self.height = height
        self.running = True

    def edit(self):
        self.config.update({
            int(self.ui.buttonnumber.text().replace("Button ", "")): [
                path.abspath(self.ui.audiofile.text().replace("file://", "").replace("\r", "").replace("\n", "")),
                self.ui.volume.value(),
                self.ui.activated.isChecked()
            ]
        })

    def addaudio(self):
        file = path.abspath(self.ui.addaudio.text().replace("file://", "").replace("\r", "").replace("\n", ""))
        if path.isfile(file) and len(self.ui.audiofiles.findItems(file, Qt.MatchExactly)) == 0:
            self.ui.audiofiles.addItem(file)

    def selectlaunchpad(self):
        self.launchpad = self.ui.launchpadselection.currentIndex()
        self.changed = True

    def openconfig(self):
        try:
            self.config = json.load(
                open(
                    path.abspath(
                        self.ui.configfile.text().replace("file://", "").replace("\r", "").replace("\n", ""))))
        except:
            pass

    def saveconfig(self):
        try:
            json.dump(self.config, open(
                path.abspath(self.ui.configfile.text().replace("file://", "").replace("\r", "").replace("\n", "")),
                "w"),
                      sort_keys=True)
        except:
            pass

    def resetconfig(self):
        self.config = {}

    @property
    def launchpads(self):
        pass

    @launchpads.setter
    def launchpads(self, launchpads):
        self.ui.launchpadselection.addItems(launchpads)

    def setbutton(self, button):
        if button is not None:
            self.button = button
            self.ui.buttonnumber.setText(f"Button {button}")
            c = self.config.get(button, ["", 100.0, True])
            self.ui.audiofile.setText(c[0])
            self.ui.volume.setValue(c[1])
            self.ui.activated.setChecked(c[2])

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

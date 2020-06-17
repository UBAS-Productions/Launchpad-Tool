import json
from os import path
from sys import argv, exit
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from pydub import AudioSegment

from modules.ui import Ui_window


# TODO:
#   ✓ Launchpad selection
#   ✓ Button assignment
#   ✓ Drag'n'Drop
#   ✓ Volume apply
#   ✓ Audiofilelist
#   ✓ Activesettings
#   ✓ Configfiles
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
        self.ui.volume.valueChanged.connect(self.edit)
        self.ui.activated.clicked.connect(self.edit)
        self.ui.replay.clicked.connect(self.edit)
        self.ui.editmode.clicked.connect(self.__editmode)
        self.config = {}
        self.changed = False
        self.button = 16
        self.launchpad = None
        self.editmode = False
        self.__width = width
        self.__height = height
        self.width = width
        self.height = height
        self.running = True

    def __editmode(self):
        self.editmode = self.ui.editmode.isChecked()

    def edit(self):
        Thread(name="edit", target=self.__edit).start()

    def __edit(self):
        try:
            # print(1)
            if self.ui.audiofile.text().replace("file://", "").replace("\r", "").replace("\n", "") != "":
                # print(2)
                c = self.config.get(int(self.ui.buttonnumber.text().replace("Button ", "")), [""])
                # print(3)
                if c[0] != path.abspath(
                        self.ui.audiofile.text().replace("file://", "").replace("\r", "").replace("\n", "")):
                    # print(4)
                    self.config.update({
                        int(self.ui.buttonnumber.text().replace("Button ", "")): [
                            path.abspath(
                                self.ui.audiofile.text().replace("file://", "").replace("\r", "").replace("\n", "")),
                            self.ui.volume.value(),
                            self.ui.activated.isChecked(),
                            self.ui.replay.isChecked(),
                            AudioSegment.from_file(path.abspath(
                                self.ui.audiofile.text().replace("file://", "").replace("\r", "").replace("\n", "")),
                                path.abspath(
                                    self.ui.audiofile.text().replace("file://", "").replace("\r",
                                                                                            "").replace(
                                        "\n", "")).split(".")[-1])
                        ]
                    })
                    # print(5)
                else:
                    # print(6)
                    self.config.update({
                        int(self.ui.buttonnumber.text().replace("Button ", "")): [
                            c[0],
                            self.ui.volume.value(),
                            self.ui.activated.isChecked(),
                            self.ui.replay.isChecked(),
                            c[4]
                        ]
                    })
                    # print(7)
            else:
                # print(8)
                del self.config[int(self.ui.buttonnumber.text().replace("Button ", ""))]
            # print(9)
        except:
            pass
        # print(self.config)

    def addaudio(self):
        file = path.abspath(self.ui.addaudio.text().replace("file://", "").replace("\r", "").replace("\n", ""))
        if path.isfile(file) and len(self.ui.audiofiles.findItems(file, Qt.MatchExactly)) == 0:
            self.ui.audiofiles.addItem(file)

    def selectlaunchpad(self):
        self.launchpad = self.ui.launchpadselection.currentIndex()
        self.changed = True

    def openconfig(self):
        try:
            tmp = {}
            for key, value in json.load(
                    open(
                        path.abspath(
                            self.ui.configfile.text().replace("file://", "").replace("\r", "").replace("\n",
                                                                                                       "")))).items():
                tmp.update({
                    key: value.append(AudioSegment(value[0]))
                })
            self.config = tmp
            del tmp
            Thread(name="setbutton", target=self.setbutton, args=[self.button]).start()
        except:
            pass

    def saveconfig(self):
        try:
            tmp = {}
            for key, value in self.config:
                tmp.update({
                    key: value[:-1]
                })
            json.dump(self.config, open(
                path.abspath(self.ui.configfile.text().replace("file://", "").replace("\r", "").replace("\n", "")),
                "w"),
                      sort_keys=True)
        except:
            pass

    def resetconfig(self):
        self.config = {}
        Thread(name="setbutton", target=self.setbutton, args=[self.button])

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
            c = self.config.get(button, ["", 100.0, True, False])
            # self.ui.audiofile.setText(c[0])
            # self.ui.volume.setValue(c[1])
            # self.ui.activated.setChecked(c[2])
            # self.ui.replay.setChecked(c[3])
            pass

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        self.window.resize(self.__width, self.__height)

    @property
    def width(self):
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

import json
from os import path
from sys import argv, exit
from threading import Thread
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from pydub import AudioSegment

from modules.ui import Ui_window
from modules.ui2 import Ui_Form


# TODO:
#   Buttonmatrix
class Window:
    def __init__(self, width, height):
        self.app = QApplication(argv)
        self.window = QtWidgets.QMainWindow()
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_window()
        self.ui.setupUi(self.window)
        self.ui.launchpadselection.currentIndexChanged.connect(self.selectlaunchpad)
        self.ui.configbuttons.buttons()[0].clicked.connect(self.saveconfig)
        self.ui.configbuttons.buttons()[1].clicked.connect(self.openconfig)
        self.ui.configbuttons.buttons()[2].clicked.connect(self.resetconfig)
        self.ui.addbutton.clicked.connect(self.addaudio)
        self.ui.audiofile.textChanged.connect(self.edit)
        self.ui.volume.valueChanged.connect(self.edit)
        self.ui.activated.clicked.connect(self.edit)
        self.ui.replay.clicked.connect(self.edit)
        self.ui.editmode.clicked.connect(self.__editmode)
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.Form)
        self.config = {}
        self.changed = False
        self.button = 0
        self.buttonchanged = False
        self.launchpad = None
        self.editmode = False
        self.__width = width
        self.__height = height
        self.width = width
        self.height = height
        self.running = True
        self.instances = []
        self.overview_updater = Thread(target=self.__overview_updater)

    def __overview_updater(self):
        while self.running:
            for i, frame in enumerate(self.ui2.frames):
                x, y = i % 8, i // 8
                btn = x + y * 16
                c = self.config.get(btn, ["", 100.0, None])
                # print(frame.styleSheet())
                # if c[2]:
                #     frame.setStyleSheet("background-color: green")
                # elif c[2] is False:
                #     frame.setStyleSheet("background-color: red")
                audiofile = ".".join(path.basename(c[0]).split(".")[:-1])
                timeleft = 0
                for instance in self.instances:
                    if btn in instance:
                        if len(instance[1]) > 0:
                            timeleft = instance[1][-1].time_left
                # print(1)
                self.ui2.labels_2[i].setText(str(timeleft))
                # print(2)
                self.ui2.labels_3[i].setText(str(audiofile))
                # print(3)
            sleep(0.15)

    def __editmode(self):
        self.editmode = self.ui.editmode.isChecked()

    def edit(self):
        Thread(target=self.__edit).start()

    def __edit(self):
        try:
            if self.ui.audiofile.text() != "":
                c = self.config.get(int(self.ui.buttonnumber.text().replace("Button ", "")), [""])
                if c[0] != path.abspath(
                        self.ui.audiofile.text().replace("file://", "").replace("\r", "").replace("\n", "")):
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
                else:
                    self.config.update({
                        int(self.ui.buttonnumber.text().replace("Button ", "")): [
                            c[0],
                            self.ui.volume.value(),
                            self.ui.activated.isChecked(),
                            self.ui.replay.isChecked(),
                            c[4]
                        ]
                    })
            else:
                self.config.update({
                    int(self.ui.buttonnumber.text().replace("Button ", "")): [
                        "",
                        self.ui.volume.value(),
                        self.ui.activated.isChecked(),
                        self.ui.replay.isChecked()
                    ]
                })
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

    def __openconfig(self):
        Thread(target=self.openconfig).start()

    def openconfig(self):
        try:
            self.config.clear()
            config = json.load(
                open(
                    path.abspath(
                        self.ui.configfile.text().replace("file://", "").replace("\r", "").replace("\n", ""))))
            # print(config)
            for key, value in config.items():
                if value[0] != "":
                    value.append(AudioSegment.from_file(value[0]))
                self.config.update({
                    int(key): value
                })
            # print(self.config)
            Thread(target=self.setbutton, args=[self.button]).start()
        except:
            pass

    def __saveconfig(self):
        Thread(target=self.saveconfig).start()

    def saveconfig(self):
        try:
            tmp = {}
            for key, value in self.config.items():
                # print(key, value)
                # print(key, value[:-1])
                value = value[:-1]
                tmp.update({
                    key: value
                })
            json.dump(tmp, open(
                path.abspath(self.ui.configfile.text().replace("file://", "").replace("\r", "").replace("\n", "")),
                "w"),
                      sort_keys=True)
        except:
            pass

    def resetconfig(self):
        self.config.clear()
        Thread(target=self.setbutton, args=[self.button]).start()

    @property
    def launchpads(self):
        return

    @launchpads.setter
    def launchpads(self, launchpads):
        self.ui.launchpadselection.addItems(launchpads)

    def setbutton(self, button):
        if button is not None:
            self.button = button
            self.ui.buttonnumber.setText(f"Button {button}")
            self.buttonchanged = True
            # NOTE:
            # Those are segmentation faults!
            # self.ui.audiofile.setText(c[0])
            # self.ui.volume.setValue(c[1])
            # self.ui.activated.setChecked(c[2])
            # self.ui.replay.setChecked(c[3])
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


if __name__ == "__main__":
    w = Window(640, 480)
    w.window.show()
    exit(w.app.exec_())
    w.running = False

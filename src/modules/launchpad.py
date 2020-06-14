"""

The Launchpad handler.
"""
from threading import Thread
from time import sleep

import launchpad_py as launchpad
from pygame import midi


def SearchDevices(name, output=True, input=True):
    ret = []

    for n in range(midi.get_count()):
        md = midi.get_device_info(n)
        if name.lower() in str(md[1]).lower():
            if output is True and md[3] > 0:
                ret.append(str(md[1], "UTF-8"))
            if input is True and md[2] > 0:
                ret.append(str(md[1], "UTF-8"))
    return ret


# TODO:
#   JSON Settings
#   Button press: Start/Stop
#   Button hold: Loop/Unloop
#   Button double press: Enable/Disable (maybe?)
#   Window with time left for sound with activated TC
class Launchpad:
    def __init__(self):
        self.lp = launchpad.Launchpad()
        self.config = {}
        self.__launchpad = None
        self.button = 16
        self.running = True
        self.handler = Thread(name="launchpadhandler", target=self.__handler)
        self.setbutton = None
        self.action = None

    def open(self, lp):
        self.lp.Open(lp)
        self.reset()
        self.lp.LedAllOn()
        sleep(1)
        self.reset()

    def reset(self):
        self.lp.Reset()

    def close(self):
        self.lp.Close()
        self.isopen = False

    def get_button(self):
        button = self.lp.ButtonStateXY()
        return button[0:2] if len(button) > 0 and button[2] and not button[0] > 7 else None

    def __handler(self):
        try:
            while self.running:
                button = self.get_button()
                if button is not None:
                    self.button = button[0] + button[1] * 16
                    # print(self.button)
                    self.action(self.button)
                    self.setbutton(self.button)
        except:
            exit(0)
        exit(0)

    @property
    def launchpads(self):
        return SearchDevices("Launch")

    @property
    def launchpad(self):
        pass

    @launchpad.setter
    def launchpad(self, lp):
        # try:
        #     self.close()
        # except:
        #     pass
        try:
            if lp is not self.__launchpad:
                self.__launchpad = lp
                self.open(lp)
        except:
            pass

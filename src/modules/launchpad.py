"""

The Launchpad handler.
"""
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
        self.__config = {}
        self.__launchpad = None

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

    @property
    def launchpads(self):
        return SearchDevices("Launch")

    @property
    def launchpad(self):
        pass

    @launchpad.setter
    def launchpad(self, lp):
        try:
            if lp is not self.__launchpad:
                self.__launchpad = lp
                self.open(lp)
        except:
            pass

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, config):
        self.__config = config

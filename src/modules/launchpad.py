from threading import Thread
from time import sleep, time

import launchpad_py as launchpad
from pygame import midi

midi.init()


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
        self.button = 0
        self.instances = {}
        self.blink = {}
        self.running = True
        self.handler = Thread(name="launchpadhandler", target=self.__handler)
        self.led_handler = Thread(name="led_handler", target=self.__led_handler)
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
        return button[0:2] if len(button) > 0 and button[2] and not button[0] > 7 and not button[1] < 1 else None

    def __handler(self):
        try:
            while self.running:
                button = self.get_button()
                if button is not None:
                    self.button = button[0] + (button[1] - 1) * 16
                    # print(self.button)
                    Thread(name=self.button, target=self.action, args=[self.button]).start()
                    Thread(name="setbutton", target=self.setbutton, args=[self.button]).start()
                sleep(0.01)
        except:
            exit(0)
        exit(0)

    def __led_handler(self):
        while True:
            try:
                self.lp.Reset()
                for btn, c in self.config.items():
                    if c[0] != "":
                        if c[2]:
                            try:
                                if self.instances.get(btn, None).playing():
                                    if self.blink.get(btn, [1, 1])[0] < time() - 1:
                                        self.lp.LedCtrlXY(btn % 16, btn // 16 + 1, 0, 3)
                                        self.blink.update({btn: [time(), 2]})
                                    elif self.blink.get(btn, [1, 2])[0] < time() - 1:
                                        self.lp.LedCtrlXY(btn % 16, btn // 16 + 1, 0, 0)
                                        self.blink.update({btn: [time(), 1]})
                            except:
                                self.lp.LedCtrlXY(btn % 16, btn // 16 + 1, 0, 3)
                        else:
                            self.lp.LedCtrlXY(btn % 16, btn // 16 + 1, 3, 0)
                sleep(0.2)
            except:
                pass

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

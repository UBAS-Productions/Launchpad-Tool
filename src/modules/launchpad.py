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
        self.instances = []
        self.blink = {}
        self.running = True
        self.isopen = False
        self.handler = Thread(target=self.__handler)
        self.led_handler = Thread(target=self.__led_handler)
        self.setbutton = None
        self.action = None

    def open(self, lp):
        self.lp.Open(lp)
        self.reset()
        self.lp.LedAllOn()
        sleep(1)
        self.reset()
        self.isopen = True

    def reset(self):
        self.lp.Reset()

    def close(self):
        self.isopen = False
        self.reset()
        self.lp.Close()

    def get_button(self):
        button = self.lp.ButtonStateXY()
        return button[0:2] if len(button) > 0 and button[2] and not button[0] > 7 and not button[1] < 1 else None

    def __handler(self):
        try:
            while self.running:
                while self.isopen:
                    button = self.get_button()
                    if button is not None:
                        self.button = button[0] + (button[1] - 1) * 16
                        # print(self.button)
                        Thread(target=self.action, args=[self.button]).start()
                        Thread(target=self.setbutton, args=[self.button]).start()
                    sleep(0.01)
        except:
            exit(0)
        exit(0)

    def __led_handler(self):
        while self.running:
            while self.isopen:
                try:
                    l = []
                    # self.lp.Reset()
                    for btn, c in self.config.items():
                        if c != ["", 100.0, True, False]:
                            # print(c)
                            l.append(btn)
                            Thread(target=self.led, args=[btn, c]).start()
                    remove = []
                    for x in range(8):
                        for y in range(8):
                            remove.append(x + y * 16)
                    for led in remove:
                        if not led in l:
                            self.lp.LedCtrlRaw(led, 0, 0)
                    sleep(0.05)
                except:
                    pass

    def led(self, btn, c):
        # print(c)
        if c[2]:
            try:
                tmp = False
                for instance in self.instances:
                    # print(instance, btn)
                    if instance[0] == btn and len(instance[1]) > 0:
                        if instance[1][-1].playing:
                            tmp = True
                            b = self.blink.get(btn, [1, 1])
                            # print(b)
                            # print(instance)
                            # print(b[0])
                            if b[0] < time() - .5:
                                if b[1] == 1:
                                    self.lp.LedCtrlRaw(btn, 3, 3)
                                    self.blink.update({btn: [time(), 2]})
                                elif b[1] == 2:
                                    self.lp.LedCtrlRaw(btn, 0, 0)
                                    self.blink.update({btn: [time(), 1]})
                if not tmp:
                    self.lp.LedCtrlRaw(btn, 0, 3)
            except:
                pass
        else:
            self.lp.LedCtrlXY(btn % 16, btn // 16 + 1, 3, 0)

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

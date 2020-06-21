from threading import Thread
from time import sleep, time

from pydub.playback import _play_with_simpleaudio as play
from simpleaudio.functionchecks import LeftRightCheck


def __audiotest():
    LeftRightCheck.run(0)


def stopall():
    for instance in instances:
        for i in instance[1]:
            i.stop()


instances = []
config = {}
editmode = False
running = True


def action(button):
    c = config.get(button, ["", 100.0, False, False])
    # print(c)
    if c[2] and not editmode:
        for instance in instances:
            if button in instance and len(instance[1]) > 0:
                if c[3] and not c[0] == "":
                    instance[1].append(Audio(c[4], c[1]))
                else:
                    for i in instance[1]:
                        i.stop()
                    instances.remove(instance)
                return
        if not c[0] == "":
            instances.append([button, [Audio(c[4], c[1])]])


# def action(button):
#     global instances
#     if not editmode:
#         c = config.get(button, ["", 100.0, False, False, None])
#         if c[2] and c[0] != "":
#             if len(instances):
#                 for btn, instance in instances.items():
#                     if button == btn:
#                         if not c[3]:
#                             for i in instance:
#                                 i.stop()
#                             instances.pop(btn)
#                             return
#                         else:
#                             instance.append(Audio(c[4], c[1]))
#             instances.update({button: [Audio(c[4], c[1])]})


class Audio(Thread):
    def __init__(self, src_audio, volume=100):
        Thread.__init__(self)
        self.output = None
        self.src_audio = src_audio
        self.volume = volume
        self.started = None
        self.start()

    def run(self):
        self.play()
        self.started = time()
        while self.output.is_playing():
            if running:
                sleep(0.1)
            else:
                break
        self.remove()

    def play(self):
        try:
            self.output = play(self.audio)
        except:
            pass

    def stop(self):
        try:
            self.output.stop()
        except:
            pass

    def remove(self):
        global instances
        for btn, instance in instances:
            try:
                instance.remove(self)
            except:
                pass
            finally:
                exit(0)

    @property
    def time_left(self):
        try:
            if self.playing:
                duration = len(self.src_audio) / 1000
                left = duration - (time() - self.started)
                return int(left)
        except:
            return None

    @property
    def playing(self):
        try:
            return self.output.is_playing()
        except:
            pass
        return False

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume
        self.audio = self.src_audio + ((self.src_audio.dBFS * (100 / volume)) - self.src_audio.dBFS)

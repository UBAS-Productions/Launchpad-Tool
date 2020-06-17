from threading import Thread

import numpy as np
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play
from simpleaudio.functionchecks import LeftRightCheck


def __audiotest():
    LeftRightCheck.run(0)


instances = np.array([])
config = {}
editmode = False


def action(button):
    global instances
    # print(config)
    if not editmode:
        c = config.get(button, ["", 100.0, False, False])
        # print(c[2] and c[0] != "" and not editmode)
        instances.view(instances.dtype).sort(order=['f0'], axis=0)
        if c[2] and c[0] != "":
            try:
                with np.where(instances == button)[0][0] as i:
                    if button in instances[i] and not c[3]:
                        instances[i][1].stop()
                        return
            except:
                pass
            tmp = Audio(c[0], c[1])
            # tmp.start()
            instances = np.append(instances, [button, tmp])


class Audio(Thread):
    def __init__(self, audiofile, volume=100):
        Thread.__init__(self)
        self.output = None
        self.audiofile = audiofile
        self.src_audio = AudioSegment.from_file(self.audiofile, self.audiofile.split(".")[-1])
        self.volume = volume
        self.start()

    def run(self):
        self.play()
        self.output.wait_done()
        self.remove()

    def play(self):
        try:
            self.output = play(self.audio)
        except RuntimeWarning:
            quit()

    def stop(self):
        try:
            self.output.stop()
            self.remove()
        except:
            pass

    def remove(self):
        global instances
        instances = np.delete(instances, np.where(instances[1] == self))

    @property
    def playing(self):
        try:
            return self.output.is_playing()
        except:
            return False

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume
        self.audio = self.src_audio + ((self.src_audio.dBFS * (100 / volume)) - self.src_audio.dBFS)

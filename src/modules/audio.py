from threading import Thread

from pydub.playback import _play_with_simpleaudio as play
from simpleaudio.functionchecks import LeftRightCheck


def __audiotest():
    LeftRightCheck.run(0)


instances = {}
config = {}
editmode = False


def action(button):
    global instances
    if not editmode:
        c = config.get(button, ["", 100.0, False, False, None])
        # print(c)
        print("---")
        print(1)
        if c[2]:
            print(2)
            if len(instances):
                for btn, instance in instances.items():
                    print(3)
                    if button == btn and not c[3]:
                        print(4)
                        instance.stop()
                        print(5)
                        instances.pop(btn)
                        print(6)
                        return
                pass
            print(7)
            instances.update({button: Audio(c[4], c[1])})
            print(8)
            # print(instances[-1][1].playing)


# def JITInitialiser(audiofile):

class Audio(Thread):
    def __init__(self, src_audio, volume=100):
        Thread.__init__(self)
        self.output = None
        self.src_audio = src_audio
        self.volume = volume
        self.start()

    def run(self):
        # while self.src_audio is None:
        #     pass
        self.play()
        self.output.wait_done()
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
        for btn, instance in instances.items():
            if instance == self:
                instances.pop(btn)

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

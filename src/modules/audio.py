from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play
from simpleaudio.functionchecks import LeftRightCheck


def __audiotest():
    LeftRightCheck.run(0)


instances = []
config = {}


def action(button):
    # print(config)
    c = config.get(button, ["", 100.0, False, False])
    if c[2]:
        for instance in instances:
            if button in instance:
                if c[3]:
                    instance[1].append(Audio(c[0], c[1]))
                else:
                    for i in instance[1]:
                        i.stop()
                    instances.remove(instance)
                return
        instances.append([button, [Audio(c[0], c[1])]])


class Audio:  # Thread):
    """

    Audio handler.
    """

    def __init__(self, audiofile, volume=100):
        self.output = None
        self.audiofile = audiofile
        self.src_audio = AudioSegment.from_file(self.audiofile, self.audiofile.split(".")[-1])
        self.volume = volume
        self.play()
    def play(self):
        try:
            self.output = play(self.audio)
        except:
            pass

    def stop(self):
        """

        Stopps the playing audio.
        """
        try:
            self.output.stop()
        except:
            pass

    @property
    def playing(self):
        """

        :return:
        """
        try:
            return self.output.is_playing()
        except:
            return False

    @property
    def volume(self):
        """

        :return:
        """
        return self.__volume

    @volume.setter
    def volume(self, volume):
        """

        :type volume: int
        """
        self.__volume = volume
        self.audio = self.src_audio + ((self.src_audio.dBFS * (100 / volume)) - self.src_audio.dBFS)

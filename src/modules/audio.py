import os

from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play
from simpleaudio.functionchecks import LeftRightCheck


def audiotest():
    LeftRightCheck.run(0)
class Audio:
    """

    Audio handler.
    """

    def __init__(self, audiofile, volume=100):
        self.output = None
        self.audiofile = audiofile
        self.src_audio = AudioSegment.from_file(self.audiofile, self.audiofile.split(".")[-1])
        self.volume = volume

    def play(self):
        """

        """
        try:
            self.output = play(self.audio)
        except RuntimeWarning:
            quit()

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
        print(self.src_audio.dBFS)
        self.audio = self.src_audio + ((self.src_audio.dBFS * (100 / volume)) - self.src_audio.dBFS)
        print(self.audio.dBFS)


if __name__ == "__main__":
    import time

    path = os.path.join(os.getcwd(), "file.mp3")
    print(path)
    test = Audio(path)
    test.play()
    print(test.playing)
    time.sleep(1000)
    test.stop()

# button1audio = Audio(path)
# button1audio.play()

import os

from pydub import AudioSegment


class Audio:
    def __init__(self, audiofile):
        self.audiofile = audiofile
        self.playing = False

    def play(self):
        self.playing = True
        try:
            AudioSegment.from_file(self.audiofile, self.audiofile.split(".")[-1])
        except RuntimeWarning:
            quit()

    def stop(self):
        self.playing = False


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "file.mp3")
    print(path)
    test = Audio(path)
    test.play()
# button1audio = Audio(path)
# button1audio.play()

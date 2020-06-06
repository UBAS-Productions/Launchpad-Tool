from pydub import AudioSegment


class Audio:
    def __init__(self, audiofile):
        self.audiofile = audiofile
        self.playing = False

    def play(self):
        self.playing = True
        AudioSegment.from_file(self.audiofile)

    def stop(self):
        self.playing = False
button1audio = Audio(path)
button1audio.play()

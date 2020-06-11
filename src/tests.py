import unittest
from os import path, getcwd
from time import sleep

from modules.audio import Audio


class AudioTest(unittest.TestCase):
    def test_audio(self):
        filepath = path.join(getcwd(), "test.mp3")
        test = Audio(filepath)
        test.play()
        sleep(1)
        self.assertEqual(test.playing, True)
        test.stop()
        sleep(1)
        self.assertEqual(test.playing, False)


if __name__ == '__main__':
    unittest.main()

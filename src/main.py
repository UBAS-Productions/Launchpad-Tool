from threading import Thread

from modules import audio
from modules.audio import __audiotest
from modules.launchpad import Launchpad
from modules.window import Window


# Functions
def cleanup():
    lp.reset()
    lp.close()


def __update():
    while running:
        if w.changed:
            lp.launchpad = w.launchpad
        if w.ui.addaudio.changed:
            w.addaudio()
            w.ui.addaudio.changed = False
        if w.ui.audiofile.changed:
            w.edit()
            w.ui.audiofile.changed = False
    exit(0)


running = True
# Window initialisation
w = Window(640, 480)
w.window.show()
# Launchpad initialisation
lp = Launchpad()
# Sync
w.launchpads = lp.launchpads
lp.config = w.config
lp.launchpad = w.launchpad
lp.running = running
lp.action = audio.action
lp.setbutton = w.setbutton
audio.config = w.config
# Audiotest
audiotest = Thread(name="audiotest", target=__audiotest)
# audiotest.start()
# Threads
update = Thread(name="update", target=__update)
update.start()
lp.handler.start()
lp.led_handler.start()
# Exit on command
exitcode = w.app.exec_()
running = False
cleanup()
exit(exitcode)

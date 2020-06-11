from threading import Thread

from modules.launchpad import Launchpad
from modules.window import Window


# Functions
def cleanup():
    lp.close()


def __sync():
    while running:
        if w.changed:
            lp.config = w.config
            lp.launchpad = w.launchpad
            w.changed = False
        if w.ui.addaudio.changed:
            w.addaudio()
            w.ui.addaudio.changed = False
        if w.ui.audiofile.changed:
            w.ui.addaudio.changed = False
    exit(0)


running = True
# Window initialisation
w = Window(640, 480)
w.window.show()
# Launchpad initialisation
lp = Launchpad()
w.launchpads = lp.launchpads
# Audiotest
# audiotest()

# Threads
# w.handler.start()
sync = Thread(name="sync", target=__sync)
sync.start()

# Exit on command
exitcode = w.app.exec_()
# w.running = False
running = False
cleanup()
exit(exitcode)

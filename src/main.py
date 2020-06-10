from modules.audio import audiotest
from modules.window import Window

# Window initialisation
w = Window(640, 480)
w.window.show()
# w.handler.start()
# Audiotest
audiotest()
# Exit on command
exitcode = w.app.exec_()
# w.running = False
exit(exitcode)

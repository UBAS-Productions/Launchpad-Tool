from modules.audio import audiotest
from modules.window import Window

# Window initialisation
w = Window(640, 480)
w.window.show()
# Audiotest
audiotest()
# Exit on command
exit(w.app.exec_())

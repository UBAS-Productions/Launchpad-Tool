"""

The Launchpad handler.
"""
import launchpad_py as launchpad

try:
    lp = launchpad.Launchpad()
    lp.Open()
    lp.Reset()
except:
    pass
# TODO:
#   JSON Settings
#   Button press: Start/Stop
#   Button hold: Loop/Unloop
#   Button double press: Enable/Disable (maybe?)

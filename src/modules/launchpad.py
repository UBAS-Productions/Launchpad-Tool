"""

The Launchpad handler.
"""
import launchpad_py as launchpad

lp = launchpad.Launchpad()
lp.Open()
lp.Reset()

# TODO:
#   JSON Settings
#   Button press: Start/Stop
#   Button hold: Loop/Unloop
#   Button double press: Enable/Disable (maybe?)

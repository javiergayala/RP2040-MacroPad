"""Constant definitions for app key sequences."""

from micropython import const
from adafruit_hid.keycode import Keycode

# Keys

ZOOM_KEY = [Keycode.LEFT_CONTROL, Keycode.F13]
TEAMS_KEY = [Keycode.F16]
IMSG_KEY = [Keycode.F17]
ITERM_KEY = [Keycode.F18]
FIREFOX_KEY = [Keycode.F19]
SAFARI_KEY = [Keycode.F13]
VSCODE_KEY = [Keycode.COMMAND, Keycode.HOME]

# Colors

ZOOM_COLOR = const(0x2D8CFF)
TEAMS_COLOR = const(0x6264A7)
IMSG_COLOR = const(0x34C759)
ITERM_COLOR = const(0xA2A8A3)
FIREFOX_COLOR = const(0xA44900)
SAFARI_COLOR = const(0xCC1111)
VSCODE_COLOR = const(0x0078D7)

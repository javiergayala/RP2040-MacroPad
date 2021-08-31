# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import *

app = {  # REQUIRED dict, must be named 'app'
    "name": "DEFAULT",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, "Zoom", ZOOM_KEY),
        (0x000000, "Teams", TEAMS_KEY),
        (0x000000, "iMsg", IMSG_KEY),
        # 2nd row ----------
        (0x000000, "iTerm", ITERM_KEY),
        (0x000000, "Firefox", FIREFOX_KEY),
        (0x000000, "Safari", SAFARI_KEY),
        # 3rd row ----------
        (0x000000, "Lock", [Keycode.CONTROL, Keycode.COMMAND, Keycode.Q]),
        (0x000000, "Amph", [Keycode.CONTROL, Keycode.COMMAND, Keycode.F17]),
        (0x000000, "VSCode", [Keycode.COMMAND, Keycode.HOME]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (0x800000, "Home", []),  # Digi-Key in new window
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

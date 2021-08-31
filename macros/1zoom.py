# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import *

app = {  # REQUIRED dict, must be named 'app'
    "name": "Zoom",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (ZOOM_COLOR, "Mute", [ZOOM_KEY, [Keycode.SHIFT, Keycode.COMMAND, "A"]]),
        (ZOOM_COLOR, "Mute ALL", [ZOOM_KEY, [Keycode.CONTROL, Keycode.COMMAND, "M"]]),
        (ZOOM_COLOR, "Chat", [ZOOM_KEY, [Keycode.SHIFT, Keycode.COMMAND, "H"]]),
        # 2nd row ----------
        (ZOOM_COLOR, "Camera", [ZOOM_KEY, [Keycode.SHIFT, Keycode.COMMAND, "V"]]),
        (ZOOM_COLOR, "Share", [ZOOM_KEY, [Keycode.SHIFT, Keycode.COMMAND, "S"]]),
        (0x000000, "", []),
        # 3rd row ----------
        (ZOOM_COLOR, "Join", [ZOOM_KEY, [Keycode.COMMAND, "J"]]),
        (ZOOM_COLOR, "Start Mtg", [ZOOM_KEY, [Keycode.CONTROL, Keycode.COMMAND, "V"]]),
        (ZOOM_COLOR, "Leave", [ZOOM_KEY, [Keycode.COMMAND, "W"]]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (0x800000, "Home", []),  # Digi-Key in new window
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

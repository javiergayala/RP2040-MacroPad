# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import ZOOM_COLOR, ZOOM_KEY

app = {  # REQUIRED dict, must be named 'app'
    "name": "Zoom",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (ZOOM_COLOR, "Mute", [Keycode.SHIFT, Keycode.COMMAND, "A"]),
        (ZOOM_COLOR, "Mute ALL", [Keycode.CONTROL, Keycode.COMMAND, "M"]),
        (ZOOM_COLOR, "Chat", [Keycode.SHIFT, Keycode.COMMAND, "H"]),
        # 2nd row ----------
        (ZOOM_COLOR, "Camera", [Keycode.SHIFT, Keycode.COMMAND, "V"]),
        (ZOOM_COLOR, "Share", [Keycode.SHIFT, Keycode.COMMAND, "S"]),
        (0x000000, "", []),
        # 3rd row ----------
        (ZOOM_COLOR, "Join", [Keycode.COMMAND, "J"]),
        (ZOOM_COLOR, "Start Mtg", [Keycode.CONTROL, Keycode.COMMAND, "V"]),
        (ZOOM_COLOR, "Leave", [Keycode.COMMAND, "W"]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (ZOOM_COLOR, "Zoom", ZOOM_KEY),
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

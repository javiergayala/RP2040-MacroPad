# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import IMSG_COLOR, IMSG_KEY

app = {  # REQUIRED dict, must be named 'app'
    "name": "iMessage",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (IMSG_COLOR, "Emoji", [Keycode.CONTROL, Keycode.COMMAND, " "]),
        (IMSG_COLOR, "Reply", [Keycode.COMMAND, "R"]),
        (IMSG_COLOR, "Tapback", [Keycode.SHIFT, "T"]),
        # 2nd row ----------
        (IMSG_COLOR, "Details", [Keycode.COMMAND, "I"]),
        (IMSG_COLOR, "SndFile", [Keycode.OPTION, Keycode.COMMAND, "F"]),
        (0x000000, "", []),  # Scroll down
        # 3rd row ----------
        (IMSG_COLOR, "Previous", [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x000000, "", []),
        (IMSG_COLOR, "Next", [Keycode.CONTROL, Keycode.TAB]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (IMSG_COLOR, "iMessage", IMSG_KEY),
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}
# Write your code here :-)

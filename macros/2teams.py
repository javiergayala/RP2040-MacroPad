# MACROPAD Hotkeys example: TEAMS web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import TEAMS_COLOR, TEAMS_KEY

app = {  # REQUIRED dict, must be named 'app'
    "name": "MS Teams",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (TEAMS_COLOR, "Activity", [Keycode.COMMAND, "1"]),
        (TEAMS_COLOR, "Chat", [Keycode.COMMAND, "2"]),
        (TEAMS_COLOR, "Teams", [Keycode.COMMAND, "3"]),  # Scroll ]up
        # 2nd row ----------
        (TEAMS_COLOR, "Ex Comp", [Keycode.COMMAND, Keycode.SHIFT, "X"]),
        (TEAMS_COLOR, "Send", [Keycode.COMMAND, Keycode.RETURN]),
        (TEAMS_COLOR, "Attach", [Keycode.COMMAND, "O"]),  # Scroll down
        # 3rd row ----------
        (TEAMS_COLOR, "\\n", [Keycode.SHIFT, Keycode.RETURN]),
        (TEAMS_COLOR, "Home", [Keycode.OPTION, "H"]),
        (TEAMS_COLOR, "Private", [Keycode.COMMAND, Keycode.SHIFT, "P"]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (TEAMS_COLOR, "Teams", TEAMS_KEY),
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

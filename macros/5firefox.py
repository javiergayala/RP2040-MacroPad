# MACROPAD Hotkeys example: FIREFOX web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import FIREFOX_COLOR, FIREFOX_KEY

app = {  # REQUIRED dict, must be named 'app'
    "name": "Firefox",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (FIREFOX_COLOR, "< Back", [Keycode.COMMAND, Keycode.LEFT_ARROW]),
        (FIREFOX_COLOR, "Fwd >", [Keycode.COMMAND, Keycode.RIGHT_ARROW]),
        (FIREFOX_COLOR, "Up", [Keycode.SHIFT, " "]),  # Scroll ]up
        # 2nd row ----------
        (FIREFOX_COLOR, "< Tab", [Keycode.COMMAND, Keycode.OPTION, Keycode.LEFT_ARROW]),
        (
            FIREFOX_COLOR,
            "Tab >",
            [Keycode.COMMAND, Keycode.OPTION, Keycode.RIGHT_ARROW],
        ),
        (FIREFOX_COLOR, "Down", [" "]),  # Scroll down
        # 3rd row ----------
        (FIREFOX_COLOR, "Reload", [Keycode.COMMAND, "r"]),
        (FIREFOX_COLOR, "Home", [Keycode.OPTION, "H"]),
        (FIREFOX_COLOR, "Private", [Keycode.COMMAND, Keycode.SHIFT, "P"]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (FIREFOX_COLOR, "Firefox", FIREFOX_KEY),
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

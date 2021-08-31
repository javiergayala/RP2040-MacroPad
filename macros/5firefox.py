# MACROPAD Hotkeys example: FIREFOX web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import *

app = {  # REQUIRED dict, must be named 'app'
    "name": "Firefox",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (FIREFOX_COLOR, "< Back", [FIREFOX_KEY, [Keycode.COMMAND, Keycode.LEFT_ARROW]]),
        (FIREFOX_COLOR, "Fwd >", [FIREFOX_KEY, [Keycode.COMMAND, Keycode.RIGHT_ARROW]]),
        (FIREFOX_COLOR, "Up", [FIREFOX_KEY, [Keycode.SHIFT, " "]]),  # Scroll ]up
        # 2nd row ----------
        (
            FIREFOX_COLOR,
            "< Tab",
            [FIREFOX_KEY, [Keycode.COMMAND, Keycode.OPTION, Keycode.LEFT_ARROW]],
        ),
        (
            FIREFOX_COLOR,
            "Tab >",
            [FIREFOX_KEY, [Keycode.COMMAND, Keycode.OPTION, Keycode.RIGHT_ARROW]],
        ),
        (FIREFOX_COLOR, "Down", [FIREFOX_KEY, [" "]]),  # Scroll down
        # 3rd row ----------
        (FIREFOX_COLOR, "Reload", [FIREFOX_KEY, [Keycode.COMMAND, "r"]]),
        (FIREFOX_COLOR, "Home", [FIREFOX_KEY, [Keycode.OPTION, "H"]]),
        (
            FIREFOX_COLOR,
            "Private",
            [FIREFOX_KEY, [Keycode.COMMAND, Keycode.SHIFT, "P"]],
        ),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (0x800000, "Home", []),  # Digi-Key in new window
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

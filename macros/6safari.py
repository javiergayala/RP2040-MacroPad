# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import SAFARI_COLOR, SAFARI_KEY

app = {  # REQUIRED dict, must be named 'app'
    "name": "Mac Safari",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (SAFARI_COLOR, "< Back", [SAFARI_KEY, [Keycode.COMMAND, "["]]),
        (SAFARI_COLOR, "Fwd >", [SAFARI_KEY, [Keycode.COMMAND, "]"]]),
        (SAFARI_COLOR, "Up", [SAFARI_KEY, [Keycode.SHIFT, " "]]),  # Scroll ]up
        # 2nd row ----------
        (
            SAFARI_COLOR,
            "< Tab",
            [SAFARI_KEY, [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]],
        ),
        (SAFARI_COLOR, "Tab >", [SAFARI_KEY, [Keycode.CONTROL, Keycode.TAB]]),
        (SAFARI_COLOR, "Down", " "),  # Scroll down
        # 3rd row ----------
        (SAFARI_COLOR, "Reload", [SAFARI_KEY, [Keycode.COMMAND, "r"]]),
        (SAFARI_COLOR, "Home", [SAFARI_KEY, [Keycode.COMMAND, "H"]]),
        (SAFARI_COLOR, "Private", [SAFARI_KEY, [Keycode.COMMAND, "N"]]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (SAFARI_COLOR, "Safari", SAFARI_KEY),
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

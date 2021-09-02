# MACROPAD Hotkeys example: VSCODE web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import VSCODE_COLOR, VSCODE_KEY

app = {  # REQUIRED dict, must be named 'app'
    "name": "VS Code",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (VSCODE_COLOR, "Cmd Pal", [Keycode.SHIFT, Keycode.COMMAND, "P"]),
        (VSCODE_COLOR, "Xplorer", [Keycode.SHIFT, Keycode.COMMAND, "E"]),
        (VSCODE_COLOR, "Search", [Keycode.SHIFT, Keycode.COMMAND, "F"]),
        # 2nd row ----------
        (VSCODE_COLOR, "Ext.", [Keycode.COMMAND, Keycode.SHIFT, "X"]),
        (VSCODE_COLOR, "Problem", [Keycode.COMMAND, Keycode.SHIFT, "M"]),
        (VSCODE_COLOR, "Output", [Keycode.COMMAND, Keycode.SHIFT, "U"]),  # Scroll down
        # 3rd row ----------
        (VSCODE_COLOR, "Term.", [Keycode.CONTROL, "`"]),
        (VSCODE_COLOR, "Replace", [Keycode.OPTION, Keycode.COMMAND, "F"]),
        (VSCODE_COLOR, "Comment", [Keycode.COMMAND, "/"]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (VSCODE_COLOR, "VSCODE", VSCODE_KEY),
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

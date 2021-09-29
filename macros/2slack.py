# MACROPAD Hotkeys example: TEAMS web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from key_constants import SLACK_COLOR, SLACK_KEY

app = {  # REQUIRED dict, must be named 'app'
    "name": "Slack",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (SLACK_COLOR, "React", [Keycode.SHIFT, Keycode.COMMAND, Keycode.BACKSLASH]),
        (SLACK_COLOR, "Quote", [Keycode.SHIFT, Keycode.COMMAND, "9"]),
        (SLACK_COLOR, "Code", [Keycode.OPTION, Keycode.SHIFT, Keycode.COMMAND, "c"]),
        # 2nd row ----------
        (SLACK_COLOR, "Mk Rd", [Keycode.ESCAPE]),
        (SLACK_COLOR, "Mk AllRd", [Keycode.SHIFT, Keycode.ESCAPE]),
        (SLACK_COLOR, "Thread", [Keycode.T]),  # Scroll down
        # 3rd row ----------
        (SLACK_COLOR, "\\n", [Keycode.SHIFT, Keycode.RETURN]),
        (SLACK_COLOR, "Remind", [Keycode.M]),
        (SLACK_COLOR, "NextMsg", [Keycode.OPTION, Keycode.SHIFT, Keycode.DOWN_ARROW]),
        # 4th row ----------
        (0x000000, "<--", []),  # Adafruit in new window
        (SLACK_COLOR, "Slack", SLACK_KEY),
        (0x000000, "-->", []),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # Close window/tab
    ],
}

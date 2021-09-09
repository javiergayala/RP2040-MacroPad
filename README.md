# RP2040-MacroPad ![language](https://img.shields.io/badge/language-python-blue.svg)

> CircuitPython 7.x Software for the Adafruit RP2040 Macropad

## :books: Table of Contents

- [Installation](#package-installation)
- [Usage](#rocket-usage)
- [Support](#hammer_and_wrench-support)
- [Contributing](#memo-contributing)
- [Credits](#credits)

## :package: Installation

1. Copy the contents of the repo to the `CIRCUITPY` drive.

    ```sh
    cp boot.py ${CIRCUITPY}/
    cp code.py ${CIRCUITPY}/
    cp key_constants.py ${CIRCUITPY}/
    cp -a lib ${CIRCUITPY}/
    cp -a macros ${CIRCUITPY}/
    ```

2. Reset the RP2040MacroPad

### If something goes wrong

Once you boot off of this software, you will no longer see a `CIRCUITPY` drive, thanks to the command in the `boot.py` file that disables the USB drive.  If you need to re-enable the drive, you'll have to boot into "Safe Mode".

#### CircuitPython 7.x Safe Mode

1. Press the reset button on the side of the device
2. While the light for the top left button is blinking, press the reset button one more time
3. To exit Safe Mode, **Eject the `CIRCUITPY` drive**, then unplug the device and plug it back in

## :rocket: Usage

The bottom row (detailed in the table below) have the following functions:

| Bottom Left | Bottom Center  |  Bottom Right |
|---|---|---|
| Page Right  | Application  | Page Left  |

The "Page Right" button will take you to the MacroPad page to the right of your current one, conversely the "Page Left" will take you to the MacroPad page to the left.  The "Application" button will call up whichever application your current page is for.  For example, if your display says `Zoom` at the top, then pressing the "Application" button will bring the `Zoom` application to the forefront.

### Rotary Encoder

The rotary encoder in the upper right-hand corner is used primarily to adjust the volume.  Pressing the encoder dial "in" will take you back to the main/home screen of the MacroPad.

## :hammer_and_wrench: Support

Please [open an issue](https://github.com/javiergayala/RP2040-MacroPad/issues/new) for support.

## :memo: Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/javiergayala/RP2040-MacroPad/compare/).

## Credits

Credit goes to [Phillip Burgess](https://learn.adafruit.com/users/pburgess) who wrote the [original tutorial on Adafruit](https://learn.adafruit.com/macropad-hotkeys).

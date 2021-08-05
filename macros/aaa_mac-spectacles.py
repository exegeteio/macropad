# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Mac Spectacle',  # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Upper', [Keycode.COMMAND,
         Keycode.LEFT_CONTROL, Keycode.LEFT_ARROW]),
        (0x004000, 'Full', [Keycode.COMMAND, Keycode.OPTION, 'f']),
        (0x400000, 'Upper', [Keycode.COMMAND,
         Keycode.LEFT_CONTROL, Keycode.RIGHT_ARROW]),
        # 2nd row ----------
        (0x202000, 'Left', [Keycode.COMMAND,
         Keycode.OPTION, Keycode.LEFT_ARROW]),
        (0x202000, 'Center', [Keycode.COMMAND,
         Keycode.OPTION, 'c']),
        (0x400000, 'Right', [Keycode.COMMAND,
         Keycode.OPTION, Keycode.RIGHT_ARROW]),
        # 3rd row ----------
        (0x000040, 'Lower', [Keycode.COMMAND, Keycode.SHIFT,
         Keycode.LEFT_CONTROL, Keycode.LEFT_ARROW]),
        (0x000040, 'Screen', [
         Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, Keycode.RIGHT_ARROW]),
        (0x000040, 'Lower', [Keycode.COMMAND, Keycode.SHIFT,
         Keycode.LEFT_CONTROL, Keycode.RIGHT_ARROW]),
        # 4th row ----------
        (0x000000, 'Prev', [Keycode.OPTION,
                            Keycode.LEFT_CONTROL, Keycode.LEFT_ARROW]),
        (0x800000, '', []),   # Not sure what to do with this one???
        (0x101010, 'Next', [Keycode.OPTION,
         Keycode.LEFT_CONTROL, Keycode.RIGHT_ARROW]),
    ]
}

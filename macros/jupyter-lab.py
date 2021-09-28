# MACROPAD Hotkeys: VS Code

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name': 'Jupyter',       # Application name
    'macros': [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x010101, 'Undo', [Keycode.CONTROL, 'z']),
        (0x000000, '', ' '),
        (0x000000, '', ' '),
        # 2nd row ----------
        (0x2624a2, 'Above', 'a'),
        (0x2624a2, 'Below', 'b'),
        (0x000000, '', ' '),
        # 3rd row ----------
        (0x28a328, 'Run', [Keycode.COMMAND, Keycode.ENTER]),
        (0x32cb32, '+Ins', [Keycode.ALT, Keycode.ENTER]),
    ]
}

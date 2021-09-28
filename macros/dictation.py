# SPDX-FileCopyrightText: 2021, Ryan Pavlik <ryan.pavlik@gmail.com>
# SPDX-License-Identifier: CC0-1.0

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name': 'Dictation',       # Application name
    'macros': [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x87cefa, 'Copy', [Keycode.CONTROL, "c"]),
        (0xfa8072, 'Excuse', "Please excuse any typos and strange capitalization. I am using some simple dictation at the moment due to a broken wrist."),
        (0x87cefa, 'Paste', [Keycode.CONTROL, "v"]),
        # 2nd row ----------
        (0x000000, '', []),
        (0x800080, 'VD Up', [Keycode.CONTROL, Keycode.ALT, Keycode.UP_ARROW]),
        (0x000000, '', []),
        # 3rd row ---------- 
        (0x4b0082, 'Save', [Keycode.CONTROL, "s"]),
        (0x800080, 'VD Down', [Keycode.CONTROL, Keycode.ALT, Keycode.DOWN_ARROW]),
        (0x000000, '', []),
        # 4th row ----------
        (0x009100, 'Start', [Keycode.F16]),
        (0xffd700, 'Cancel', [Keycode.F15]),
        (0xff0000, 'Stop', [Keycode.F14]),
    ]
}

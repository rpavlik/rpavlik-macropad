# SPDX-FileCopyrightText: 2021, Ryan Pavlik <ryan.pavlik@gmail.com>
# SPDX-License-Identifier: CC0-1.0

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name': 'VS Code (CMake)',       # Application name
    'macros': [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xff8c00, 'Cmds', [Keycode.CONTROL, "P"]),
        (0x000055, 'Format', [Keycode.CONTROL, 'I']),
        (0x000000, '', []),
        # 2nd row ---------- Peek
        (0x005b63, 'AllRefs', [Keycode.ALT, Keycode.SHIFT, Keycode.F12]),
        (0x005b63, '◉PkDef', [Keycode.ALT, Keycode.F12]),
        (0x005b63, '◉Decl', [Keycode.ALT, Keycode.SHIFT, Keycode.F11]), # this needs a custom keyboard shortcut added for "Peek Declaration"
        # 3rd row ---------- Go To
        (0x005b63, '»Ref', [Keycode.SHIFT, Keycode.F12]),
        (0x005b63, '»Def', [Keycode.F12]),
        (0x005b63, '»Decl', [Keycode.CONTROL, Keycode.SHIFT, Keycode.F11]), # this needs a custom keyboard shortcut added for "Go to Declaration"
        # 4th row ----------
        (0xc27e00, 'Build', [Keycode.F7]),
        (0x000000, '', ''),
        (0x009100, 'Debug', [Keycode.CONTROL, Keycode.F5]),
    ]
}

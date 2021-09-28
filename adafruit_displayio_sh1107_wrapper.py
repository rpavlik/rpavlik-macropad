# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 Mark Roberts for Adafruit Industries
# SPDX-FileCopyrightText: 2021 James Carr
# SPDX-FileCopyrightText: 2021 Ryan Pavlik
#
# SPDX-License-Identifier: MIT
"""
`adafruit_displayio_sh1107_wrapper`
================================================================================

Add features to a built-in DisplayIO driver for SH1107 monochrome displays.

Based on the `adafruit_displayio_sh1107` library with all the stuff built-in to
board libraries removed.


* Author(s): Scott Shawcroft, Mark Roberts (mdroberts1243), James Carr, Ryan Pavlik

Implementation Notes
--------------------

**Hardware:**

* `Adafruit MacroPad RP2040`_

**Software and Dependencies:**

* Adafruit CircuitPython (version 7+) firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

class SH1107_Wrapper:
    """
    Wrapper for built-in DisplayIO SSD1107 driver
    """

    def __init__(
        self,
        display
    ):
        self.display = display
        self.bus = display.bus
        self._is_awake = True  # Display starts in active state (_INIT_SEQUENCE)

    @property
    def is_awake(self):
        """
        The power state of the display. (read-only)

        True if the display is active, False if in sleep mode.
        """
        return self._is_awake

    def sleep(self):
        """
        Put display into sleep mode

        The display uses < 5uA in sleep mode
        Sleep mode does the following:
        1) Stops the oscillator and DC-DC circuits
        2) Stops the OLED drive
        3) Remembers display data and operation mode active prior to sleeping
        4) The MP can access (update) the built-in display RAM
        """
        if self._is_awake:
            self.bus.send(int(0xAE), "")  # 0xAE = display off, sleep mode
            self._is_awake = False

    def wake(self):
        """
        Wake display from sleep mode
        """
        if not self._is_awake:
            self.bus.send(int(0xAF), "")  # 0xAF = display on
            self._is_awake = True

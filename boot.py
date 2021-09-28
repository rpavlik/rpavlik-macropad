import storage, usb_cdc
import board, digitalio
print("Press and hold top left key to update")
button = digitalio.DigitalInOut(board.KEY1)
button.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
if button.value:
	storage.disable_usb_drive()
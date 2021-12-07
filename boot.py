import storage, usb_cdc, usb_midi
import board, digitalio
print("Top-Left for")
print("Drive Access")
button = digitalio.DigitalInOut(board.KEY1)
button.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
if button.value:
	print("DRIVE INACTIVE")
	storage.disable_usb_drive()
	usb_cdc.disable()
	# usb_midi.disable()
else:
	print("DRIVE ACTIVE")
	print("release now")
	while not button.value:
		pass

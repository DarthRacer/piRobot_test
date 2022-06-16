import evdev
gamepad = evdev.InputDevice('/dev/input/event0')
print (gamepad)
for event in gamepad.read_loop():
	if event.type == evdev.ecodes.EV_KEY:
		keyevent = (evdev.categorize(event))
		if keyevent.keystate == keyevent.key_down:
			if keyevent.keycode == 'BTN_BASE':
				print ("Back")
			elif keyevent.keycode == 'BTN_TOP2':
				print ("Forward")
			elif keyevent.keycode == 'BTN_BASE4':
				print ("Right")
			elif keyevent.keycode == 'BTN_BASE3':
				print ("Left")
			elif keyevent.keycode == 'BTN_TOP':
				print ("Exiting Script")
				break
		if keyevent.keystate == keyevent.key_up:
			print ("STOPPED")

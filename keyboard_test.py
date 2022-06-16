#import curses module for keyboard input
import curses

# Get curses window, turn off echoing to screen
#turn on instant no wat response,
#and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
	while True:
		char = screen.getch()
		if char == ord('q'):
			break
		elif char == curses.KEY_LEFT:
			print ("left")
		elif char == curses.KEY_RIGHT:
			print ("right")
finally:
	#Close down curses properly, including 
	#turning echo back on
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()

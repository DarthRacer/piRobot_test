
import pygame

pygame.joystick.init()

"""
Just a check to ensure a joystick is plugged in.
Only going to retrieve data for the 0th joystick anyways...
"""
num_joysticks = pygame.joystick.get_count()
if num_joysticks == 0:
    raise ValueError("No joysticks attached!")

joystick = pygame.joystick.Joystick(0)
joystick.init()

#Just some info about the controller
j_id = joystick.get_id()
j_name = joystick.get_name()
num_axes = joystick.get_numaxes()
num_balls = joystick.get_numballs()
num_buttons = joystick.get_numbuttons()
num_hats = joystick.get_numhats()
print(j_id, j_name)
print(num_axes, num_balls, num_buttons, num_hats)

#Define the inner and outer radii that are considered 0 and 100% movement
dead_zone = 0.2#inner radius
edge_zone = 0.9#outer radius

while True:
    for event in pygame.event.get():
        pass

    """
    Only have an xbox 360 controller to work with
    There, axes 0 and 1 correspond the left stick x and y
    And axes 3 and 4 correspond to the right stick x and y
    Not sure what axes 2 and 5 are listed for...
    For me, the ranges only go from [-1.0, 1.0), so 1.0 is not included for right and bottom.
    """
    left_x = joystick.get_axis(0)
    print (round(left_x * 100))
    left_y = joystick.get_axis(1)
    print (round(left_y * 100))
    right_x = joystick.get_axis(2)
    print (round(right_x * 100))
    right_y = joystick.get_axis(3)
    print (round(right_y * 100))


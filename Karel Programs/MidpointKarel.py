from karel.stanfordkarel import *

"""
File: MidpointKarel.py
--------------------
This program makes Karel find the midpoint of any
sized world, and place a beeper there. If there world 
is even then they place a beeper on the left side, this 
is why most intuative solutions don't work or are much
more complex.
"""

def main():
    """
    This took wayyyy to long to figure out, but the program uses a 
    zig zag pattern to get to the middle at the top of the world.
    Once karel gets to the top they move to the floor and place
    a beeper at the midpoint.
    """
    turn_left()
    go_to_middle_at_the_top()
    go_to_row1()
    put_beeper()

def go_to_middle_at_the_top():
    """
    Uses a zig zag patter that will always end at the middle
    or the leftmost square if even.
    """
    while front_is_clear():
        move()

        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()

def go_to_row1():
    """ Moves karel to the bottom of the world """
    turn_around()
    while front_is_clear():
        move()

    turn_left()

def turn_right():
    """ turns karel to the right """
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    """ turns karel 180 degrees """
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
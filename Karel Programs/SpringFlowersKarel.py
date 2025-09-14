"""
SpringFlowersKarel.py
---------------------
This program has karel go up "stems", and create a flower at the
top of each "stem". They always ends at the end of the world, and 
they can make flowers in any dimension world.
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
    Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
    """
    
    move_till_wall()
    make_flower()
    move_till_wall()
    make_flower()
    move_till_wall()

def move_till_wall():
    """
    moves karel till stem or wall is hit
    """
    while front_is_clear():
        move()

def make_flower():
    """
    makes the flower bloom, then goes to ground and faces east
    """
    up_stem()
    bloom()
    down_stem()

def up_stem():
    """ goes up the stem """
    turn_left()
    while right_is_blocked():
        move()

def bloom():
    """
    makes the flower bloom
    pre: facing north
    post: facing east
    """
    for i in range(3):
        put_beeper()
        move()
        turn_right()
    # fence post problem
    put_beeper()

def down_stem():
    """
    moves karel down the stem
    pre: facing west
    post: facing east
    """
    turn_left()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    """ Turns Karel right """
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
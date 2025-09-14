"""
ZebraCrossingKarel.py
---------------------
This program has Karel drop 2 columns of beepers, then creates a 
space for the next column of beepers. The output is a zebra crossing.
Written to work in any dimension world.
"""

from karel.stanfordkarel import *

def main():
    """
    Has Karel create the first stripe, then if there is space to add
    another stripe, she creates one.
    """
    do_zebra()
    while front_is_clear():
        create_zebra_gap() 
        do_zebra()

def do_zebra():
    """
    Does the entire zebra stripe
    """
    up_zebra()
    top_of_zebra()
    down_zebra()

def up_zebra():
    """
    Goes up the left column of the stripe while putting beepers
    """
    turn_left()
    while front_is_clear():
        put_beeper()
        move()

def top_of_zebra():
    """
    Finishes the top left column and sets up down_zebra()
    """
    turn_right()
    put_beeper()
    move()

def down_zebra():
    """
    moves karel down the right column of the stripe while putting beepers
    """
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    # fence post problem
    put_beeper()
    turn_left()

def create_zebra_gap():
    # makes the 3 space gap inbetween crossing
    for i in range(4): # move 4 because do_zebra assumes karel is on first beeper place
        move()

def turn_right():
    # turns karel right
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
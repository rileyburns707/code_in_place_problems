"""
LabyrinthKarel.py
-----------------
This program makes Karel solve a maze. There were 2 worlds
in the test case, so the code must be written to solve any
maze that Karel could interact with.
"""

from karel.stanfordkarel import *

def main():
    """
    Checks to see if there is a place for Karel to move, and moves there.
    """
    
    while front_is_clear() or left_is_clear() or right_is_clear():
        move_to_wall()
        find_direction()

def move_to_wall():
    """
    Moves Karel to the nearest wall
    """
    while front_is_clear():
        move()

def find_direction():
    """
    Checks to see if there is a direction without a wall,
    and turns Karel in the open direction. Written to ensure
    she won't go back the same way she came.
    """
    if left_is_clear():
        turn_left()
    if right_is_clear():   # right is clear
        turn_right()

def turn_right():
    """
    Makes Karel turn right
    """
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
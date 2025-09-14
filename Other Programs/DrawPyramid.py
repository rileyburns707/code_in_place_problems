from graphics import Canvas
import random

"""
DrawPyramid.py
--------------
This program makes a pyramid. You can change the global variables and it 
will still create a pyramid based on the new numbers.
"""

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH = 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    """
    This function creates the bottom row of the pyramid then adds
    the rest of the rows after
    """
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # milestone 1: create a brick - DONE
    # milestone 2: make the base row of bricks - DONE
    base_row(canvas)

    # milestone 3: make the pyrmaid
    create_rest_of_rows(canvas)

def create_brick(canvas, left_x, left_y):
    """ places a single brick """
    canvas.create_rectangle(
        left_x, left_y, 
        left_x + BRICK_WIDTH, left_y + BRICK_HEIGHT, 
        "yellow", "black"
    )

def base_row(canvas):
    """ places the bottom row of the pyramid """
    for i in range(BRICKS_IN_BASE):
        create_brick(canvas, i*BRICK_WIDTH, CANVAS_HEIGHT - BRICK_HEIGHT)

def create_rest_of_rows(canvas):
    """
    Places the rest of the rows in the pyramid by looping through the remaining rows.
    This starts at the second row and ends at the top.
    """
    
    tower_height = 1     # set to 1 but really starts at row 2
    bricks_left = BRICKS_IN_BASE - 1    # number of bricks to place in that row
    while tower_height < BRICKS_IN_BASE:
        starting_x = tower_height * (BRICK_WIDTH / 2)   # starting x for each row
        left_y = CANVAS_HEIGHT - (tower_height + 1) * BRICK_HEIGHT    # y-coordinate for the entire row

        for i in range(bricks_left):
            left_x = starting_x + i * BRICK_WIDTH
            create_brick(canvas, left_x, left_y)
    
        tower_height += 1
        bricks_left -= 1


if __name__ == '__main__':
    main()

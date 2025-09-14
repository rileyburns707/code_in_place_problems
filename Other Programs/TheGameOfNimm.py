"""
TheGameOfNimm.py
----------------
This program allows the users to play a classic game of Nimm.
2 players remove stones until there are 0 stones left, but they can 
only remove 1 or 2 stones at a time.
"""
STONE_COUNT = 20    # starts with a pile of 20 stones
ACTIVE_PLAYER = 1

def main():
    """ Calls the playe game functions """
    play_game(ACTIVE_PLAYER, STONE_COUNT)
    

def play_game(ACTIVE_PLAYER, STONE_COUNT):
    """ 
    Has the 2 players alternate removing stones, while checking if they
    entered a valid number.
    """
    while STONE_COUNT > 0:
        print(f"There are {STONE_COUNT} stones left.")

        # On a given turn, a player may take either 1 or 2 stones from the center pile
        num_to_remove = int(input(f"Player {ACTIVE_PLAYER} would you like to remove 1 or 2 stones? "))
        STONE_COUNT =  check_if_valid(num_to_remove, STONE_COUNT)

        if ACTIVE_PLAYER == 1:
            ACTIVE_PLAYER = 2
        else:
            ACTIVE_PLAYER = 1

        print("")

    print(f"Player {ACTIVE_PLAYER} wins!")

def check_if_valid(num_to_remove, STONE_COUNT):
    """ Checks if the number entered is a 1 or a 2, and updates the stone count """
    if num_to_remove == 1:
            STONE_COUNT -= 1
    elif num_to_remove == 2:
        STONE_COUNT -= 2
    else:
        num_to_remove = int(input("Please enter 1 or 2: "))
        if num_to_remove == 1:
            STONE_COUNT -= 1
        elif num_to_remove == 2:
            STONE_COUNT -= 2

    return STONE_COUNT

if __name__ == '__main__':
    main()
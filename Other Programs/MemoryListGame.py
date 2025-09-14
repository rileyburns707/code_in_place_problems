import random

"""
MemoryListGame.py
-----------------
This program is a memory game where the player
cannot reveal the hidden numbers until they have
guessed a matching pair.
"""

NUM_PAIRS = 3

def main():
    """
    Main function creates a answer list called "truth_list", and shuffles it.
    It then creates the list displayed to the player than hides the numbers.
    The user is prompted to guess indices that have the same number hidden until
    all the numbers are shown to have a match. 
    """
    truth_list = create_truth_list()                            # milestone 1
    shuffled_truth_list = shuffle_truth_list(truth_list)        # milestone 2
    display_list = create_display_list()                        # milestone 3
    # get_valid_index(display_list)                             # milestone 4
    check_for_match(display_list, shuffled_truth_list)          # milestone 5 & 6


def create_truth_list():
    """ Creates a truth list that has the values  0  through  N_PAIRS - 1  twice. """
    truth_list = []
    for i in range(NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)

    return truth_list

def shuffle_truth_list(truth_list):
    """ shuffles the truth list """
    random.shuffle(truth_list)
    return truth_list

def create_display_list():
    """ creates a new list the same size as the truth list. Has '*' displayed at each spot """
    display_list = []
    for i in range(NUM_PAIRS * 2):
        display_list.append('*')

    return display_list

def get_valid_index(display_list):
    """ checks if the user has guess a valid index """
    while True:
        index_guessed = int(input("Enter an index: "))

        if 0 <= index_guessed <= (len(display_list) - 1) and display_list[index_guessed] == '*':
            return index_guessed

def check_for_match(display_list, shuffled_truth_list):
    """
    Repeatedly shows the display list and asks the user to guess 2 indices.
    If both the indices guessed have the same value in truth list then it
    is a match and the display list is updated. If it is not a match the terminal
    says the value at each index of the truth list. Once all matches are found
    the game ends.
    """
    while '*' in display_list:
        print(display_list)
        guess1 = get_valid_index(display_list)
        guess2 = get_valid_index(display_list)
        if shuffled_truth_list[guess1] == shuffled_truth_list[guess2]:
            print("Match!")
            display_list[guess1] = shuffled_truth_list[guess1]
            display_list[guess2] = shuffled_truth_list[guess2]
            clear_terminal()
        else:
            print(f"Value at index {guess1} is {shuffled_truth_list[guess1]}")
            print(f"Value at index {guess2} is {shuffled_truth_list[guess2]}")
            clear_terminal()
    
    print(display_list)
    return print('Congratulations! You won!')

def clear_terminal():
    """ clears the terminal so the player cannot see previous guesses """
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
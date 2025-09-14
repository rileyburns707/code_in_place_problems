"""
BabyVocab.py
------------
This program creates a histogram of all the words
in the words.txt file.
"""

def main():
    """ 
    Makes a list of the words, then creates a 
    dictionary to track the count of each word.
    Then makes a histogram of the quantity of each
    word.
    """
    words = load_words_from_file("Other Programs/words.txt")
    word_count_dict = create_dict(words)
    create_histogram(word_count_dict)

def create_dict(words):
    """
    create a dictionary of the count of each word by
    iterating through the words and increase value count if word 
    is already in the dictionary.
    """
    word_count_dict = {}
    for word in words:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] += 1

    return word_count_dict

def create_histogram(word_count_dict):
    """
    Iterate through each pair in the word_count_dict.
    Print each row using print_histogram_bar(key, value)
    """
    for key, value in word_count_dict.items():
        print_histogram_bar(key, value)

def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words

if __name__ == '__main__':
    main()

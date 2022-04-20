import random


def get_word():
    """
    Returns a randmo five-letter word from the dictionary file
    """
    # open word list
    with open("dictionary.txt", "r") as word_file:
        words = word_file.read().splitlines()
    # choose random word
    while True:
        word = random.choice(words)
        if len(word) == 5:
            return word.upper()

        
def word_to_list(word):
    """
    Accepts a words and returns it as a list 
    """
    temp = []
    for letter in word:
        temp.append(letter)
    return temp


def get_guess():
    """
    Returns a five letter word
    """
    while True:
        guess = input("> ").upper()
        if len(guess) == 5:
            return guess
   

# ----- MAIN PROGRAM ----- #

# --- Game Variables --- #
word = word_to_list(get_word())
guesses = []
running = True

# --- Main Loop --- #
while running:
    guess = word_to_list(get_guess())
    
    # check for correct guess 
    if guess == word:
        print("\nWINNER!")
        running = False
    else:
        # identify correct letters, misplaced letters and incorrect letters
        temp = []
        for index in range(5):
            if guess[index] == word[index]:
                temp.append("O")
            elif guess[index] in word:
                temp.append("?")
            else:
                temp.append("X")
        guesses.append(temp)
        
        # print guesses
        for line in guesses:
            print("".join(line))
            print("")
            
        # check for loss
        if len(guesses) == 6:
            print("Bad Luck")
            running = False
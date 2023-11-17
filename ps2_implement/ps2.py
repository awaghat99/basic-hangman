import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word_with_guessed_letters = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_with_guessed_letters += letter
            word_with_guessed_letters += " "
        else:
            word_with_guessed_letters += "_ "
    return word_with_guessed_letters
    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters_guessed:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")
    return alphabet
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    game_is_on = True
    word_length = len(secret_word)
    guesses_left = 6
    letters_guessed = []
    print("Welcome to the Hangman Game")
    print("I am thinking of a word that is", word_length, "letters long")
    print(get_guessed_word(secret_word, letters_guessed))
    
    while game_is_on:
        print("\n ---------- \n")
        print("You have", guesses_left, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter: ")
        letters_guessed.append(guessed_letter)
        
        if guessed_letter in secret_word: 
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
            
        if guesses_left == 0:
            print("You lose!")
            print("The word was:", secret_word)
            game_is_on = False
        elif is_word_guessed(secret_word, letters_guessed):
            print("You win!")
            game_is_on = False



if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

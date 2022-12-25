# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
#global variables
letters_guessed = []


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    for letter in secret_word:
        if letter not in letters_guessed:
            #print("False!")
            return False
    #print("Word is Guessed!")
    return True 




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    display_word = ""
    for elem in secret_word:
        if elem in letters_guessed:
            display_word = display_word + elem
        if elem not in letters_guessed:
            display_word = display_word + '_ '
    return display_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_letters = ""
    for elem in alphabet:
        if elem not in letters_guessed:
            available_letters = available_letters + elem
    return available_letters
      
def how_many_guesses(num_guesses):
    if num_guesses > 1:
       num_guesses = num_guesses - 1
    else: 
       print("Sorry, you ran out of guesses. The word was", secret_word)
    #start with 6, remove 1 for every guess not in secret_word
    return num_guesses
    
def is_input_valid(user_input):
    if user_input.isalpha():
        return True
            
def total_score(num_guesses, secret_word):
    #Total score = guesses_remaining* number unique letters in secret_word
    unique_letters = set(secret_word)
    num_unique_letters = len(unique_letters)
    return (num_guesses * num_unique_letters)

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    num_guesses = 6
    num_warnings = 3

    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), " letters long.")
    #function get_guessed_word  -------------
    get_guessed_word(secret_word, letters_guessed)
    #Interactive time
    
    while (is_word_guessed(secret_word, letters_guessed) == False):
        print("You have ", num_guesses, " guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        user_input = input("Please guess a letter: ")
        if is_input_valid(user_input): #Check input for validity
        #if user_iput is in secret_word add user_input to letters_guessed 
        #& print"Good guess: get_guessed_word
            letters_guessed.append(user_input.lower())
            if(user_input.lower() in secret_word):
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word", get_guessed_word(secret_word, letters_guessed))
                num_guesses = num_guesses -1
                if(num_guesses == 0):
                    print("Sorry, you ran out of guesses. The word was", secret_word)
                    break
        else:
            if(num_warnings > 1):
                num_warnings = num_warnings - 1
                if(num_guesses == 0):
                    print("Sorry, you ran out of guesses. The word was", secret_word)
                    break
            else:
                num_guesses = num_guesses - 1
                num_warnings = 3
                if(num_guesses == 0):
                    print("Sorry, you ran out of guesses. The word was", secret_word)
                    break
            print("Oops! That is not a valid letter. You have ", num_warnings, "warnings left:")
    if (is_word_guessed(secret_word, letters_guessed) == True):
        print("Congratulations, you won!")
        print("Your total score for this game is: ", total_score(num_guesses, secret_word))
        
    pass
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #find all words of same length in wordlist
        #use strip() to get rid of spaces
    my_word_small = my_word.replace(" ", "")
    if len(other_word) == len(my_word_small):
        for x in range(len(my_word_small)):
            #print("x: ", x)
            if my_word_small[x] == "_":
                #print("if: ", my_word_small[x])
                x = x+1
            elif my_word_small[x] == other_word[x]:
                #print("elif 1: ", my_word_small[x])
                x = x+1
            elif my_word_small[x] != other_word[x]:
                #print("elif2: ", my_word_small[x])
                return False
        return True
            
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    if len(possible_matches) == 0: 
        print("No matches found")
    else: 
        print(possible_matches)
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guesses = 6
    num_warnings = 3

    
    print("Welcome to the game Hangman - with hints!")
    print("I am thinking of a word that is", len(secret_word), " letters long.")
    #function get_guessed_word  -------------
    get_guessed_word(secret_word, letters_guessed)
    #Interactive time
    
    while (is_word_guessed(secret_word, letters_guessed) == False):
        print("You have ", num_guesses, " guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        user_input = input("Please guess a letter: ")
        if user_input == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        if is_input_valid(user_input): #Check input for validity
        #if user_iput is in secret_word add user_input to letters_guessed 
        #& print"Good guess: get_guessed_word
            letters_guessed.append(user_input.lower())
            if(user_input.lower() in secret_word):
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word", get_guessed_word(secret_word, letters_guessed))
                num_guesses = num_guesses -1
                if(num_guesses == 0):
                    print("Sorry, you ran out of guesses. The word was", secret_word)
                    break
        elif user_input != "*":
            if(num_warnings > 1):
                num_warnings = num_warnings - 1
                if(num_guesses == 0):
                    print("Sorry, you ran out of guesses. The word was", secret_word)
                    break
            else:
                num_guesses = num_guesses - 1
                num_warnings = 3
                if(num_guesses == 0):
                    print("Sorry, you ran out of guesses. The word was", secret_word)
                    break
            print("Oops! That is not a valid letter. You have ", num_warnings, "warnings left:")
    if (is_word_guessed(secret_word, letters_guessed) == True):
        print("Congratulations, you won!")
        print("Your total score for this game is: ", total_score(num_guesses, secret_word))
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    


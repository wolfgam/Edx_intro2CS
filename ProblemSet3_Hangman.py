# Radiactive Decay
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    block = int((stop-start)/step)
    area = 0
    for i in range(0,block):
         area=area+f(start+i*step)*step
    return (area)



# Hangman Game

import random
import string

WORDLIST_FILENAME = "C:/Users/fduan/Documents/Python_training/Edx_python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    Guess = ''
    for char in lettersGuessed:
        Guess+=char
    
    flag = len(Guess)!=0
    for i in range(0,len(secretWord)):
        charInS = secretWord[i] in Guess
        flag = flag and charInS
    return flag



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ans=''
    Guess = ''
    for char in lettersGuessed:
        Guess+=char
    
    for i in range(0,len(secretWord)):
        if secretWord[i] in Guess:
            ans=ans+secretWord[i]
        else:
            ans=ans+'_ '
    return ans


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alpha = string.ascii_lowercase
    for char in lettersGuessed:
        alpha = alpha.replace(char,'')
    return alpha
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '-------------'
    lettersGuessed = []
    GuessCount = 8

    while GuessCount > 0:
        print 'You have ' + str(GuessCount) + ' guesses left'
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
       
        if guess in lettersGuessed:
            str_output = 'Oops! You\'ve already guessed that letter: '
        elif guess in secretWord:
            lettersGuessed.append(guess)
            str_output = 'Good guess: '
        else:
            GuessCount -=1
            lettersGuessed.append(guess)
            str_output = 'Oops! That letter is not in my word: '
        print str_output+getGuessedWord(secretWord, lettersGuessed)
        print '-------------'
            
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations you won'
            break
        if GuessCount == 0:
            print 'Sorry you ran out of guesses. The word was :' + secretWord
            break

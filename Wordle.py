import os
import random
from termcolor import colored

os.chdir('/Users/dchavre/Documents/VS Code/Projects/Wordle') # Changing the directory to allow for the larger random wordlist

WORDLIST_FILENAME = "wordlist.txt"

# Giving values to some variables:
guess_output = ''
x = ''
green = []
yellow = []

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def word_selection(wordlist):
    l = []
    for i in wordlist:
        if len(i) == 5:
            l.append(i)
    return random.choice(l)

def input_word(): # Using recursion to take a guess
    guess = input('Guess: ')
    if len(guess) == 5:
        if guess not in l:
            print('Please make sure your word is a real word, try again.')
            return input_word()
        else:
            return guess.lower()
    else:
        print('Please make sure your word is five letters long, try again.')
        return input_word()

def letter_analyzation(guess, word, x, yellow, green):
    green.clear()
    yellow.clear()
    guess_output = ''
    not_found = str(word) # Copying variable word
    for i in range(0, 5, 1): # Making a loop to shorten code
        # Subtracting individual letters from it every time there's a matching letter:
        if guess[i] in word:
            if guess[i] == word[i]:
                x = colored(str(guess[i]), 'green')
                not_found = not_found.replace(str(guess[i]), '', 1)
            else:
                if guess[i] in not_found:
                    x = colored(str(guess[i]), 'yellow')
                    not_found = not_found.replace(str(guess[i]), '', 1)
                else:
                    x = colored(str(guess[i]), 'grey')
        else:
            x = colored(str(guess[i]), 'grey')
        guess_output += x
    return guess_output

def check_win(guess, word): # Checks for a win by looking if the guess is the same as the word
    if guess == word:
        win = True
        return win
    else:
        win = False
        return win

def Wordle(word):
    # Making global variables to avoid any errors:
    global guess_output
    global green
    global yellow

    # Defining some variables to allow the 
    win = False
    counter = 0

    while counter <= 5 and win == False: # A while loop to run as long as the player has more moves or if they haven't won yet.
        counter += 1 # Counts to make the while loop better

        guess = input_word() # Takes an input

        # Coloring the letters:
        guess_output = letter_analyzation(guess, word, x, green, yellow)
        print(guess_output)

        win = check_win(guess, word) # Checks if a win is present.

        # Win case:
        if win == True:
            print('Congrats, you have won in', str(counter), 'moves!')
    
    # Losing case:
    if counter >= 6 and win == False:
        print('You have lost, the word was' , str(word) + '.')

l = load_words()
word = word_selection(l)
Wordle(word)

# Reset case:
reset = input('Would you like to try again? y/n: ')
if reset == 'y':
    l = load_words()
    word = word_selection(l)
    Wordle(word)

os.chdir('/Users/dchavre/Documents/VS Code') # Changing the directory to allow for normal use afterwards
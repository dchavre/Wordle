import os
import random
from termcolor import colored

original_directory = os.getcwd() # Saving the original directory to switch back to afterwards.

directory = input('Please paste your directory into the program: ') # Changing the directory to allow for the larger random wordlist
os.chdir(directory)

WORDLIST_FILENAME = "wordlist.txt"

# Giving values to some variables:
guess_output = ''
x = ''
op = ''
green = ['', '', '', '', '']
yellow = ['', '','', '', '']
grey = ['', '', '', '', '']

def load_words():
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
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

def letter_analyzation(guess, word, x, green, yellow, grey, guess_output, op):
    guess_output = ''
    green = ['', '', '', '', '']
    yellow = ['', '','', '', '']
    grey = ['', '', '', '', '']

    not_found = str(word) # Copying variable word
    # Loop for green letters:
    for i in range(0, 5, 1):
        if guess[i] in word:
            if guess[i] == word[i]:
                x = colored(str(guess[i]), 'green')
                not_found = not_found.replace(str(guess[i]), '', 1)
                op += x
                green[i] = op
                op = ''
                         
    # Loop for yellow letters:
    for j in range(0, 5, 1):
        if guess[j] in not_found and guess[j] != word[j]:
            x = colored(str(guess[j]), 'yellow')
            not_found = not_found.replace(str(guess[j]), '', 1)
            op += x
            yellow[j] = op
            op = ''
            
    # Loop for grey letters:
    for k in range(0, 5, 1):
        if guess[k] not in not_found:
            x = colored(str(guess[k]), 'grey')
            op += x
            grey[k] = op
            op = ''
            
    # Arranging guess_output using lists green yellow and grey:
    for l in range(0, 5, 1):
        if "" != green[l]:
            guess_output += green[l]
        elif "" != yellow[l]:
            guess_output += yellow[l]
        elif "" != grey[l]:
            guess_output += grey[l]
    
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
    global grey

    # Defining some variables to allow the 
    win = False
    counter = 0

    while counter <= 5 and win == False: # A while loop to run as long as the player has more moves or if they haven't won yet.
        counter += 1 # Counts to make the while loop better

        guess = input_word() # Takes an input

        # Coloring the letters:
        guess_output = letter_analyzation(guess, word, x, green, yellow, grey, guess_output, op)
        print(guess_output)

        win = check_win(guess, word) # Checks if a win is present.

        # Win case:
        if win == True:
            print('Congrats, you have won in', colored(str(counter), "blue"), 'moves!')
    
    # Losing case:
    if counter >= 6 and win == False:
        print('You have lost, the word was' , colored(str(word), "red") + '.')

l = load_words()
word = word_selection(l)
Wordle(word)

# Reset case:
reset = input('Would you like to try again? y/n: ')
if reset == 'y':
    l = load_words()
    word = word_selection(l)
    Wordle(word)

os.chdir(original_directory) # Changing the directory to allow for normal use afterwards
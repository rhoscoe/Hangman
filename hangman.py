# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:20:09 2018

@author: rosie
"""

import random

def get_word():
    with open('sowpods.txt', 'r') as f:
        text = list(f)
        word =  random.choice(text).strip()
        return word

HANGMAN = (
    """
    x-------x
    """,
    """
    x-------x
    |
    |
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    GAME OVER
    """
)


if __name__ == '__main__':
    goes = len(HANGMAN) - 1
    word = get_word()
    display = ["_ "]*len(word)
    guessed_letters = set()
    draw = 0
    #print word - for checking purposes
    while draw < goes:
        print display
        user_g = raw_input("Letter: ")
        
        if user_g in guessed_letters: #this part alerts the player that they've already made this guess
                print("Already guessed!!")
                user_g = raw_input("Guess a letter: ")
        elif user_g.upper() in word:
                guessed_letters.add(user_g) #adds letters to guessed letters, lets the player try again
                for i, letter in enumerate(word): #gets the index you need for the letter that matches the guess
                    if user_g.upper() == letter:
                        display[i] = user_g.upper() #puts the letter in the right place on the _ display
                if "_ " not in display:
                    print "You win!"
                    break
        else:
            guessed_letters.add(user_g) #adds letters to guessed letters, lets the player try again
            print "Not in the word. You have "+str(goes)+" goes. Try again!"
            draw +=1 #index for correct hangman image, which in turn gives them one less go
            print HANGMAN[draw]

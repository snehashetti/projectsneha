# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:54:17 2022

@author: Sneha
"""

dict1 = {'name': 'Sneha',
         'Company':'CTS',
         'Dept': 'EAS SAP',
         'desg': {'y1':'PAT', 'y2':'PA'},
         'SAL': 28000}

dict1['Company']
dict1.keys()
dict1.values()

for values in dict1:
    print(values)
    
dict1['SAL']=30000

dict1.clear()
dir(dict)

del dict1['SAL']

#Hangman letter

dir(random)

import random
fruits = ['mango', 'banana', 'apple', 'grapes', 'chikoo']
secret = random.choice(fruits)
print('Welcome to Hangman Letter Game')
guess_word=[]
secret_len = len(secret)
alpha = 'abcdefghijklmnopqrstuvwxyz'
letter_store = []

for letter in secret:
    guess_word.append("-")
    print('The secret word you have to guess has', secret_len, 'letters')
    
chances = 1
while chances < 10:
    guess = input('Guess your Letter: ').lower()
    if guess not in alpha:
        print('Enter a letter from a-z')
    else:
        letter_store.append(guess)
        if guess in secret:
            print("your guess is correct")
            for x in range(0, secret_len):
                if secret[x]==guess:
                    guess_word(x) = guess
                    print(guess_word)
            if "-" not in guess:
                print("You win!!")
                break
            else:
                print("The letter is not in the word. Try Again!")
                chances += 1
                if chances == 10:
                   print(" Sorry Mate, You lost :<! The secret word was",secret)
print("Game Over!!")
                
                    
    
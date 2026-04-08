import random 
from collections import Counter

somewords = 'rose tulip orchids sunflower lily carnation peony hibiscus daisy snapdragon jasmine sweetpea'
somewords = somewords.split(' ')

word = random.choice(somewords)

if __name__ == '__main__':
    print('-----HangMan Game-----')
    print('Guess the word! (Hint: the word is a flower.)')
    
    for _ in word:
        print('_', end=' ')
    print()
    
    letterGuessed=''
    chances = len(word)
    flag=0
    
    while chances > 0 and flag== 0:
        print()
        guess = input('Enter a letter to guess:').lower()
        
        if not guess.isalpha():
            print('Enter only a letter!')
            continue
        elif len(guess) > 1:
            print('Enter only a single letter!')
            continue
        elif guess in letterGuessed:
            print('You already guessed that letter!')
            continue
        
        if guess in word:
            letterGuessed += guess * word.count(guess)
        else:
            chances -= 1
            
        for char in word:
            if char in letterGuessed:
                print(char, end=' ')
            else:
                print('_', end=' ')
                
        if Counter(letterGuessed) == Counter(word):
            print("\nCongratulations! You guessed the word:", word)
            flag = 1
            break

        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print('\nYou lost! The word was:', word)                   
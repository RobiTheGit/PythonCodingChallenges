#!/usr/bin/python3
def CharacterOccurences(string, char):
    x = 0
    for i in string:
        if i == char:
            x += 1
        else:
            pass
    print(f'Ocuurences of {char} in {string} =', x)
    
CharacterOccurences(input('Input a string: '),input('What letter would you like to find the ammount of: '))

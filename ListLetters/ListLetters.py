#!/usr/bin/python3
#Gets all unique letters, and puts them in alphabetical order
import re
def ListLetters(string):
    letters = []
    for i in string:
        if i not in letters:
            letters.append(i)
        else:
            pass
    letters.sort(key=str.lower)
    print(*letters, sep='')
ListLetters(str(input("String: ")))

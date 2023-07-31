#!/usr/bin/python3
def RemoveVowel(string):
    result = ''
    for i in string:
        if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            i = ''
        result += i
    print(result)
RemoveVowel(input('Input a string: '))

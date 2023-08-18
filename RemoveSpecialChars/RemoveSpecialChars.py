#!/usr/bin/python3
import re
def RemoveSpecialChars(string):
    str2 = re.sub(r'[^A-z 0-9]','',string)
    print(str2)
RemoveSpecialChars(input('String: '))

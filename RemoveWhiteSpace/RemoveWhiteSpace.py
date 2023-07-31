#!/usr/bin/python3
import re
def RemoveWhiteSpace(string):
    output = re.sub(rf'[ \t]','',string)
    print(output)
RemoveWhiteSpace(input('Input a string: '))

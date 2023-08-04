#!/usr/bin/python3
def AlphaStr(string):
    str2 = list(string)
    str2.sort(key=str.lower)
    print(*str2, sep='')
AlphaStr(str(input('String: ')))

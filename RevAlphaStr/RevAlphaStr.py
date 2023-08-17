#!/usr/bin/python3
def RevAlphaStr(string):
    str2 = list(string)
    str2.sort(key=str.lower)
    str2 = str2[::-1]
    print(*str2, sep='')
RevAlphaStr(str(input('String: ')))

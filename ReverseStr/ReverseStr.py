#!/usr/bin/python3
def ReverseStr(String):
    StringList = list(String)
    StringList = StringList[::-1]
    print(*StringList, sep='')

ReverseInt(str(input("Number or Text to reverse: ")))

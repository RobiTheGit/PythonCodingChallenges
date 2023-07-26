#!/usr/bin/python3
import re
def RemoveChar(string, character):
    print(string.replace(character, ""))

RemoveChar(str(input("Text: ")), str(input("Letter to remove: ")))

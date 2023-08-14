#!/usr/bin/python3
import re
def SpaceToChar(InputStr, Char):
	str2 = re.sub(" ", Char, InputStr)
	print(str2)
SpaceToChar(input('A string: '), input('Character to replace spaces with: '))

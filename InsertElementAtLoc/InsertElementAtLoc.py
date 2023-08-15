#!/usr/bin/python3
global listt
listt = [1,2,3,4,5,6,7,8,9,0]
def InsertElementAtLoc(element, location):
    try:
        listt.insert(location, element)
    except:
        pass
    print(listt)
InsertElementAtLoc(input('Element to put in the list: '), int(input('Where to put the element in (must not be over 10): ')))

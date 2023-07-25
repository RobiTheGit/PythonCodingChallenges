#!/usr/bin/python3
def EvenOrOdd(num):
    global result
    num = float(num)
    if num%2 != 0:
        result = 'odd'
    else:
        result = 'even'
    print(num, 'is', result)

EvenOrOdd(input("Number To Check If It Is Even Or Odd:\n> "))

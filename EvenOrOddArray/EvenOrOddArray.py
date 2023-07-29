#!/usr/bin/python3
array = [0,1,2,3,4,5,6]
def EvenOrOdd(num):
    global result
    num = float(num)
    if num%2 != 0:
        result = 'odd'
    else:
        result = 'even'
    print(num, 'is', result)

for x in array:
    EvenOrOdd(x)

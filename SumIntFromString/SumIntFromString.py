#!/usr/bin/python3
import re
def IntToString(String):
    sums = 0
    String = re.sub(r"[^0-9]", "", String)
    for i in String:
        try:
            i = int(i)
            sums += i
        except:
            pass
    print(sums)

IntToString(input('String: '))

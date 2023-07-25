#!/usr/bin/python3
def CelciusToFarenheit(temp):
    temp2 = float(temp)
    print(f'{temp}C is {(temp2*9/5)+32}F')

def FarenheitToCelcius(temp):
    temp2 = float(temp)
    print(f'{temp}F is {(temp2-32)*(5/9)}C')

Temperature = input("Temperature to Convert:\n> ")
Type = input("Convert to Celcius or Farenheit:\n> ")

if Type.upper().startswith("C"):
    FarenheitToCelcius(Temperature)

elif Type.upper().startswith("F"):
    CelciusToFarenheit(Temperature)

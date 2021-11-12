'''
@Author: Dayananda C
@Date: 2021-09-11 
@Time:  12:00:00
@Last Modified by: Dayananda C
@Title : Quadratic
'''

from math import sqrt
import math

def Quadratic() :
    try:
        a= float(input("Enter value of a : "))
        b= float(input("Enter value of b : "))
        c= float(input("Enter value of c : "))

        delta = b * b - 4 * a *c 
        sqrtOfDelta= math.sqrt(abs(delta))                  

        if delta > 0:  
            print("Roots are real and unequal")  
            print((-b + sqrtOfDelta) / (2 * a))  
            print((-b - sqrtOfDelta) / (2 * a)) 

        elif delta == 0:  
            print("Roots are real and equal")  
            print(-b / (2 * a))

        else:  
            print("Complex Roots")  
            print(- b / (2 * a), " + i", sqrtOfDelta)  
            print(- b / (2 * a), " - i", sqrtOfDelta)  

    except:
        print("Please enter a valid input")
        Quadratic()

Quadratic()
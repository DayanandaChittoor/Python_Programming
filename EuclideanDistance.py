'''
@Author: Dayananda C
@Date: 2021-09-11 
@Time:  12:00:00
@Last Modified by: Dayananda C
@Title : Euclidean distance
'''

def EuclideanDistance() :
    try:
        x = float(input("Enter value of x : "))
        y = float(input("Enter value of y : "))

        import math
        euclideanDistance =math.sqrt(x*x+y*y)
        print("Ecludean distance  = {} ".format(euclideanDistance))

    except ValueError:
        print("Please Enter a valid input ")
        EuclideanDistance()

print("Enter (x,y) point to find Euclidean distance \n")
EuclideanDistance()

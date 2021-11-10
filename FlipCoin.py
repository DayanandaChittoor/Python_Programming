'''
@Author: Dayananda C
@Date: 2021-08-11 10:30:00
@Last Modified by: Dayananda C
@Last Modified time: 2021-08-11 10:50:00
@Title : Flip Coin and print percentage of Heads and Tails
'''

import random

numberOfFlips = int(input("How many times you want to flip the coin : "))
i=0
numOfHeads =0
numOfTails =0

while (i<=numberOfFlips):
        i+=1
      
        flip = random.uniform(0,1)
        print(flip)

        if (flip<0.5) :
                     print("Tails")
                     numOfTails+=1
        else :
             print("Heads")
             numOfHeads+=1 
                     
PercentageofHeads = ((numOfHeads/numberOfFlips) *100)
print("Percentage of heads = ")
print(PercentageofHeads)

PercentageOfTails = ((numOfTails/numberOfFlips) *100)
print("Percentage of tails = ")
print(PercentageOfTails)
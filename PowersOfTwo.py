'''
@Author: Dayananda C
@Date: 2021-08-11 10:30:00
@Last Modified by: Dayananda C
@Last Modified time: 2021-08-11 10:55:00
@Title : To print a table of powers of two till the user entered number
'''

def printPower() :

  N = int(input("Enter Number : "))

  i = 1
  while(i<=N<31) :
       
       powerOfTwo = 2 ** i
       print(powerOfTwo)
       i+=1
       
printPower()   

'''
@Author: Dayananda C
@Date: 2021-08-11 10:30:00
@Last Modified by: Dayananda C
@Last Modified time: 2021-08-11 10:55:00
@Title : Program to print the Nth harmonic value
'''

Number = int(input("Enter Harmonic value of N : "))
i=1
harmonicseries = 0
print("Harmonic series : ")
while (i<=Number and Number !=0 ) :

    print ("{}/{} +".format(1,i) ,end=" ")
    harmonicseries =harmonicseries+ 1/i 
    i+=1

print()
print("Sum of harmonic series = {} ".format(harmonicseries) )
'''
@Author: Dayananda C
@Date: 2021-08-11 10:30:00
@Last Modified by: Dayananda C
@Last Modified time: 2021-08-11 10:55:00
@Title : Print prime factors of a number
'''


print("Finding the prime factors of a number \n")

Number = int(input("Enter the number : "))
i=2
print("Prime factors are")
while(i<=Number and Number !=0 ) :
    
    if Number%i == 0 :
         print(i) 

    i+=1
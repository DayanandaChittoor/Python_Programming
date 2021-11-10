'''
@Author: Dayananda C
@Date: 2021-08-11 10:30:00
@Last Modified by: Dayananda C
@Last Modified time: 2021-08-11 10:55:00
@Title : To check the entered year is leap year or not
'''

def findLeapYear() : 
         
    inputYear = int(input("Enter year :"))
  
    checkLength = str(inputYear)
    lengthOfYear = len(checkLength)

    if (lengthOfYear == 4) :
           if inputYear % 100 != 0 and inputYear % 4 == 0 or inputYear % 400 == 0 :
                  print(str(inputYear) + " is a leap year")
           else :
                 print(str(inputYear) + " is not a leap year")
             
    else :
        print("Please enter a four digit number")
        findLeapYear()

findLeapYear()  
'''
@Author: Dayananda C
@Date: 2021-08-11 10:00:00
@Last Modified by: Dayananda C
@Last Modified time: 2021-08-11 10:30:00
@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

def printName() :

 UserName = input("Enter the User Name : ")

 Length = len(UserName)

 if ((Length >= 3 ) & ( Length <= 20)) :
          print ("Hello " + UserName + ", How are you?")
 else :
     print ("Username should have atleast three characters and should not exceed twenty characters")
     printName()

printName()
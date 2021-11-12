'''
@Author: Dayananda C
@Date: 2021-09-11 
@Time:  11:00:00
@Last Modified by: Dayananda C
@Title : A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0
'''

from array import* 

def SumOfIntegers() :
    try:
         
        length =int(input("Enter the length of array = "))
     
        intArray = array('i' ,[])

        for i in range(length):
            values = int(input("Enter the value in array : "))
            intArray.append(values)

        count =0
        for i in range(0,length):

            for j in range(i+1,length):

                for k in range(j+1,length):
                    
                    if(intArray[i] +intArray[j]+intArray[k] == 0):
                                print(intArray[i],intArray[j],intArray[k])  
                                count +=1                   
        print("Number of triplets : {}  ".format(count)) 
    
    except ValueError :
        print("Please enter a valid input")
        SumOfIntegers()

print("Enter the values for printing triples")
SumOfIntegers()
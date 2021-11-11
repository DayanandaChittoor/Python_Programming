'''
@Author: Dayananda C
@Date: 2021-09-11 
@Time:  10:00:00
@Last Modified by: Dayananda C
@Title : Take input from user and Print Two dimensional array
'''

from array import*

def twoDimensionalArray() :
    try:
        M_Rows = int(input("Enter Number of rows : "))
        N_Coloumns = int(input("Enter number of coloumn : "))
    
        matrix = []
        x=1
        for i in range(M_Rows):
            a=[]
            for j in range(N_Coloumns):
                 elements= (input("Enter element " + str(x) +" : "))
                 x+=1
                 a.append(elements)
            matrix.append(a)
    
        for i in range(M_Rows):
            for j in range(N_Coloumns):
             print(matrix[i][j],end = " ")
            print()    

    except ValueError:
        print("Invalid input, as you can not enter string")
        twoDimensionalArray()

print("To print Two Dimensional Array \n")
twoDimensionalArray()

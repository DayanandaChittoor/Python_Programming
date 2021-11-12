'''
@Author: Dayananda C
@Date: 2021-10-11 
@Time:  18:00:00
@Last Modified by: Dayananda C
@Title : Coupon Number
'''

from array import*
from random import randint
class CouponNumber:
    
    def findDistinctCoupon(self):
        
        Number = int(input("Enter the Coupon number : "))  
        Coupon =[]
    
        maxLimit =int(input("Enter max limit : "))
        count = 0
        i=1
        isRepeated = True
        for i in range(1,Number) :
            import random
            randomNum = randint(1,maxLimit)
            if randomNum not in Coupon :
                Coupon.append(randomNum)
                count+=1
            elif randomNum in Coupon :
                isRepeated = False    
            else:
                print("Does not contain any distict  number")

        print ("Distinct coupon number's {}: ".format(count))
        print(Coupon)
        print("-------------Coupon Numbers--------------")

print("Welcome to Coupon numbers program")
cn = CouponNumber()
cn.findDistinctCoupon()      
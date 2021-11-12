'''
@Author: Dayananda C
@Date: 2021-11-11 
@Time:  12:00:00
@Last Modified by: Dayananda C
@Title : Gambler Program
'''

from random import randint

class Gambler:
    def findPercentage(self):
    
        stake =int(input("Enter the stake : "))
        goal = int(input("Enter the goal : "))
        numberOfBets = int(input("Enter the number of bets to be placed :"))

        countBets = 0
        countWins = 0
        countLoss = 0

        while True:

            if stake == 0 or numberOfBets == countBets or stake == goal :    
                break

            else:
                random_value = randint(0,1)
                countBets = countBets + 1

                if random_value == 1:
                    stake = stake + 1
                    countWins = countWins + 1
                    

                else:
                    stake = stake- 1
                    countLoss = countLoss + 1

        print("Number of wins : {}".format(countWins)) 
        print("Number of loss : {}".format(countLoss))               
        print("Percentage of win : ", (countWins / countBets) * 100, "%")
        print("Percentage of loss : ", (countLoss / countBets) * 100,"%")

print("----------------Gambler program ------------------")
gambler = Gambler()
gambler.findPercentage()
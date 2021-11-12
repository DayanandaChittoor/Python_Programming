'''
@Author: Dayananda C
@Date: 2021-10-11 
@Time:  18:00:00
@Last Modified by: Dayananda C
@Title : StopWatch program
'''

import time 

class stopWatch:
    def elapsedTime() :
        try:
            start = int(input("To start press 1:"))
            startTime = time.time()
            print(startTime) 
                
            stop =int(input("\npress 0 to stop:"))
            stopTime = time.time()
            print(stopTime)

            Elapsed = stopTime - startTime
            print("\nTime Elapsed of stopwatch is :", Elapsed,'sec' ) 
            
        except ValueError:
            print("You have an Exception")

        
print("Welcome to Stopwatch Program \n")
stopWatch.elapsedTime()

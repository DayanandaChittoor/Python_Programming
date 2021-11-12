'''
@Author: Dayananda C
@Date: 2021-09-11 
@Time:  13:00:00
@Last Modified by: Dayananda C
@Title : Windchill
'''
def Windchill() :
    try:
        temperature= float(input("Enter temperature :"))
        windSpeed = float(input("Enter windspeed  :"))

        if temperature < 50 and  windSpeed >=3 and windSpeed < 120 :
            v = pow(windSpeed ,0.16)
            windChill = 35.74 + (0.6215 * temperature) + ((0.4275 * temperature) - 35.75)  * v
            print( "Windchill  = {} ".format(windChill))   
     
    except ValueError:
        print("Please enter a valid input!")
        Windchill()

print("To calculate the Wind Chill \n")
Windchill()
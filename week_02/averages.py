#2-3 Number Averager - W200 Fall 2021
#Tiffany Smalley
import math

#validate user input - ensure it is a numeric value
while True:
    try:
        numberOne = float(input("Please enter one number:"))
        if numberOne:
            break
    except ValueError:
        print ("Please enter a numeric value only.")
        continue

#validate user input - ensure it is a numeric value
while True:
    try:
        numberTwo = float(input("Please enter another number:"))
        if numberTwo:
            break
    except ValueError:
        print ("Please enter a numeric value only.")
        continue

#validate user input - ensure it is a numeric value
#complete calculation and assign value to variable for printing
while True:
    try:
        whichMean = int(input("Please select an average type: enter 1 for Arithmetic Mean , enter 2 for Geometric Mean , enter 3 for Root-Mean-Square:  "))
        if whichMean == 1:
            calcMean  = "Arithmetic Mean : " + str((numberOne + numberTwo)/2)
            break
        elif whichMean == 3:
            calcMean = "Root-Mean-Square : " + str(math.sqrt((((numberOne**2)+(numberTwo**2))/2)))
            break
        elif whichMean == 2:
            calcMean = "Geometric Mean : " + str(math.sqrt(numberOne + numberTwo))
            break
    except ValueError:
        print ("Please enter a numeric value only.")
        continue

#print result
print(calcMean)

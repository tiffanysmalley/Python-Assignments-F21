#2-2 Gas Pump Informer - W200 Fall 2021
#Tiffany Smalley

print("Gas Pump Informer")
print("-----------------")
#validate user input - ensure it is a positive numeric value
while True:
    try:
        gasIn = float(input("Enter a number of gallons for conversion:"))
        if gasIn>0:
            break
        else:
            print("Please enter a positive number of gallons.")
    except ValueError:
        print ("Please enter a positive numeric value only.")
        continue
#convert to string for printing
gasInStr = str(gasIn)

#print input
print("You entered " + gasInStr + " gallons")
print("-----------------")

#declare variables to hold the result of each conversion
gasLiters = gasIn*3.7854
gasBarrel = gasIn/19.5
gasPrice = gasIn*3.65

#print out the results
print(gasInStr + " gallons is equivalent to {:0.4f}".format(gasLiters) +" liters")
print(gasInStr + " gallons requires {:0.3f}".format(gasBarrel) +" barrels to produce")
print("For " + gasInStr + " gallons you will pay ${:0.2f}".format(gasPrice) +" USD total on average")

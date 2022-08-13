#2-1 Tip Calculator - W200 Fall 2021
#Tiffany Smalley

#Validate user input - start a loop until broken by set condition
while True:
    try:
        #collect input and try to convert to float
        price = float(input("Enter the price of a meal: $"))
        #check that input is not negative
        if price>0:
            break
        else:
        #throw error if negative
            print("Please enter a positive number.")
    #throw error for non-numeric value, continue to reprompt
    except ValueError:
        print ("Please enter a positive numeric value.")
        continue

#convert input to float
price = float(price)
tip = price * 0.16
total = price + tip

print("--------------------------")
print("A 16% tip would be: {:0.2f}".format(tip))
print("The total including tip would be: {:0.2f}".format(total))

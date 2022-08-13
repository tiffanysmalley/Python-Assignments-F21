#2-4 Income Tax Calculator - W200 Fall 2021
#Tiffany Smalley

#validate input - must be a number value
while True:
    try:
        income = float(input("Please enter your income: $"))
        if income >= 0:
            break
    except ValueError:
        print ("Please enter a positive, numeric value only.")
        continue

#implement logic structure to place in correct tax bracket
#if the total income is less than or equal to 1000 then we just apply 5%
if income <= 1000:
    tax = income*.05
#if it is between 1001 and 2000, we apply the 5% for the first $1k and 10% to anything after that
elif income >= 1001 and income <=2000:
    tax = ((income-1000)*.1) + 50
#if it greater than or equal to 2001, we apply the 5% for the first $1k, 10% to the second $1k, then 15% to anything above that
elif income >= 2001:
    tax = (((income-2000)*.15) + 50 + 100)

#print result
print("The tax owed is: ${:0.2f}".format(tax))

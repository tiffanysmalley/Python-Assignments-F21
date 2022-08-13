#2-5 Palindrome - W200 Fall 2021
#Tiffany Smalley

#take in string input
nameIn = str(input("Enter your name: "))

#iterate backward through string, assigning to new string
nameBackward = ""
i = len(nameIn)
j = len(nameIn)

while i > 0:
    #if it's the first letter, capitalize
    if i == j:
        nameBackward += nameIn[i-1].upper()
    #else, make it lowercase
    else:
        nameBackward += nameIn[i-1].lower()
    #decrement
    i-=1
    #print("testing iterative output: " + nameBackward)

#create temporary use variables to avoid any case issues in comparison
testNI = nameIn.lower()
testNB = nameBackward.lower()

if testNB == testNI:
    print(nameBackward)
    print("Palindrome!")
else:
    print(nameBackward)

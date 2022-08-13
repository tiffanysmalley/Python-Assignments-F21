#contents of scrabble.py
import sys
import wordscore

#Give nickname to scorer imported from wordscore
scorer = wordscore.score_word#(validMatch)

def noWilds(stringIn, scorer):
    """Matching function for all inputs that contain no wildcard chars.
    Takes that string and the scorer to return a list of tuples of valid
    works with thier scores"""
    matches = []
    #loop through data list
    #look at each word in the scrabble universe
    for word in data:
        #create a temp string to manipulate, reset to the stringIn
        tempString = stringIn
        #create a build string, reset to ""
        buildString = ""
        #look at each character in the word from data
        for char in word:
            #if the char is in the string input
            if char in tempString:
                buildString+=char
                #remove the first instance of that char from the temp string
                tempString = tempString.replace(char,"",1)
                if word == buildString:
                    matches.append((scorer(word), word.lower()))
                    break
            #otherwise, it's not in there, break from this for loop.
            else:
                break
    #return full list of matches found
    return matches


def wildList(numWilds, stringIn, wcSet, alphaSet, scorer):
    """takes in a string with one or two Wildcards and returns a list of
    potential string combinations using every character, regardless of order"""
    #prepare a list of tuples for return
    newStrs=[]

    #1 wildcard character
    if numWilds == 1:
        #for each character in that string, replace the ? or * with each
        #letter of the alphabet and add it to a tuple along with the score
        for char in stringIn:
            for alpha in alphaSet:
                if char == "?" or char == "*":
                    wildString = stringIn.replace(char, alpha)
                    if wildString not in newStrs:
                        #remove this is if doesnt work
#                         sortedChar = str(sorted(wildString))
#                         wildString ="".join(sortedChar)
#                         print("printed: ", wildString)
                        newStrs.append(((scorer(wildString)-scorer(alpha)), wildString.upper()))
        return newStrs

    #2 wildcard characters
    tempString = ""
    tester = 0
    #if there are two wild characters
    if numWilds == 2:
        #if the only characters are wilds
        #find all unique 2-char combos of all letters and add them
        if len(stringIn)==2:
            for alpha in alphaSet:
                for alpha2 in alphaSet:
                    tempString = alpha + alpha2
                    tester+=1
                    if tempString not in newStrs:
                        newStrs.append((0,tempString.upper()))
                    tempString = ""
            #print("tester in wilds only: ", tester)
            #print("len of list of tuples returned: ", len(newStrs))
            return newStrs

        i = 0
        #if the string is more than just wildcards
        if len(stringIn)>2:
            for char in stringIn:
                for alpha in alphaSet:
                    #replace the wildcardswith alpha chars
                    tempString = stringIn.replace('*', alpha).replace('?',alpha)
                    if tempString not in newStrs:
                            #append with scores minus the wildcard letters (score 0)
                            newStrs.append((int(scorer(tempString.upper())-scorer(alpha)-scorer(alpha)), tempString.upper()))
                            #print(tempString.upper())
                    currAlphInd = alphaSet.index(alpha)
                    #only need combos that won't duplicate
                    for i in range(currAlphInd,26):
                        if alphaSet[i] != alpha:
                            #append with scores minus the wildcard letters (score 0)
                            tempString = stringIn.replace('*', alpha).replace('?',alphaSet[i])
                            if tempString not in newStrs:
                                newStrs.append((int(scorer(tempString.upper())-scorer(alpha)-scorer(alphaSet[i])), tempString.upper()))
                                tester+=1
            #print("tester in wilds +: ", tester)
            #print("len of list of tuples returned: ", len(newStrs))
            #print(newStrs)
            return newStrs

def matchWithWilds(strList):
    """takes each wildcard options and loops through to match to data strings"""
    #matchlist
    matches = []
    #loop through data list, look at each word in the scrabble universe
    for word in data:
        #look at each word in the strList
        for stringIn in strList:
            #create a temp string to manipulate, reset to the stringIn
            tempString = stringIn[1]
            #create a build string, reset to ""
            buildString = ""
            #look at each character in the word from data
            for char in word:
                #if the char is in the tempString/string at hand
                if char in tempString:
                    buildString+=char

                    #remove the first instance of that char from the temp string
                    tempString = tempString.replace(char,"",1)
                    if word == buildString and word.lower() not in [x[1] for x in matches]:
                        matches.append((stringIn[0],word.lower()))
                        break
                #otherwise, it's not in there, break from this for loop.
                else:
                    break
    return matches



#main function -------------------


#establish permitted letters and WC set
alphaSet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
wcSet = ['?','*']

#get all scrabble words
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]

#grabs arguments from command line
try:
    string = sys.argv[1]
except:
    print("No input recieved.")
    sys.exit(1)

stringIn = sys.argv[1]
#stringIn = input("Enter a string: ")
stringIn = stringIn.upper()

#EXCEPTION---
#raise an exception if stringIn is < 2 char or > 7 char
if len(stringIn) < 2 or len(stringIn) > 7:
    raise Exception("Input cannot be more than 7 or less than 2 chars")
    exit()

#EXCEPTION---
#Raise and exception if anything but an alpha character + wildcard chars * ?
wilds =0
for char in stringIn:
    if char not in alphaSet:
        if char not in wcSet:
            raise Exception("Input must be an alpha character or one of 2 wildcard characters (? or *)")
            exit()
    if char in wcSet:
        wilds += 1
    if wilds > 2:
        raise Exception("You have input too many wildcards. 2 is the maximum")
        exit()
#EXCEPTION---
#Raise and exception if more than one ? or * each
if stringIn.count('*')>1 or stringIn.count('?')>1:
    raise Exception("You may only enter one ? wildcard and * wildcard max")


#list to hold tuples of matches with scores
matches = []

##will need to change this
#scorer = score_word

#if there are no wildcards
if wilds == 0:
    matches = noWilds(stringIn, scorer)

#if there are either 1 or 2 wildcards
if wilds == 1 or wilds == 2:
    #get a list of matching strings permutations
    wildList = wildList(wilds, stringIn, wcSet, alphaSet, scorer)
    #remove any dupes
    wildList = list(set(wildList))
    #get a list of tuples
    matches = matchWithWilds(wildList)

#sort the list
matches = sorted(matches, key=lambda item: (item[0]), reverse=True)

#print the list
for wordScore in matches:
    print("({}, {})".format(*wordScore))
#print total number of words
print("Total number of words:", len(matches))

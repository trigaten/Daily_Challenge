"""Takes a string of numbers from a user and outputs a list of possible english character 
representations of those numbers -- I am in highschool and am not super experienced with Python
As such, there may be a number of inefficiences -- I am not sure if copy is needed?
Please lmk if anything is done poorly -- I'd like to learn
Throws ERROR if digit !member of [2, 9] is input
"""
from copy import copy
# gets the string of numbers from user and makes it into a list
pNumber = list(input())
# the ASCII character value right below 'a'
chrLoc = 96
# construct dictionary of mappings from number to its 3 or 4 possible letters
numToLet = {}
for i in range(2, 10):
    # if there are 4 letters for this number
    if i is 7 or i is 9:
        ls = []
        for j in range(4):
            chrLoc+=1
            ls.append(chr(chrLoc))
        numToLet[str(i)] = ls
    # if there are 3 letters for this number
    else:
        ls = []
        for j in range(3):
            chrLoc+=1
            ls.append(chr(chrLoc))
        numToLet[str(i)] = ls

# construct list of possible character representations of the numerical string
possibilities = []
# takes the user input string of numbers and modifies it character by character (recursively) according to the loc (int) position
def do(pNumber, loc):
    if loc < len(pNumber):
        letters = numToLet[pNumber[loc]]
        for i in letters:
            c = copy(pNumber)
            c[loc] = str(i)
            do(c, loc+1)
    else:
        possibilities.append(pNumber)

do(pNumber, 0)

print("There are " + str(len(possibilities)) + " different combinations possible")
print(possibilities)
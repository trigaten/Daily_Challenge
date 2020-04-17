from copy import copy
pNumber = list(input())
# the ASCII character value right below 'a'
chrLoc = 96
# construct dictionary 
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
# construct possibilities list
possibilities = []
# takes the user input string of numbers and modifies it bit by bit according to the loc (int) position
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
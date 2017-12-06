

myList = [1,2,3,5,8]
print(myList)
print(myList[0])
print(myList[4])

def printMyList():
    print('In the function')
    for i in range(0, len(myList)):
        print(myList[i], end='  ')

# calling the function
printMyList()

def addMyList():
    sumOffList = 0
    print('\nSumming up my list off numbers')
    for i in range(0, len(myList)):
        sumOffList = sumOffList + myList[i]
    print('The sum off myList is ', sumOffList)

addMyList()

print(sum(myList[:]))
import turtle

myTurtle = turtle.Turtle()
myTurtle.shape('turtle')
#mySecondTurtle = turtle.Turtle()

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

def usingTurtleWithLists():
    for i in range(0, len(myList)):
        myTurtle.forward(myList[i]*10)
        myTurtle.right(90)


print(sum(myList[:]))

usingTurtleWithLists()  ## ??

turtle.done()
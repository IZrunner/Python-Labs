import copy
import sys

# task 1
print("--------------TASK_1--------------")
someListOne = []
someListTwo = [1, 101]
someListThree = []

for counter in range(3):
    hackVar = input("Type your variable here : ")
    someListThree.append(hackVar)

print(someListThree)

someListFour = list()

# task 2
print("--------------TASK_2--------------")
someListCopyOne = someListOne.copy()
someListCopyTwo = someListTwo[:]
someListCopyThree = list(someListThree)
someListCopyFour = copy.deepcopy(someListFour)


# task 3
print("--------------TASK_3--------------")
someListFour.append(someListTwo[0])
print(someListFour)


# task 4
print("--------------TASK_4--------------")
print(someListThree[0]) # a
someListThree[1] = 3 * [3] # b
print(someListThree)
del someListThree[2] # c
print(someListThree)
print(max(someListTwo)) # d


print("--------------TASK_5--------------")
nextList = [ 22,['ogo',3,88],'apple']

for localCounter in nextList:
    if type(localCounter) is list:
        if 88 in  localCounter:
            indexVar = localCounter.index(88)
            print(localCounter[indexVar])


print("--------------TASK_6--------------")
listTaskSix = [1,2,3,4,5,6,7,8]
listStartPos = len(listTaskSix) / 2
listTaskSixNew = listTaskSix[int(listStartPos):]
print(listTaskSixNew)


print("--------------TASK_7--------------")
listEndIndex = -3
listStartPos = 0

for localCounter in listTaskSix:
    if listStartPos == 3:
        break
    listTaskSix.insert(listStartPos, listTaskSix[listEndIndex])
    listTaskSix.pop(listEndIndex)
    listEndIndex += 1
    listStartPos += 1
print(listTaskSix)


print("--------------TASK_8--------------")
listTaskSix.sort(reverse=True)
print(listTaskSix)


print("--------------TASK_9--------------")
listTaskSix = [1,2,3,4,5,6,7,8]
sumOfListElements = 0

for localCounter in listTaskSix:
    print(localCounter)
    sumOfListElements += localCounter
print(sumOfListElements)


print("--------------TASK_10--------------")
someStr = 'Hello'
listTaskNine = []

for localCounter in someStr:
    listTaskNine.append(3*localCounter)
print(listTaskNine)


print("--------------TASK_11--------------")
someList = [[4,6,7],
            [9,5,1]]
someListModified = []

for localCounter in someList:
    for nestedCounter in range(len(localCounter)):
        if nestedCounter == 1 and localCounter[nestedCounter] % 2 == 1:
            someListModified.append(localCounter[nestedCounter])
            print(someListModified)


print("--------------TASK_12--------------")
someList = [[1,2,3],
            [4,5,6],
            [6,4,1]]
someListModified = []
antiDiagonal = int(len(someList) - 1)

for localCounter in someList:
    for nestedCounter in localCounter:
        someListModified.append(localCounter[antiDiagonal])
        break
    antiDiagonal -= 1

print(someListModified)
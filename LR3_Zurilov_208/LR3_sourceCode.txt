import sys
import copy
from math import pi
from typing import List, Union, Tuple

print("--------------TASK_1--------------\n")
someTupleOne = ('value',)
someTupleTwo = ()
someTupleThree = (1, 2, 3)

print(someTupleOne)
print(someTupleTwo)
print(someTupleThree)


print("\n--------------TASK_2--------------\n")
someTupleTwo = copy.copy(someTupleOne)
someTupleOne = copy.deepcopy(someTupleThree)

print(someTupleTwo)
print(someTupleOne)


print("\n--------------TASK_3--------------\n")
someTupleFour = someTupleTwo, someTupleThree
print(someTupleFour)


print("\n--------------TASK_4--------------")
print("----------------A----------------\n")
print(someTupleFour[0])
print("\n----------------B----------------\n")
someTupleFive = [2, 4, 6, 8, 10, 12, 14], someTupleOne
print(someTupleFive)
print("\n----------------C----------------\n")
someTupleSix = ('One', 'Two', 'Three', 'Over_Nine_Thousand', 'Ziltoid_The_Omniscient')
print(max(someTupleSix))
print(max(someTupleThree))


print("\n--------------TASK_5--------------\n")
t = (22, ('ogo', 3, 88), 'apple')
for counter in t:
    if type(counter) is tuple:
        if 'ogo' in counter:
            indexVar = counter.index('ogo')
            print(counter[indexVar])


print("\n--------------TASK_6--------------\n")
someTupleEight = (2, 4, 6, 8, 10, 12)
bufLength = int((len(someTupleEight) / 2))
print(someTupleEight[bufLength:])


print("\n--------------TASK_7--------------\n")
someTupleEightSorted = sorted(someTupleEight, reverse=True)
print(someTupleEight)
print(someTupleEightSorted)


print("\n--------------TASK_8--------------\n")
elementsSum = 0
for counter in someTupleEight:
    elementsSum += counter
    print(str(counter) + " " + str(elementsSum))


print("\n--------------TASK_9--------------\n")
someTupleNine = ((6, 2),
                 (2, 0),
                 (4,))
print(someTupleNine)
someTupleNineSorted = tuple(sorted(someTupleNine, key=lambda item: item[0]))
print(someTupleNineSorted)


print("\n--------------TASK_10--------------\n")
for counter in range(1, 5):
    print(counter)
else:  # Executed because no break in for
    print("No Break")


#print("\n--------------REPEAT_TASK_1--------------\n")
# someRepeatMatrix = [[1, 2, 3, 4],
#                     [2, 3, 4, 5],
#                     [3, 4, 5, 6],
#                     [4, 5, 6, 7]]
# startPositionOne = 0
# startPositionTwo = 0

# for counter in range(len(someRepeatMatrix)):
#     if startPositionOne == counter:
#         for nestedCounter in range(len(someRepeatMatrix[counter])):
#             if nestedCounter == startPositionTwo:
#                 print(someRepeatMatrix[counter])
#             startPositionTwo += 2
#     startPositionOne += 2
#     startPositionTwo = 0


print("\n--------------REPEAT_TASK_2--------------\n")
l = [-1, 3, -5, 6, 7, 6, -7, 8]
lFixed = []
for counter in l:
    if counter > 0:
        lFixed.append(counter)
print(lFixed)


print("\n--------------REPEAT_TASK_3--------------\n")
someRepeatList = []
for counter in range(1, 4):
    someLocalTuple = (counter, counter ** 2)
    someRepeatList.append(someLocalTuple)
print(someRepeatList)


print("\n--------------REPEAT_TASK_4--------------\n") #this must work, but it doesn't
counter = 1
someRepeatOtherList = [round(pi, 2) for pi in range(6)]
print(someRepeatOtherList)










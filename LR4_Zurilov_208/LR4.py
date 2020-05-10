import sys
import copy

print("--------------TASK_1--------------\n")
someEmptySet = set()
someSetOne = {1, 2, 3}
someSetTwo = {'abc', 'abc', 'cde', 'efg'}
someSetThree = {counter for counter in 'Rainbow' if counter not in 'Rrbw'}
print(someSetOne)
print(someSetTwo)
print(someSetThree)


print("\n--------------TASK_2--------------\n")
someSetOne.update(someSetTwo)
print(someSetOne)


print("\n--------------TASK_3--------------\n")
someSetFour = someSetOne.union(someSetTwo)
print(someSetFour)


print("\n--------------TASK_4--------------")
print("----------------A-----------------\n")
print(someSetTwo)


print("\n----------------B-----------------\n")
# userInput = input("Input some string to search it in the previous set:")
# someCheck = userInput in someSetTwo
# if someCheck:
#     print("Yes, user input exists")
# else:
#     print("No, user input doesn't exists")


print("\n--------------TASK_5--------------\n")
someSetComparison = {'abc', 'cde'}
someSetFive = someSetTwo.difference(someSetComparison)
print(someSetFive)


print("\n--------------TASK_6--------------\n")
someSetSix = someSetTwo.intersection(someSetComparison)
print(someSetSix)


print("\n--------------TASK_7--------------\n")



print("\n--------------TASK_8--------------\n")
someSetFour.update([6, 7, 8])
someSetFour.update((1, 2, 3))
someSetFour.update("Hello world")
someSetFour.update({'name':'Killer', 'last name':'Queen'})
print(someSetFour)


print("\n--------------TASK_9--------------\n")
someSetFour.remove(1)
someSetFour.discard("zzzzzz")
print(someSetFour)


print("\n--------------TASK_10--------------\n")
someSetFourReference = someSetFour
someSetFour.clear()
print(someSetFour)


print("\n--------------TASK_11--------------\n")
del someSetFourReference
del someSetFour


print("\n--------------REPEAT_TASK_1--------------\n")
someOtherList = [counter**2 for counter in range(4)]
# someOtherTuple = (counter**2 for counter in range(4)) #<generator object <genexpr> at 0x000001F1A3C6C318>
someOtherSet = {counter**2 for counter in range(4)}
print(someOtherList)
print(someOtherSet)
# print(someOtherTuple) #<generator object <genexpr> at 0x000001F1A3C6C318>

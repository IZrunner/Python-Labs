import sys
import copy

# print("Dio")
# 1.	Продемонструйте в коді способи створення словників без використання конструктора.
print("----------------TASK_1----------------\n")
someDictOneTOne = {'like': 'a', 'rainbow': 'in', 'the': 'dark'}
someDictTwoTOne = {}
print(someDictOneTOne['like'])
print(someDictTwoTOne)

# 2.	Продемонструйте в коді способи створення словників з використанням конструктора.
print("\n\n----------------TASK_2----------------\n")
someDictOneTTwo = dict({'some': 'body', 'once': 'told me'})
someDictTwoTTwo = dict([('the world', 'is gonna'), ('roll', 'me')])
someDictThreeTTwoSquares = {x: x * x for x in range(6)}
print(someDictOneTTwo['some'])
print(someDictTwoTTwo['the world'])
print(someDictThreeTTwoSquares)

# 3.	Створіть новий  словник із елементів двох інших словників.
print("\n\n----------------TASK_3----------------\n")
someDictOneTTwo.update(someDictTwoTTwo)
print(someDictOneTTwo)

# 4.	Є словник із довільної кількості  елементів.
# a.	Виведіть на екран всі елементи множини парами: ключ, значення (два способи)
print("\n\n----------------TASK_4_a----------------\n")
print(someDictOneTTwo)
for key, value in someDictOneTTwo.items():
    print(key, value)

# b.	Перевірте, чи є введене з клавіатури значення, ключем словника.
# print("\n----------------TASK_4_b----------------\n")
# checkKey = input("Enter the key to check : ")
# if checkKey in someDictOneTTwo:
#     print("Yes, '" + str(checkKey) + "' is one of the keys in the 'someDictOneTTwo' dictionary")
# else:
#     print("Not an existing key")


# 5.	Створіть словник, який містить наступні ключі: “one”,”two”,”three”. Всім ключам повинно відповідати значення 33.
print("\n\n----------------TASK_5----------------\n")
buffList = ['one', 'two', 'three']
someDictOneTTFive = {x: 33 for x in buffList}
print(someDictOneTTFive)

# 6.	Створіть словник, який містить наступні ключі: “one”,”two”,”three”. Всім ключам повинно відповідати значення - кортеж (33,44).
print("\n\n----------------TASK_6----------------\n")
someDictOneTTSix = {x: (33, 44) for x in buffList}
print(someDictOneTTSix)

# 7.	За допомогою генератора словників створіть наступний словник
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
print("\n\n----------------TASK_7----------------\n")
someDictOneTTSev = {x: x * 2 for x in range(5)}
print(someDictOneTTSev)

# 8.	Є словник 	 d=dict(a="hello",b=2,c=3,d="hello")
# Сформуйте список ключів, у яких значення дорівнює “hello”.
print("\n\n----------------TASK_8----------------\n")
d = dict(a="hello", b=2, c=3, d="hello")
l = [x for x in d if d[x] == "hello"]
print(l)


# 9.	Продемонструйте додавання  до словника елементів всіх допустимих типів.
print("\n\n----------------TASK_9----------------\n")
someDictOneTTSev.update({3: 4})
someDictOneTTSev.update(keyStr='valueStr')
someDictOneTTSev.update({'listKey': ['one', 'two']})
someDictOneTTSev.update({'tupleKey': ('some', 'values')})
someDictOneTTSev.update({'mapKey': {'hiddenKey': 'hiddenValue', 'secretKey': 'secretValue'}})
print(someDictOneTTSev)


# 10.	Видаліть із словника існуючий та неіснуючий елемент.
print("\n\n----------------TASK_10----------------\n")
del someDictOneTTSev['mapKey']
print(someDictOneTTSev)
resultValue = someDictOneTTSev.pop('nonExistingKey', 'You\'re trying to delete a non-existing key')
print("The return value is : " + resultValue)


# 11.	Видаліть із словника всі елементи.
print("\n\n----------------TASK_11----------------\n")
someDictOneTTSev.clear()
print(someDictOneTTSev)


# FIX LATER
# 12.	Маємо два оператори:
# d=dict(a=1,b=2,c=3)
# print(?)
# Що треба написати в параметрах print, щоб отримати текст “error” при зверненні до d з ключем “k”?(інших операторів додавати не можна)
print("\n\n----------------TASK_12----------------\n")
d = dict(a=1, b=2, c=3)
# print(d[])


# 13.	Маємо наступний  список словників:
# За допомогою генератора словників видаліть словник, який містить дубль id.
print("\n\n----------------TASK_13----------------\n")
data = [
    {'id': 10, 'data': '...'},
    {'id': 11, 'data': '...'},
    {'id': 12, 'data': '...'},
    {'id': 10, 'data': '...'},
    {'id': 11, 'data': '...'},
]

newData = [dict(t) for t in {tuple(d.items()) for d in data}]
print(newData)







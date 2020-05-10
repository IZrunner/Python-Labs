import copy

class ShopGoods:
    def __init__(self, name="Iron Throne", amount=1, price=123):
        self.__name = name
        self.__amount = amount
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__amount

    @property
    def price(self):
        return self.__price


print("--------------TASK_1.1--------------")
l = [[1, 8], [5, 3], [2, 6]]
lSorted = sorted(l, key=lambda x: x[0], reverse=True)
print(lSorted)


print("--------------TASK_1.2--------------")
someStr = "This is a test string from Andrew"
someStrList = someStr.split()
someStrList.sort(key=lambda x: x.lower())
print(someStrList)


print("--------------TASK_1.3--------------")
l = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
lSorted = sorted(l, key=lambda x: x[2], reverse=False)
print(lSorted)


print("--------------TASK_2--------------")
weirdSofa = ShopGoods("Weird Sofa", 2, 321)
print(weirdSofa.name)
print(weirdSofa.amount)
print(weirdSofa.price)


print("--------------REPEAT_TASK_1--------------")
print(sum([1, 2, 3, 4, 5])) # sum values in a list
print(sum((1, 2, 3, 4, 5))) # sum values in a tuple
print(sum({1, 2, 3, 4, 5})) # sum values in a set


print("--------------REPEAT_TASK_2.1--------------")
# fio = "Ivanov"
# def fun():
#     print(fio)
#     fio = "Petrov"
# fun() # UnboundLocalError: local variable 'fio' referenced before assignment
#       # wasn't explicitly set as 'global' or 'local' inside the function


print("--------------REPEAT_TASK_2.2--------------")
t1 = (1,[2,3],4)
t2 = copy.copy(t1)
t1[1].append(5) # append 5 to editable list -> OK
print(t2)
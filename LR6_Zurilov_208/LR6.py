import copy


# -----------------TASK_1.1-----------------
def someFunc1(arg1, arg2):
    if (arg1 > arg2):
        return print(arg1)
    else:
        return print(arg2)


# -----------------TASK_1.2-----------------
def someFunc2(arg1=1, arg2=3, arg3=5, arg4=7):
    print(arg1, arg2, arg3, arg4)


# -----------------TASK_1.3-----------------
def someFunc3(name, weight, height):
    print(name, weight, height)


# -----------------TASK_1.4-----------------
def someFunc4(*params):
    print("Amount of arguments : ", len(params))


# -----------------TASK_1.5-----------------
def someFunc5(**params):
    return print(params)


# -----------------TASK_1.6-----------------
def someFunc6(arg1, arg2):
    temp = arg1
    arg1 = arg2
    arg2 = temp
    return print("arg1 = ", arg1, " arg2 = ", arg2)


# -----------------TASK_1.7-----------------
def someFunc7(list):
    list2 = [i for i in list * 2]
    return print(list2)


# -----------------TASK_1.8-----------------
def someFunc8(listt):
    listt = [1, 2]
    print("list : ", listt)


# -----------------TASK_1.9-----------------
def someFunc9(string):
    list2 = list()
    counter = 0
    list2.append(string[0])
    for i in string:
        if i is " ":
            list2.append(string[counter + 1])
        counter = counter + 1
    print(list2)


# -----------------TASK_1.10-----------------
def someFunc10(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    if n == 2:
        return result
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result


# -----------------TASK_1.11-----------------
x = 10


def someFunc11():
    print("Before someFunc11 x = ", x)
    someFunc11_1()
    print("After someFunc11_1 x = ", x)
    someFunc11_2()
    print("After someFunc11_2 x = ", x)
    someFunc11_3()


def someFunc11_1():
    x = 20
    print("In someFunc11_1 x = ", x)


def someFunc11_2():
    global x
    x = 20
    print("In someFunc11_2 x = ", x)


def someFunc11_3():
    y = 4
    print("In someFunc11_3 y = ", y)

    def someFunc11_4():
        nonlocal y
        y = 8

    someFunc11_4()
    print("After someFunc11_4 y = ", y)


# Що буде в результаті виконання наступного коду?
def someFunc12(a, l=[]):
    l.append(a)
    print(l)


def someFunc13(a, l=()):
    l = l + (a,)
    print(l)


def main():
    print("-----------------TASK_1.1-----------------\n")
    # 1.1.1. integer
    someFunc1(5, 3)
    # 1.1.2. double
    someFunc1(1.5, 1.8)
    # 1.1.3. one parameter is double, other - integer
    someFunc1(1.9, 1)
    print()

    print("\n-----------------TASK_1.2-----------------\n")
    someFunc2()
    someFunc2(0)
    someFunc2(0, 0)
    someFunc2(0, 0, 0)
    someFunc2(0, 0, 0, 0)
    print()

    print("\n-----------------TASK_1.3-----------------\n")
    someFunc3(name="Ivan", weight="65", height="170")
    print()

    print("\n-----------------TASK_1.4-----------------\n")
    someFunc4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print()

    print("\n-----------------TASK_1.5-----------------\n")
    someFunc5(a=1, b=2, c=3)
    print()

    print("\n-----------------TASK_1.6-----------------\n")
    someFunc6(12, 34)
    print()

    print("\n-----------------TASK_1.7-----------------\n")
    someFunc7([1, 2, 3, 4, 5])
    print()

    print("\n-----------------TASK_1.8-----------------\n")
    l = [1, 2, 3]
    print("l = ", l)
    someFunc8(l)
    print("l = ", l)
    print()

    print("\n-----------------TASK_1.9-----------------\n")
    someFunc9("Somebody once told me the world is gonna roll me")
    print()

    print("\n-----------------TASK_1.10-----------------\n")
    print(someFunc10(20))
    print()

    print("\n-----------------TASK_1.11-----------------\n")
    someFunc11()
    print()

    print("\n-----------------TASK_2-----------------\n")
    for i in range(4, 7):
        someFunc12(i)
    print()

    print("\n-----------------TASK_3-----------------\n")
    for i in range(4, 7):
        someFunc13(i)
    print()

    print("\n-----------------TASK_4-----------------\n")
    t1 = (1, [2, 3], 4)
    t2 = copy.copy(t1)  # create another link to memory area t1, need to use deepcopy
    t1[1].append(5)
    print(t2)
    print()


main()
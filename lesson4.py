# def calc(a, b=6):
#     return a*b
# print(calc(5, b=9))


# result = calc(5, 9)
# print(f'result: {result}')
#
# print(calc(5))
#
# def person(f_name, age, l_name):
#     return f'Hello, my name is {f_name} {l_name}. I am {age} years old'
#
# print(person('Anna', 25, 'Smith'))

# print(sum([5, 6, 7, 4]))
# print(max([5, 6, 7, 4]))
#
# def pattern(lenght, char1, char2):
#     return (char1 + char2) * lenght + char1
#
# print(pattern(8, '*', '-'))
#
# print(f'Locals: {locals()}')
#


# mult = lambda x, y: x*y
# print(mult(5, 6))



# l1 = [20, 15, 8, 7, 6]
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2, l))
# filtered2 = list(filter(lambda y: isinstance(y, str), l))
# # print(filtered2)
# # print(filtered)
# # print(*filtered2)
# power = list(map(lambda x: x**2, l1))
# print(power)

# power = list(map(lambda x: x**2 if isinstance(x,int) else x, l))
# print(power)
# from functools import reduce
# result = reduce(lambda x, y: x - y, l1)
#
# print(result)


# def my_decorator(func):
#     def wrapper():
#         print('я - обертка!')
#         func()
#         print('Завернули')
#     return wrapper()
# @my_decorator
# def say_hello():
#     print(f'Hello')
#
#
# def my_decorator(func):
#     def wrapper(arg):
#         print('я - обертка!')
#         func(arg)
#         print('Завернули')
#     return wrapper
# @my_decorator
# def say_hello(name):
#     print(f'hello, {name}')
#
# say_hello('Sam')

# def milk(func):
#     def wrapper():
#         print('hot milk')
#         func()
#     return wrapper()
# def sugar(func):
#     def wrapper():
#         print('sugar')
#         func()
#     return wrapper()
# @sugar
# @milk
# def coffee():
#     print('Coffee')
# coffee()


# import datetime as dt
# print(dt.date.today())
# bdate = 1986
# current_date = dt.date.today()
# age = current_date.year - bdate
# current_month = current_date.month
# print(age)
# print(current_month)
#
# import math as m
# print(m.prod(l1))


# def add_it(a, b, c=3):
#     return a + b + c
# print(add_it(8,10,3))

# import Module
# from Module import *
# print(Module.sum(3,5))
# from Module import *
# print(hello('Sam'))
# print(sum(5, 8))
#
# # print(dir(__builtins__))
# # print(globals())
# # print(f'Locals: {locals()}')
#
# var = 'global'
# def func1():
#     var = 'enclosed'
#     def local():
#         var = 'local'
#         print(var)
#     local()
# func1()
# print(f'outside: {var}')

# def mult(a, b):
#     return a * b
#
# num = (mult(5, 11))
# print(num)
#
# num2 = (mult(5,2))
# print(num2)

# def say_hello():
#     print('Hello')
#
# say_hello()

# def check_even(a):
#     if a % 2 == 0:
#         print('yes')
#     else:
#         print('no')
#
# for i in range(88):
#     check_even(i)


# def fun():
#    s = 'hel'
#    print(s)
# fun()
# print(s)
# не найдет из-за области видимости

# def fun():
#    print(f'first {s}')
# s = 'hello'
# fun()
# print(f'second {s}')

# глобальное пространство имен

# age = 17
# def print_age():
#     print(age)
#
# print_age()

# локальное пр-во имен
# def print_age():
#     age = 17
#     print(age)
#
# print_age()
# print(age)  не работает т.к. переменная локальная

# def multi():
#     x = 10
#     y = 5
#
#     def sum_fun():
#         c = 20
#         print(x + y + c)
#     sum_fun()
#
# multi()

########

# def multi():
#     x = 10
#
#     def sum_fun():
#         c = 20
#         print(x + y + c)
#     sum_fun()
#
# y = 5
# multi()

# def multi(a, b):
#     print(a * b)
#
# multi(2,5,10) error

#
# a, b, *c = [3, 'hi', 2, True]
# print(a, b, c)
#

# def fun(a,b,c):    разобраться
#     print(a, b, c)
#
# a1 = [True, 51, 'hello']
# fun(*a1)

# def fun(*args):
#     s = 0
#     for i in args:
#         s += i
#     print(s)
# fun(1, 4, 7, 19, 10, 12)

# def fun(*args):
#     s = 0
#     print(args)
#     for i in args:
#         s += i
#     print(s)
# a = (1, 4, 7, 19, 10, 12)
# fun(*a)

# def fun(*args):
#     lst = args
#     name = args[0]
#     last_name = args[2]
#     print(f'hello, {name} {last_name}')
#     print(lst)
#
# fun('denis', 'denisov', 'denisovich', 23, 'Kazan')

# def return_dict(**kwargs):
#     print(kwargs)
#
# return_dict(a=2, b='ggg', c=6)
#
# def return_dict(**args):
#     print(args)
#
# return_dict(a=2, b='ggg', c=6)

# def fun(x):
#     if x < 10:
#         print(x)
#         fun(x+1)
# fun(8)

# def fact(n):
#     if n == 1 :
#         return 1
#     return fact(n-1) * n
#
# print(fact(4))


# def fib(v):
#     if v == 0:
#         return 0
#     if v == 1:
#         return 1
#     return fib(v-1) + fib(v-2)
#
# print(fib(3))

# def fun(x):
#     return x**3
# print(fun(3))

# a = lambda x: x**3
# print(a(3))

# s = lambda x: x*x
# print(s(4))

# a = lambda x: 'chet' if x % 2 == 0 else 'nechet'
# print(a(88))

# def fun(num):   сортировка по последней цифре
#     return num % 10
#
# a = [4, 10, 43, 98, 34, 9]
# print(sorted(a, key=fun))

# перевод в список
# a = '1 2 3 4 5'
# b = list(map(int, a.split()))
# print(b)

# перевод в список
# a = '1 2 3 4 5'
# b = list(map(str, a.split()))
# print(b)

def fun(x):
    return x**2

def fun_n(x):
    return x**3

a = [1, 3, 5 ,7, -67, -3]
# a1 = list(map(str, a))
# print(a1)

# a2 = list(map(abs, a)) делает отрицательные числа положительными
# print(a2)
#
# a3 = list(map(fun, a))
# print(a3)

def create_array(n):
    res=[]
    i=1
    while i <= n:
        res += [i]
    return res












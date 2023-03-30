# def calc(a, b=1):
#     print(a*b)   тело ф-ции
#     return a+b   возвращаемое значение
#
# result = calc(5, 9)
# print(f'result: {result}')
#
# print(calc(5))
#
# def person(age, f_name, l_name):
#     return f'Hello, my name is {f_name} {l_name}. I am {age} years old'

# print(person(25, 'anna', 'Smith'))

# print(sum([5, 6, 7, 4]))
# print(min([5, 6, 7, 4]))

# def pattern(lenght, char1, char2):
#     return (char1 + char2) * lenght + char1
#
# print(pattern(8, '*', '-'))
#
# mult = lambda x, y: x-y
# print(mult(5, 6))

l1 = [20, 15, 8, 7, 6]
l = [20, 'str', 15, 188, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2, l))
# print(filtered)
# print(*filtered) unpacking
# power = list(map(lambda x: x**2 if isinstance(x, int) else x, l))
# print(power)
#
# from functools import reduce
# result = reduce(lambda x, y: x - y, l1)
# print(result)


# def say_hello(name):    не работает
#     print(f'hello, {name}')
#
# def my_decorator(func):
#     def wrapper(arg):
#         print('я - обертка!')
#         func(arg)
#         print('Завернули')
# #     return wrapper()
#
# @my_decorator
# def say_hello(name):
#     print(f'hello, {name}')
#
# say_hello('Sam')

import datetime
print(datetime.date.today())
bdate = 1986
current_date = datetime.date.today()
age = current_date.year - bdate
current_month = current_date.month
print(age)
print(current_month)

import math as m
print(m.prod(l1))






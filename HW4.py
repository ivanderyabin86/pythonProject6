# Task 4.1
# def my_square(a=5):
#     return (a*4, a*a, a * (2**(0.5)))
# print(my_square(a=6))

# Task 4.2

# def business_card(first_name, last_name, age, position):
#     card = []
#     card.append(first_name)
#     card.append(last_name)
#     card.append(age)
#     card.append(position)
#     return card
#
# manager = business_card('John', 'Smith', 35, 'Web-developer')
# print("First name:", manager[0])
# print("Last name:", manager[1])
# print("Age:", manager[2])
# print("Position:", manager[3])



# Task 4.3

my_list = [20, -3, 15, 2, -1, -21]
filtered = list(filter(lambda x: isinstance(x, int) and x > 0, my_list))
print(filtered)

# the same result without lambda
# result = []
# for i in range(0, len(my_list)):
#     if my_list[i] > 0:
#         result.append(my_list[i])
# print(result)

# the same result without lambda 2
# def new (a):
#     result = []
#     for i in range(0, len(my_list)):
#         if my_list[i] > 0:
#             result.append(my_list[i])
#     return result
# print(new(my_list))


# Task 4.4

my_list = [20, -3, 15, 2, -1, -21]

xy = lambda x, y: x*y
a = 1
for i in range (0, len(my_list)):
    a = xy(a, my_list[i])
print(a)


# пошагово
# my_list2 = [2, 3, 4]  
# xy = lambda x, y: x*y
# a = 1
# for i in range (0, len(my_list2)):
#     a = xy(a, my_list2[i])
#     print('a = ' + str(a))
#     print('my list i = ' + str(my_list2[i]))



# Task 4.5





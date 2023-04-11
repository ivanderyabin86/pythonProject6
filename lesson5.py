# class Dog:
#     biology_class = 'Animals'
#     def __int__(self, name, weight, colour):
#         self.name = name
#         self.weight = weight
#         self.colour = colour
#
#     def run(self):
#         return 'I can run!'
#
#     def get_name(self):
#         return f'Hi, my name is {self.name}'
#
#
# dog1 = Dog('Bob', 3, 'black')
# print(dog1.name)
# # print(dog1.biology_class)
#
# dog2 = Dog('Rex', 3, 'Red')
# print(dog2.biology_class)
# print(dog2.get_name())
#
#
# class Pitbull(Dog):
#     def __int__(self, name, weight, colour):
#         super().__init__(name, weight, colour)
#         self.passport = passport
#
#
#     def give_a_paw(self):
#         return 'I can give a paw'
#
# dog3 = Pitbull('Lasie', 8, 'Black', 'Type1')
# # print(dog3.get_name())
# # print(dog3.biology_class)
# # print(dog3.give_a_paw())
# print(dog2.run())
# print(dog3.run())
#
# print(dog2.__dict__)
#
# class hotel:
#     property_class = 'For rent'
#     def __init__(self, name, capacity, restaurants, staff, profit):
#         self.__name = name
#         self.capacity = capacity
#         self.restaurants = restaurants
#         self.staff = staff
#         self.profit = profit
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#     def get_name(self):
#         return f'Welcome to {self.__name}'
#
#
#     def roomservice(self):
#         return f'We provide room service 24/7'
#
#
# hotel1 = hotel('Grand Relax Hotel', 300, 2, 40, 750000)
# print(hotel1.name)
# print(hotel1.get_name())
# print(hotel1.hotel_class)
#
# hotel2 = hotel('Sleepy Hollow', 150, 1, 30, 400000)
# # print(hotel2.hotel_class)
# print(hotel2.get_name())
# print(hotel2.set_name('Hollow'))
# print(hotel2.get_name())
# # print(hotel2.__name)
#
# print(hotel2.__dict__)
# print(hotel2._hotel__name)
#
#
# class motel(hotel):
#
#     def __init__(self, name, capacity, restaurants, staff, profit, gas_station):
#         super().__init__(name, capacity, restaurants, staff, profit)
#         self.gas_station = gas_station
#
#     def gas(self):
#         return 'We have a gas station !'
#
#     def roomservice(self):
#         return 'We provide room service'
#
# hotel3 = motel('Highway to Hell', 100, 0, 10, 200000, 'Yes')
# print(hotel3.get_name())
# print(hotel3.gas())
# print(hotel3.property_class)
# print(hotel2.roomservice())gi
# print(hotel3.roomservice())
#
#
#

def add(a, b):
    return a + b
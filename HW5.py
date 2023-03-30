class hotel:
    property_class = 'For rent'
    def __init__(self, name, capacity, restaurants, staff, profit):
        self.__name = name
        self.capacity = capacity
        self.restaurants = restaurants
        self.staff = staff
        self.profit = profit

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return f'Welcome to {self.__name}'


    def roomservice(self):
        return f'We provide room service 24/7'


hotel1 = hotel('Grand Relax Hotel', 300, 2, 40, 750000)
# print(hotel1.name)
# print(hotel1.get_name())
# print(hotel1.hotel_class)

hotel2 = hotel('Sleepy Hollow', 150, 1, 30, 400000)
# print(hotel2.hotel_class)
print(hotel2.get_name())
print(hotel2.set_name('Hollow'))
print(hotel2.get_name())
# print(hotel2.__name)

print(hotel2.__dict__)
print(hotel2._hotel__name)


class motel(hotel):

    def __init__(self, name, capacity, restaurants, staff, profit, gas_station):
        super().__init__(name, capacity, restaurants, staff, profit)
        self.gas_station = gas_station

    def gas(self):
        return 'We have a gas station !'

    def roomservice(self):
        return 'We provide room service'

hotel3 = motel('Highway to Hell', 100, 0, 10, 200000, 'Yes')
# print(hotel3.get_name())
# print(hotel3.gas())
# print(hotel3.property_class)
# print(hotel2.roomservice())
# print(hotel3.roomservice())




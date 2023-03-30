# def largest_sum(s):
#     return max(sum(map(int,x)) for x in s.split('0'))

# age = int(input('Введите ваш возраст: '))
# if age < 7:
#     print('Приходите когда-нибудь потом')
# if age >= 7 and age <= 18:
#     print('Добро пожаловать, гони 10 долларов, также можно сфотографироваться за 3 доллара')
# elif age > 18:
#     print(('Добро пожаловать, гони 20 долларов, также можно сфотографироваться за 3 доллара'))

print("Го в наш зоопарк!")
age = int(input("Введите ваш возраст: "))
if age < 7:
        print("Извините, вы слишком малы для катания.")
if age >= 7 and age <= 18:
    ticket_price = 10
    photo_option = input("Хотите ли вы сделать фотографию за $3? (да/нет): ")
    if photo_option == "да":
        ticket_price += 3
        print(f"Цена билета: ${ticket_price}")
    if photo_option == "нет":
        print(f"Цена билета: ${ticket_price}")
elif age > 18:
    ticket_price = 20
    photo_option = input("Хотите ли вы сделать фотографию за $3? (да/нет): ")
    if photo_option == "да":
        ticket_price += 3
        print(f"Цена билета: ${ticket_price}")
    if photo_option == "нет":
        print(f"Цена билета: ${ticket_price}")


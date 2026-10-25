shopping_list = ["Молоко", "Хлеб", "Колбаса", "Яйца", "Макароны", "Сыр", "Спагетти", "Сосиски", "Соус песто", "Печеньки",]


def shopping_list():
    while shopping_list:
        print(type(shopping_list))
        print(bool(shopping_list))
        print(shopping_list)
        item = shopping_list.pop(0)
        print("Купить:" + item)
        print("")

    print(type(shopping_list))
    print(bool(shopping_list))
    print(shopping_list)

def wh_tr ():
    while True:
        number = int(input("Введите число: "))
        for i in range(number):
            number -= 1
            print(number)

        if number == 0:
            break

        print(number)

wh_tr()
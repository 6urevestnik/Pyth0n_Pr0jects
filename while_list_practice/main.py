shopping_list = ["Молоко", "Хлеб", "Колбаса", "Яйца", "Макароны", "Сыр", "Спагетти", "Сосиски", "Соус песто", "Печеньки",]


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

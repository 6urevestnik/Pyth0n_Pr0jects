#main
#E == exit
#H == help
#C == counter

print("||========================|")
print("||      -=[name]=-        |")
print("||========================|")
print("||                        |")
print("|| [1] >> counter         |")
print("|| [2] >>                 |")
print("||                        |")
print("|| [H] >> help            |")
print("|| [F} >> to pay respect  |")
print("||                        |")
print("|| [E] >> exit            |")
print("||========================|")

working = True
while working == True:

    is_working = input("Введите continue чтобы продолжить, введите E чтобы выйти: ")
    if is_working =="continue":
        working = True
    elif is_working =="E":
        working = False
        break

    Activity = input('Введите название операции: ')

    if Activity == "1":
        oprt = input('Введите тип операции: ')
        if oprt == "+":
            a = 0
            b = int(input('Введите число: '))
            if b!=0:
                while b!=0:
                    a += b
                    print(a)
                    b = int(input('Введите число: '))
                print(f"Ответ: {a}")
        elif oprt == "-":
            a = int(input('Введите число: '))
            b = int(input('Введите число: '))
            if b!=0:
                while b!=0:
                    a -= b
                    print(a)
                    b = int(input('Введите число: '))
                print(f'Ответ: {a}')

    elif Activity == "F":
        print("||========================|")
        print("||     -=[Respect]=       |")
        print("||========================|")
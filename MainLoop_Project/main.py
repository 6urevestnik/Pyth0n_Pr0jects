#main
#E == exit
#H == help
#C == counter

do_i_work = True
if do_i_work == "E":
    do_i_work = False
    while do_i_work != "E":
        if do_i_work == "H":
            print('Для выхода введите Е')
            print('Press F to pay respect')
            print('Введите С чтобы запустить счётчик')
        elif do_i_work == "C":
            op = input('Выберите операцию: ')
            if op == "+":
                a = 0
                b = int(input('Введите число: '))
                if b != 0:
                    while b != 0:
                        a += b
                        print(a)
                        b = int(input('Введите число: '))
                    print(f'Ответ: {a}')
                elif op == "-":
                    a = int(input('Введите число: '))
                    b = int(input('Введите число: '))
                    if b != 0:
                        while b != 0:
                            a -= b
                            print(a)
                            b = int(input('Введите число: '))
                        print(f'Ответ: {a}')
        elif do_i_work == "F":
            print('Respect')
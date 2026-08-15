print('Добро пожаловать в текстовый калькулятор.')
print('Введите тип операции чтобы продолжить: ')
print('1. Сумма +')
print('2. Разность -')
print('3. Произведение *')
print('4. Деление /')

working = True
while working == True:

    is_working = input('Введите continue чтобы продолжить, введите exit чтобы выйти: ')
    if is_working == 'continue':
        working = True
    elif is_working == 'exit':
        working = False
        break


    Activity = input('Введите тип операции: ')

    if Activity == '+':
        b = 0
        print('Для завершения вычислений введите stop.')
        a = input ('Введите число: ')

        while a != 'stop':
            a = int(a)
            b += a
            print(f'Ответ: {b}')
            a = input('')

            if a == ('stop'):
                print(f'Ответ: {b}')
                break

    elif Activity =='-':
        print('Для завершения вычислений введите stop.')
        b = input('Введите число: ')
        a = input('Введите число: ')

        while a != 'stop':
            b = int(b) - int(a)
            print(f'Ответ: {b}')
            a = input('')

            if a == 'stop':
                print(f'Ответ: {b}')
                break

    elif Activity == '*':
        print('Для завершения вычислений введите stop.')
        a = input('Введите число: ')
        b = input('')

        while b != 'stop':
            b = int(a) * int(b)
            print(f'Ответ:  {a}')
            b = input('')

            if b == 'stop':
                print(f'Ответ: {a}')
                break
    elif Activity == '/':
        print('Для завершения вычислений введите stop.')
        a = input('Введите число: ')
        b = input('')

        while b !='stop':
            a = int(a) / int(b)
            print(f'Ответ: {a}')
            b = input('')

            if b == 'stop':
                print(f'Ответ: {a}')
                break

    elif Activity == '%':
        print('Для завершения вычислений введите stop.')
        percent_working = True

        while percent_working == True:
            a = input('Введите число: ')
            if a == 'stop':
                percent_working = False
                break

            while a != 'stop':
                b = input('Введите процент от числа: ')
                c = int(a) * int(b) / 100
                print(f'Ответ: {c}')
                a = input('')



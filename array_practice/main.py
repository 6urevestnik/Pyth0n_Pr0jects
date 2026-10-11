print("Hello World")

will_repeat = 'Y'
while will_repeat == 'Y':
    if will_repeat == 'Y':

        numbers = []
        print('Введите число. Нажмите Enter для завершения.')

        for num in range(20):
            num = input('| > ')

            if num == '':
                break

            numbers.append(int(num))

        print ('|==========================================================|')
        print(f'| {numbers}')
        dlina = len(numbers)
        print(f'| Количество элементов: {dlina}')
        suma = sum(numbers)
        print(f'| Сумма элементов: {suma}')
        print ('|==========================================================|')

        if dlina > 0:
            mid_arifmetic = suma / dlina
            mid_arifmetic = int(mid_arifmetic)
            print(f'Среднее арифметическое = {mid_arifmetic}')
        else:
            print('Список пуст! Попробуй ещё раз, долбаёб!')

        print('|==========================================================|')
        print('| Повторим?                                                |')
        print('| Введите Y для повтора. Введите N чтобы не повторять.     |')
        print('|==========================================================|')
        will_repeat = input('> ')

    elif will_repeat == 'N':
        break

    print('Fuck u!')
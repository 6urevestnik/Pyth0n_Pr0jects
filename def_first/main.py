#Тут_функции

# Главное меню
def main_menu():
    print('|=========================================================|')
    print('|                  _-=[Something v.1]=-_                  |')
    print('|=========================================================|')
    print('|                    | [Main menu] |                      |')
    print('|                                                         |')
    print('| [1] >> Show menu    [2] >> Calculator                   |')
    print('| [3] >> Counter      [4] >> Equation                     |')
    print('| [5] >> Comparison   [6] >> Exponentiation               |')
    print('| [7] >> Even or not  [8] >> Middle arifmetic (average)   |')
    print('| [9] >> Output       [?] >> ???                          |')
    print('|                                                         |')
    print('| [H] >> Help         [A] >> About                        |')
    print('| [C] >> Credits      [F] >> Pay respect                  |')
    print('| [E] >> Exit         [?] >> ?                            |')
    print('|                                                         |')
    print('|=========================================================|')
# Сделать возможность вызвать меню на русском языке

# Помощь
def help():
    print('|=========================================================|')
    print('|                                                         |')
    print('| > Для выбора действия введите идентификатор из          |')
    print('| квадратных скобок.                                      |')
    print('|                -*-   -*-   -*-                          |')
    print('| > Для выхода из программы введите [E].                  |')
    print('|                -*-   -*-   -*-                          |')
    print('| > [1] >> Show menu - чтобы снова увидеть меню.          |')
    print('|                -*-   -*-   -*-                          |')
    print('| > Выбрать следующие действие можно после                |')
    print('| окончания выбранного действия.                          |')
    print('|                -*-   -*-   -*-                          |')
    print('| > [A] >> Abount - расскажет об авторе.                  |')
    print('|                -*-   -*-   -*-                          |')
    print('| > [C] >> Creedz - выражение благодарности               |')
    print('| всем кто помог написанию программы.                     |')
    print('|                -*-   -*-   -*-                          |')
    print('| > [F] >> Выразите своё уважение.                        |')
    print('|                                                         |')
    print('|=========================================================|')


# О программе
def about():
    print('|=========================================================|')
    print('|                   _-=[USER DATA]=-_                     |')
    print('|=========================================================|')
    print('| HANDLE   : 6urevestnik                                  |')
    print('| CLASS    : Future python god                            |')
    print('| LEVEl    : Not your level bro                           |')
    print('|                                                         |')
    print('| CURRENT SKILLS:                                         |')
    print('| [+] creating unnecessary menus                          |')
    print('| [+] print / input                                       |')
    print('| [+] if / elif / else                                    |')
    print('| [+] while / for                                         |')
    print('| [+] def                                                 |')
    print('| [ ] world domination                                    |')
    print('| [ ] become a god                                        |')
    print('| [ ] survive university                                  |')
    print('|=========================================================|')


# Передаю приветы
def greetz():
    print('|=========================================================|')
    print('|                   _-=[gReEtZ]=-_                        |')
    print('|=========================================================|')
    print('| gReEtZ t0:                                              |')
    print('| >> GitHub       >> Python                               |')
    print('| >> ChatGpt      >> PyCharm                              |')
    print('| >> Daft Punk    >> Coffee                               |')
    print('| >> all coders still using print()                       |')
    print('|=========================================================|')


# Выражаю благодарности
def credits():
    print('|=========================================================|')
    print('|                   _-=[Credits]=-_                       |')
    print('|=========================================================|')
    print('| CODE................................6urevestnik         |')
    print('| DESIGN..............................6urevestnik         |')
    print('| TESTING.............................6urevestnik         |')
    print('| BUGS................................also 6urevestnik    |')
    print('|=========================================================|')

#_______________________________________________________________________________________________________________________

# [2] >> Калькулятор - меню
def calculator_menu():
    print('|=========================================================|')
    print('| Дотсупные операции:                                     |')
    print('| [1] >> Сложение (+)                                     |')
    print('| [2] >> Вычитание (-)                                    |')
    print('| [3] >> Умножение (*)                                    |')
    print('| [4] >> Деление (/)                                      |')
    print('| [5] >> Процент от числа (%)                             |')
    print('| [6] >> Special division                                 |')
    print('|=========================================================|')

# [2] >> Калькулятор - меню выбора
def calculator_selection_menu():
    will_repeat = 'Y'
    while will_repeat == 'Y':

        calculator_menu()
        print('Введите номер операции: ')

        calculator_selection = input('| > ')

        if calculator_selection == '1':
            calculator_addition()
        elif calculator_selection == '2':
            calculator_subtraction()
        elif calculator_selection == '3':
            calculator_multiplication()
        elif calculator_selection == '4':
            calculator_division()
        elif calculator_selection == '5':
            calculator_percent()
        elif calculator_selection == '6':
            calculator_special_division()

        print('|====================================================|')
        print('| Повторим?                                          |')
        print('| Введи Y - для повтора, N - для пропуска            |')
        print('|====================================================|')
        will_repeat = input('| > ').strip().upper()

# [2] >> Калькулятор - сложение
def calculator_addition():
    print('|====================================================|')
    print('| Операция типа: a + b = c                           |')
    print('| Введите числа которые нужно сложить.               |')
    print('|====================================================|')

    while True:
        try:
            print("Введите a: ")
            a = int(input('| > '))
            print("Введите b: ")
            b = int(input('| > '))
            break

        except ValueError:
            print("Ошибка! Введите число.")
            continue

    c = a + b
    print(f'Ответ: {c}')

# [2] >> Калькулятор - вычитание
def calculator_subtraction():
    print('|====================================================|')
    print('| Операция типа: a - b = c                           |')
    print('| Введите числа которые нужно отнять.                |')
    print('|====================================================|')

    while True:
        try:
            print("Введите а: ")
            a = int(input('| > '))
            print("Введите b")
            b = int(input('| > '))
            break

        except ValueError as error:
            print(f"Ошибка - {error}! Введите число!")
            continue

    c = a - b
    print(f'Ответ: {c}')

# [2] >> Калькулятор - умножение
def calculator_multiplication():
    print('|====================================================|')
    print('| Операция типа: a * b = c                           |')
    print('| Введите числа которые нужно перемножить.           |')
    print('|====================================================|')

    while True:
        try:
            print("| Первый множитель: ")
            a = int(input('| > '))
            print('| Второй множитель: ')
            b = int(input('| > '))
            break

        except ValueError:
            print("Ошибка! Введите число!")
            continue

    c = a * b
    print(f'Ответ: {c}')

# [2] >> Калькулятор -  деление
def calculator_division():
    print('|====================================================|')
    print('| Операция типа: a / b = c                           |')
    print('| Введите числа которые нужно разделить:             |')
    print('|====================================================|')

    while True:
        try:
            print("Введите a: ")
            a = int(input('|> '))
            print("Введите b: ")
            b = int(input('|> '))
            break

        except ValueError:
            print("Ошибка! Введите число!")
            continue

        except ZeroDivisionError:
            print("Ошибка! На ноль делить нельзя!")
            continue


    if b != 0:
        print(f'Ответ: {a / b}')
    else:
        print('Ошибка! На 0 делить нельзя!')

# [2] >> Калькулятор -  процент от числа
def calculator_percent():
    print('Операция типа: a * b / 100 = c')
    print('Введите число :')
    a = int(input('| > '))
    print('Введите процент от числа :')
    b = int(input('| > '))
    c = a * b / 100
    print(f'{b}% от числа {a} = {c}')

# [2] >> Калькулятор - специальное деление
def calculator_special_division():
    print('| Введите делимое: ')
    a = int(input('| > '))
    print('| Введите делитель: ')
    b = int(input('| > '))

    if b != 0:
        c1 = a / b
        c2 = a // b
        c3 = a % b
        print(c1)
        print(type(c1))
        print('')
        print(c2)
        print(type(c2))
        print('')
        print(c3)
        print(type(c3))
    else:
        print('Ошибка! На 0 делить нельзя!')
#_______________________________________________________________________________________________________________________

# [3] >> Счётчики - меню
def counter_menu():
    print("|=========================================================|")
    print("| [1] >> Addition                                         |")
    print("|=========================================================|")

# [3] >> Счётчики - меню выбора
def counter_selection_menu():
    will_repeat = 'Y'
    while will_repeat == 'Y':
        counter_menu()

        print("Укажите номер операции: ")
        counter_selection = int(input('| > '))

        if counter_selection == 1:
            counter_addition()

        print('Repeat? Y/N')
        will_repeat = input('| > ')

# [3] >> Счётчики - сложение
def counter_addition():
    a = 0
    b = 0
    print("Введите числа для сложения: ")

    while b != 'stop':
        b = input('| > ')

        if b != 'stop':
            b = int(b)
            a += b
            print('Ответ: ', a)

        elif b == 'stop':
            break
    print("Результат: ", a)

# [3] >> Счётчики - вычитание
def counter_subtraction():
    a = 0
    b = 0
    print('Введите числа для вычитания: ')
    a = int(input('| > '))

    while b != 'stop':
        b = input('| > ')

        if b != 'stop':
            b = int(b)
            a -= b
            print('Ответ: ',a)

        elif b == 'stop':
            break
    print('Результат: ', a)

#_______________________________________________________________________________________________________________________


# [F] - Выражаю уважение
def respect():
    print('|=========================================================|')
    print('|                   -=[Respect!]=-                        |')
    print('|=========================================================|')

#_______________________________________________________________________________________________________________________

# [4] >> Уравнения - меню
def equation_menu():
    print('|=========================================================|')
    print('| [1] >> Сложение     a + b = c                           |')
    print('| [2] >> Вычитание    a - b = c                           |')
    print('| [3] >> Умножение    a * b = c                           |')
    print('| [4] >> Деление      a / b = c                           |')
    print('|=========================================================|')

# [4] >> Уравнения - меню выбор
def equation_selection_menu():
    will_repeat = 'Y'
    while will_repeat == 'Y':

        equation_menu()
        print('Введите номер операции: ')
        equation_selection = input('| > ')

        if equation_selection == '1':
            equation_addition()
        elif equation_selection == '2':
            equation_subtraction()
        elif equation_selection == '3':
            equation_multiplication()
        elif equation_selection == '4':
            equation_division()

        print('|====================================================|')
        print('| Повторим?                                          |')
        print('| Введи Y - для повтора, N - для пропуска            |')
        print('|====================================================|')
        will_repeat = input('| > ').strip().upper()

# [4] >> Уравнения - сложение
def equation_addition():
    a = 0
    b = 0
    c = 0

    print('Уравнение типа: a + b = c')
    print('Введите a: ')
    a = input('| > ')
    print('Введите b: ')
    b = input('| > ')
    print('Введите c: ')
    c = input('| > ')
    if a == 'x':
        b = int(b)
        c = int(c)
        print('Ответ:')
        print(c - b)
    elif b == 'x':
        a = int(a)
        c = int(c)
        print('Ответ: ')
        print(c - a)
    elif c == 'x':
        a = int(a)
        b = int(b)
        print('Ответ:')
        print(a + b)

# [4] >> Уравнения - разность
def equation_subtraction():
    a = 0
    b = 0
    c = 0

    print('Уравнение типа: a - b = c')
    print('Введите a: ')
    a = input('| > ')
    print('Введите b: ')
    b = input('| > ')
    print('Введите c: ')
    c = input('| > ')
    if a == 'x':
        b = int(b)
        c = int(c)
        print('Ответ: ')
        print(c + b)
    elif b == 'x':
        a = int(a)
        c = int(c)
        print('Ответ: ')
        print(a - c)
    elif c == 'x':
        a = int(a)
        b = int(b)
        print('Ответ: ')
        print(a - b)

# [4] >> Уравнения - умножение
def equation_multiplication():
    a = 0
    b = 0
    c = 0

    print('Уравнение типа: a * b = c')
    print('Введите а: ')
    a = input('| > ')
    print('Введите b: ')
    b = input('| > ')
    print('Введите c: ')
    c = input('| > ')
    if a == 'x':
        b = int(b)
        c = int(c)
        if b != 0:
            print('Ответ: ')
            print(c / b)
        else:
            print('Ошибка! На ноль делить нельзя!')

    elif b == 'x':
        a = int(a)
        c = int(c)
        if a != 0:
            print('Ответ: ')
            print(c / a)
        else:
            print('Ошибка! На ноль делить нельзя!')

    elif c == 'x':
        a = int(a)
        b = int(b)
        print('Ответ: ')
        print(a * b)

# [4] >> Уравнения - деление
def equation_division():
    a = 0
    b = 0
    c = 0

    print('Уравнения типа: a / b = c')
    print('Введите a: ')
    a = input('| > ')
    print('Введите b: ')
    b = input('| > ')
    print('Введите c: ')
    c = input('| > ')
    if a == 'x':
        b = int(b)
        c = int(c)
        print('Ответ: ')
        print(c * b)
    elif b == 'x':
        a = int(a)
        c = int(c)
        if c != 0:
            print('Ответ: ')
            print(a / c)
        else:
            print('Ошибка! На ноль делить нельзя!')

    elif c == 'x':
        a = int(a)
        b = int(b)
        if b != 0:
            print('Ответ: ')
            print(a / b)
        else:
            print('Ошибка! На ноль делить нельзя!')

#_______________________________________________________________________________________________________________________

# [5] >> Сравнение - меню
def comparison_menu():
    print('|=========================================================|')
    print('| [1] >> Сравнение двух чисел                             |')
    print('| [2] >> Умное сравнение трёх чисел                       |')
    print('| [3] >> Умное сравнение четырёх чисел                    |')
    print('|=========================================================|')

# [5] >> Сравнение - меню выбора
def comparison_selection_menu():
    will_repeat = 'Y'
    while will_repeat == 'Y':

        comparison_menu()

        print('Введите номер операции: ')
        comparison_selection = input('| > ')

        if comparison_selection == '1':
            comparison_two_numbers()
        elif comparison_selection == '2':
            clever_comparison_three_numbers()
        elif comparison_selection == '3':
            clever_comparison_four_numbers()

        print('|====================================================|')
        print('| Повторим?                                          |')
        print('| Введи Y - для повтора, N - для пропуска            |')
        print('|====================================================|')
        will_repeat = input('| > ').strip().upper()

# [5] >> Сравнение двух чисел
def comparison_two_numbers():
    print('Введите первое число: ')
    a = int(input('| > '))
    print('Введите второе число: ')
    b = int(input('| > '))
    if a > b:
        print(f'Большее число: {a}')
        print(f'Меньшее меньшее: {b}')
        print(f'Разница: {a-b}')
    elif a < b:
        print(f'Большее число: {b}')
        print(f'Меньшее меньшее: {a}')
        print(f'Разница: {b-a}')
    elif a == b or b == a:
        print(f' Числа равны: {a==b}')

# [5] >> Сравнение - умное сравнение (три числа)
def clever_comparison_three_numbers():
    largest = 0
    middle = 0
    smallest = 0

    print('Введите три числа: ')
    a = int(input('| > '))
    b = int(input('| > '))
    c = int(input('| > '))

    if a > b and a > c:
        largest = a
        if b > c:
            middle = b
            smallest = c
        else:
            middle = c
            smallest = b
    elif b > a and b > c:
        largest = b
        if a > c:
            middle = a
            smallest = c
        else:
            middle = c
            smallest = a

    elif c > a and c > b:
        largest = c
        if a > b:
            middle = a
            smallest = b
        else:
            middle = b
            smallest = a

    print(f"{largest} > {middle} > {smallest}")

# [5] >> Сравнение - умное сравнение (четыре числа)
def clever_comparison_four_numbers():
    a = 0
    b = 0
    c = 0
    d = 0

    largest = 0
    middle_high = 0
    middle_low = 0
    smallest = 0

    print('Введите четыре числа: ')
    a = int(input('| > '))
    b = int(input('| > '))
    c = int(input('| > '))
    d = int(input('| > '))

    if a > b and a > c and a > d:     #largest = a
        largest = a

        if b > c and b > d:
            middle_high = b

            if c > d:
                middle_low = c
                smallest = d
            else:
                middle_low = d
                smallest = c

        elif c > b and c > d:
            middle_high = c

            if b > d:
                middle_low = b
                smallest = d
            else:
                middle_low = d
                smallest = b

        elif d > b and d > c:
            middle_high = d
            if b > c:
                middle_low = b
                smallest = c
            else:
                middle_low = c
                smallest = b

    elif b > a and b > d and b >c:     #largest = b
        largest = b

        if a > c and a > d:
            middle_high = a

            if c > d:
                middle_low = c
                smallest = d
            else:
                middle_low = d
                smallest = c

        elif c > a and c > d:
            middle_high = c

            if a > d:
                middle_low = a
                smallest = d
            else:
                middle_low = d
                smallest = a

        elif d > a and d > c:
            middle_high = d

            if a > c:
                middle_low = a
                smallest = c
            else:
                middle_low = c
                smallest = a

    elif c > a and c > b and c > d:      # largest = c
        largest = c

        if a > b and a > d:
            middle_high = a

            if b > d:
                middle_low = b
                smallest = d
            else:
                middle_low = d
                smallest = b

        if b > a and b > d:
            middle_high = b

            if a > d:
                middle_low = a
                smallest = d
            else:
                middle_low = d
                smallest = a

        if d > a and d > b:
            middle_high = d

            if a > b:
                middle_low = a
                smallest = b
            else:
                middle_low = b
                smallest = a

    elif d > a and d > b and d > c:     #largest = d
        largest = d

        if a > b and a > c:
            middle_high = a

            if b > c:
                middle_low = b
                smallest = c
            else:
                middle_low = c
                smallest = b

        elif b > a and b > c:
            middle_high = b

            if a > c:
                middle_low = a
                smallest = c
            else:
                middle_low = c
                smallest = a

        elif c > a and c > b:
            middle_high = c

            if a > b:
                middle_low = a
                smallest = b
            else:
                middle_low = b
                smallest = a

    print(f"{largest} > {middle_high} > {middle_low} > {smallest}")

#_______________________________________________________________________________________________________________________

# [6] >> Возведение в степень - меню
def exponentiation_menu():
    print('|=========================================================|')
    print('| Функции возведения в степень:                           |')
    print('| [1] >> Возведение в квадрат          - a * a            |')
    print('| [2] >> Возведение в куб              - a * a * a        |')
    print('| [3] >> Возведение в квадрат квадрата - a * a * a * a    |')
    print('|=========================================================|')

# [6] >> Возведение в степень - меню выбора
def exponentiation_selection_menu():
    will_repeat = 'Y'
    while will_repeat == 'Y':

        exponentiation_menu()
        print('Введите номер операции: ')
        exponentiation_selection = input('| > ')

        if exponentiation_selection == '1':
            exponentiation_square()
        elif exponentiation_selection == '2':
            exponentiation_cube()
        elif exponentiation_selection == '3':
            exponentiation_squaring_square()

        print('|====================================================|')
        print('| Повторим?                                          |')
        print('| Введи Y - для повтора, N - для пропуска            |')
        print('|====================================================|')
        will_repeat = input('| > ').strip().upper()

# [6] >> Возведение в степень - квадрат
def exponentiation_square():
    print('Введите число для возведения квадрат: ')
    base = int(input('| > '))
    print(f'Ответ: {base} в квадрате = {base**2}')

# [6] >> Возведение в степень - куб
def exponentiation_cube():
    print('Введите число для возведения в куб: ')
    base = int(input('| > '))
    print(f'Ответ: {base} в кубе {base**3}')

# [6] >> Возведение в степень - квадрат квадрата
def exponentiation_squaring_square():
    print('Введите число для возведения в четвёртую степень: ')
    base = int(input('| > '))
    print(f'Ответ: {base} в четвёртой степени = {base**4}')

#_______________________________________________________________________________________________________________________

# [7] - Чётное или нет
def even_or_not():
    will_repeat = 'Y'
    while will_repeat == 'Y':

        print('Введите число для проверки на чётность: ')
        even_check = int(input('| > '))
        even_check_1 = even_check % 2
        if even_check_1 == 0:
            print(f'Число {even_check} чётное')
        else:
            print(f'Число {even_check} не чётное')

        print('|====================================================|')
        print('| Повторим?                                          |')
        print('| Введи Y - для повтора, N - для пропуска            |')
        print('|====================================================|')
        will_repeat = input('| > ').strip().upper()

#_______________________________________________________________________________________________________________________

# [8] - Поиск среднего арифметического
def arithmetic_mean():
    will_repeat = 'Y'
    while will_repeat == 'Y':

        numbers = []
        print('|====================================================|')
        print('| Укажите количество чисел:                          |')
        print('|====================================================|')

        count_ar_mean = int(input('| > '))

        print('|====================================================|')
        print('| Введите число. Нажмите Enter для завершения ввода. |')
        print('|====================================================|')

        for num in range(count_ar_mean):
            a = input('| > ')

            if a == '':
                break

            numbers.append(int(a))

        if len(numbers) > 0:
            print('|======================|=================|========================|')
            print('| Количество элементов | Сумма элементов | Среднее арифметическое |')
            print('|======================|=================|========================|')
            print(f'| {len(numbers):^20} | {sum(numbers):^15} | {sum(numbers)/len(numbers):^22.2f} |')
            print('|======================|=================|========================|')
        else:
            print('Список пуст! Попробуйте ещё раз!')

        print('')
        print('|====================================================|')
        print('| Повторим?                                          |')
        print('| Введи Y - для повтора, N - для пропуска            |')
        print('|====================================================|')
        will_repeat = input('| > ').strip().upper()

#_______________________________________________________________________________________________________________________

# [9] >> Вывод - меню
def output_menu():
    print('|==================|')
    print('| Тут будет меню   |')
    print('|==================|')

# [9] >> Вывод - меню выбора
def output_selection_menu():
    output_menu()
    print('|========================|')
    print('| Тут будет меню выбора  |')
    print('|========================|')

    print('| Введите номер операции')
    output_selection = input('| > ')
    if output_selection == '1':
        output_assigment()

# [9] >> Вывод - операции с присваиванием
def output_assigment():
    print('|==================|')
    print('| тут присваивание |')
    print('|==================|')

#_______________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________

#start - тут начало

main_menu()

working = 'works'
while working !='E':
    print('| Введите идентификатор функции :')
    working = input('| > ').strip()

#Тут надо будет поменять порядок на более системный, либо сначала буквы, а потом цифры, либо по смыслу что важнее
    if working == 'H':
        help()
    elif working == '1':
        main_menu()
    elif working == 'F':
        respect()
    elif working == 'A':
        about()
    elif working == 'G':
        greetz()
    elif working == 'C':
        credits()

# [2] - Калькулятор с выбором функции
    elif working == '2':
        calculator_selection_menu()
    elif working == '33':
        counter_selection_menu()

#_______________________________________________________________________________________________________________________

    # [3] - Счётчики
    elif working == '3':
        print('| Введите знак операции')
        opr2 = input('| > ')

# Счётчик суммы
        if opr2 == '+':
            a = 0
            b = int(input('| > '))
            if b != 0:
                while b != 0:
                    a = a + b
                    print(a)
                    b = int(input('| > '))
                print(f'Ответ: {a}')

# Счётчик разности
        if opr2 == '-':
            a = int(input('| > '))
            b = int(input('| > '))
            if b != 0:
                while b != 0:
                    a = a - b
                    print(a)
                    b = int(input('| > '))
                print(f'Ответ: {a}')

# Счётчик произведения
        if opr2 == '*':
            a = int(input('| > '))
            b = int(input('| > '))
            if b != 0:
                while b != 0:
                    a = a * b
                    print(a)
                    b = int(input('| > '))
                print(f'Ответ: {a}')

# Счётчик деления
        if opr2 == '/':
            a = int(input('| > '))
            b = int(input('| > '))
            if b != 0:
                while b != 0:
                   a = a / b
                   print(a)
                   b = int(input('| > '))
                print(f'Ответ: {a}')

#_______________________________________________________________________________________________________________________

# [4] - Уравнения
    elif working == '4':
        equation_selection_menu()

# [5] - Сравнение
    elif working == '5':
        comparison_selection_menu()

# [6] - Возведение в степень
    elif working == '6':
        exponentiation_selection_menu()

# [7] - Чётное или нечётное
    elif working == '7':
        even_or_not()

# [8] - Поиск среднего арифметического
    elif working == '8':
        arithmetic_mean()

# [9] - Вывод
    elif working == '9':
        output_selection_menu()

    elif working == '00':
        print('T3ST_Z0n3')

    elif working == 'E':
        print('Fuck u!')
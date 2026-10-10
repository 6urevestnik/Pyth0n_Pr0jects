#Тут_функции

# Главное меню
def main_menu():
    print('|=========================================================|')
    print('|                  -=[Something v.1]=-                    |')
    print('|=========================================================|')
    print('|                                                         |')
    print('| [1] >> Show menu   [2] >> Calculator                    |')
    print('| [3] >> Counter     [4] >> Equation                      |')
    print('| [5] >> Comparison  [6] >> Exponentiation                |')
    print('| [?] >> ???         [?] >> ???                           |')
    print('|                                                         |')
    print('| [H] >> Help        [A] >> About                         |')
    print('| [C] >> Credits     [F] >> Pay respect                   |')
    print('| [E] >> Exit        [?] >> ?                             |')
    print('|                                                         |')
    print('|=========================================================|')


# Помощь
def help():
    print('|=========================================================|')
    print('|                                                         |')
    print('| > Для выбора действия введите идентификатор             |')
    print('| из квадратных скобок.                                   |')
    print('|                -*-   -*-   -*-                          |')
    print('| > Для выхода из программы введите [E].                  |')
    print('|                -*-   -*-   -*-                          |')
    print('| > [1] >> Show menu - чтобы снова увидеть меню.          |')
    print('|                -*-   -*-   -*-                          |')
    print('| > Выбрать следующие действие можно после                |')
    print('| окончания выбранного действия.                          |')
    print('|                -*-   -*-   -*-                          |')
    print('| > Для решения простого примера воспользуйтесь           |')
    print('| функцией [2] >> Calculator.                             |')
    print('|                -*-   -*-   -*-                          |')
    print('| > Для решения примера с накоплением ответа              |')
    print('| воспользуйтесь счётчиком [3] >> Counter.                |')
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
    print('|                    -=[USER DATA]=-                      |')
    print('|=========================================================|')
    print('| HANDLE   : 6urevestnik                                  |')
    print('| CLASS    : Future python god                            |')
    print('| LEVEl    : Not your level bro                           |')
    print('|                                                         |')
    print('| CURRENT SKILLS:                                         |')
    print('| [+] creating unnecessary menus                          |')
    print('| [+] input / print                                       |')
    print('| [+] if / elif / else                                    |')
    print('| [+] while                                               |')
    print('| [+] def                                                 |')
    print('| [ ] world domination                                    |')
    print('| [ ] become a god                                        |')
    print('| [ ] survive university                                  |')
    print('|=========================================================|')


# Передаю приветы
def greetz():
    print('|=========================================================|')
    print('|                     -=[gReEtZ]=-                        |')
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
    print('|                     -=[Credits]=-                       |')
    print('|=========================================================|')
    print('| CODE................................6urevestnik         |')
    print('| DESIGN..............................6urevestnik         |')
    print('| TESTING.............................6urevestnik         |')
    print('| BUGS................................also 6urevestnik    |')
    print('|=========================================================|')


# Калькулятор - вводная часть
def calculator_menu():
    print('|=========================================================|')
    print('| Дотсупные операции:                                     |')
    print('| [+] >> Сложение (+)                                     |')
    print('| [-] >> Вычитание (-)                                    |')
    print('| [*] >> Умножение (*)                                    |')
    print('| [/] >> Деление (/)                                      |')
    print('| [%] >> Процент от числа (%)                             |')
    print('| [S] >> Special division                                 |')
    print('|=========================================================|')

# Калькулятор - операция плюс
def calculator_plus():
    a = int(input('| > '))
    b = int(input('| > '))
    c = a + b
    print(f'Ответ: {c}')

# Калькулятор - операция минус
def calculator_minus():
    a = int(input('| > '))
    b = int(input('| > '))
    c = a - b
    print(f'Ответ: {c}')

# Калькулятор - операция умножение
def calculator_multiplication():
    print('Первый множитель: ')
    a = int(input('| > '))
    print('Второй множитель: ')
    b = int(input('| > '))
    c = a * b
    print(f'Ответ: {c}')

# Калькулятор - операция деление
def calculator_division():
    a = int(input('|> '))
    b = int(input('|> '))
    c = a / b
    print(f'Ответ: {c}')

# Калькулятор - операция процент от числа
def calculator_percent():
    print('Введите число :')
    a = int(input('| > '))
    print('Введите процент от числа :')
    b = int(input('| > '))
    c = a * b / 100
    print(f'{b}% от числа {a} = {c}')

# Калькулятор - специальное деление
def calculator_special_division():
    print('| Введите делимое: ')
    a = int(input('| > '))
    print('| Введите делитель: ')
    b = int(input('| > '))
    c1 = a/b
    c2 = a//b
    c3 = a%b
    print(c1)
    print(type(c1))
    print(c2)
    print(type(c2))
    print(c3)
    print(type(c3))

# Выражаю уважение
def respect():
    print('|=========================================================|')
    print('|                   -=[Respect!]=-                        |')
    print('|=========================================================|')

# Уравнения - операция плюс
def equation_plus():
    print('Уравнение типа: a+b=c')
    print('Введите a: ')
    eq1 = input('| > ')
    print('Введите b: ')
    eq2 = input('| > ')
    print('Введите c: ')
    eq3 = input('| > ')
    if eq1 == 'x':
        eq2 = int(eq2)
        eq3 = int(eq3)
        print('Ответ:')
        print(eq3-eq2)
    elif eq2 == 'x':
        eq1 = int(eq1)
        eq3 = int(eq3)
        print('Ответ: ')
        print(eq3-eq1)
    elif eq3 == 'x':
        eq1 = int(eq1)
        eq2 = int(eq2)
        print('Ответ:')
        print(eq1+eq3)

# Уравнения - операция минус
def equation_minus():
    print('Уравнение типа: a-b=c')
    print('Введите a: ')
    eq1 = input('| > ')
    print('Введите b: ')
    eq2 = input('| > ')
    print('Введите c: ')
    eq3 = input('| > ')
    if eq1 == 'x':
        eq2 = int(eq2)
        eq3 = int(eq3)
        print('Ответ: ')
        print(eq3+eq2)
    elif eq2 == 'x':
        eq1 = int(eq1)
        eq3 = int(eq3)
        print('Ответ: ')
        print(eq1 - eq3)
    elif eq3 == 'x':
        eq1 = int(eq1)
        eq2 = int(eq2)
        print('Ответ: ')
        print(eq1-eq2)

# Уравнения - операция умножения
def equation_multiplication():
    print('Уравнение типа: a*b=c')
    print('Введите а: ')
    eq1 = input('| > ')
    print('Введите b: ')
    eq2 = input('| > ')
    print('Введите c: ')
    eq3 = input('| > ')
    if eq1 == 'x':
        eq2 = int(eq2)
        eq3 = int(eq3)
        print('Ответ: ')
        print(eq3/eq2)
    elif eq2 == 'x':
        eq1 = int(eq1)
        eq3 = int(eq3)
        print('Ответ: ')
        print(eq3/eq1)
    elif eq3 == 'x':
        eq1 = int(eq1)
        eq2 = int(eq2)
        print('Ответ: ')
        print(eq1*eq2)

# Уравнения - операция деления
def equation_division():
    print('Уравнения типа: a/b=c')
    print('Введите a: ')
    eq1 = input('| > ')
    print('Введите b: ')
    eq2 = input('| > ')
    print('Введите c: ')
    eq3 = input('| > ')
    if eq1 == 'x':
        eq2 = int(eq2)
        eq3 = int(eq3)
        print('Ответ: ')
        print(eq3*eq2)
    elif eq2 == 'x':
        eq1 = int(eq1)
        eq3 = int(eq3)
        print('Ответ: ')
        print(eq1/eq3)
    elif eq3 == 'x':
        eq1 = int(eq1)
        eq2 = int(eq2)
        print('Ответ: ')
        print(eq1/eq2)

# Сравнение двух чисел
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

# Возведение в степень - меню
def exponentiation_menu():
    print('|=========================================================|')
    print('| Функции возведения в степень:                           |')
    print('| [1] >> Возведение в квадрат          - a * a            |')
    print('| [2] >> Возведение в куб              - a * a * a        |')
    print('| [3] >> Возведение в квадрат квадрата - a * a * a * a    |')
    print('|=========================================================|')

# Возведение в степень - квадрат
def exponentiation_square():
    print('Введите число для возведения квадрат: ')
    base = int(input('| > '))
    print(f'Ответ: {base} в квадрате = {base**2}')

# Возведение в степень - куб
def exponentiation_cube():
    print('Введите число для возведения в куб: ')
    base = int(input('| > '))
    print(f'Ответ: {base} в кубе {base**3}')

# Возведение в степень - квадрат квадрата
def exponentiation_squaring_square():
    print('Введите число для возведения в четвёртую степень: ')
    base = int(input('| > '))
    print(f'Ответ: {base} в четвёртой степени = {base**4}')

# __________________________________________________________

#start - тут начало

main_menu()

working = 'works'
while working !='E':
    print('| Введите идентификатор функции :')
    working = input('| > ')

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
    elif working == '5':
        comparison_two_numbers()

# Калькулятор с выбором функции
    elif working == '2':
        calculator_menu()
        print('| Введите знак операции: ')
        operation_calculate = input('| > ')
        if operation_calculate == '+':
            calculator_plus()
        elif operation_calculate == '-':
            calculator_minus()
        elif operation_calculate == '*':
            calculator_multiplication()
        elif operation_calculate == '/':
            calculator_division()
        elif operation_calculate == '%':
            calculator_percent()
        elif operation_calculate == 'S':
            calculator_special_division()

# 3 - Счётчики
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

# 4 - Уравнения
    elif working == '4':
        eq1 = 0
        eq2 = 0
        eq3 = 0
        print('Выберите тип уравнения: ')
        print('a+b=c - введите +')
        print('a-b=c - введите -')
        print('a*b=c - введите *')
        print('a/b=c - введите /')
        opr3 = input('| > ')
        if opr3 == '+':
            equation_plus()
        elif opr3 == '-':
            equation_minus()
        elif opr3 == '*':
            equation_multiplication()
        elif opr3 == '/':
            equation_division()

# 6 - Возведение в степень
    elif working == '6':
        exponentiation_menu()
        print('| Выберите функцию: ')
        exponentiation_operator = input('| > ')
        if exponentiation_operator == '1':
            exponentiation_square()
        elif exponentiation_operator == '2':
            exponentiation_cube()
        elif exponentiation_operator == '3':
            exponentiation_squaring_square()

    elif working == 'E':
        print('Fuck u!')
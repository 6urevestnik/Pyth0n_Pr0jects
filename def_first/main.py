#start

print('|=================================================|')
print('|              -=[Something v.1]=-                |')
print('|=================================================|')
print('|                                                 |')
print('| [1] >> Show menu   [2] >> Calculator            |')
print('| [3] >> Counter     [4] >>                       |')
print('|                                                 |')
print('| [H] >> Help        [A] >> About                 |')
print('| [C] >> Credits     [F] >> Pay respect           |')
print('| [G] >> gReEtZ      [E] >> Exit                  |')
print('| [?] >> ?????                                    |')
print('|=================================================|')

#Тут_функции

def main_menu():
    print('|=================================================|')
    print('|              -=[Something v.1]=-                |')
    print('|=================================================|')
    print('|                                                 |')
    print('| [1] >> Show menu   [2] >> Calculator            |')
    print('| [3] >> Counter     [4] >>                       |')
    print('|                                                 |')
    print('| [H] >> Help        [A] >> About                 |')
    print('| [C] >> Credits     [F] >> Pay respect           |')
    print('| [E] >> Exit        [?] >> ?                     |')
    print('|=================================================|')

def help():
    print('|================================================|')
    print('| > Для выбора действия введите идентификатор    |')
    print('| из квадратных скобок.                          |')
    print('|                -*-   -*-   -*-                 |')
    print('| > Для выхода из программы введите [E].         |')
    print('|                -*-   -*-   -*-                 |')
    print('| > [1] >> Show menu - чтобы снова увидеть меню. |')
    print('|                -*-   -*-   -*-                 |')
    print('| > Выбрать следующие действие можно после       |')
    print('| окончания выбранного действия.                 |')
    print('|                -*-   -*-   -*-                 |')
    print('| > Для решения простого примера воспользуйтесь  |')
    print('| функцией [2] >> Calculator.                    |')
    print('|                -*-   -*-   -*-                 |')
    print('| > Для решения примера с накоплением ответа     |')
    print('| воспользуйтесь счётчиком [3] >> Counter.       |')
    print('|                -*-   -*-   -*-                 |')
    print('| > [A] >> Abount - расскажет об авторе.         |')
    print('|                -*-   -*-   -*-                 |')
    print('| > [C] >> Creedz - выражение благодарности      |')
    print('| всем кто помог написанию программы.            |')
    print('|                -*-   -*-   -*-                 |')
    print('| > [F] >> Выразите своё уважение.               |')
    print('|================================================|')

def about():
    print('|================================================|')
    print('|               -=[USER DATA]=-                  |')
    print('|================================================|')
    print('| HANDLE   : 6urevestnik                         |')
    print('| CLASS    : Future python god                   |')
    print('| LEVEl    : Not your level bro                  |')
    print('|                                                |')
    print('| CURRENT SKILLS:                                |')
    print('| [+] creating unnecessary menus                 |')
    print('| [+] input / print                              |')
    print('| [+] if / elif / else                           |')
    print('| [+] while                                      |')
    print('| [+] def                                        |')
    print('| [ ] world domination                           |')
    print('| [ ] become a god                               |')
    print('| [ ] survive university                         |')
    print('|================================================|')

def greetz():
    print('|================================================|')
    print('|                -=[gReEtZ]=-                    |')
    print('|================================================|')
    print('| gReEtZ t0:                                     |')
    print('| >> GitHub       >> Python                      |')
    print('| >> ChatGpt      >> PyCharm                     |')
    print('| >> Daft Punk    >> Coffee                      |')
    print('| >> all coders still using print()              |')
    print('|================================================|')

def credits():
    print('|================================================|')
    print('|                -=[Credits]=-                   |')
    print('|================================================|')
    print('| CODE.........................6urevestnik       |')
    print('| DESIGN.......................6urevestnik       |')
    print('| TESTING......................6urevestnik       |')
    print('| BUGS.........................also 6urevestnik  |')
    print('|================================================|')

def calculator_plus():
    a = int(input('| > '))
    b = int(input('| > '))
    c = a + b
    print(f'Ответ: {c}')

def calculator_minus():
    a = int(input('| > '))
    b = int(input('| > '))
    c = a - b
    print(f'Ответ: {c}')

def calculator_multiplication():
    a = int(input('| > '))
    b = int(input('| > '))
    c = a * b
    print(f'Ответ: {c}')

def calculator_division():
    a = int(input('|> '))
    b = int(input('|> '))
    c = a / b
    print(f'Ответ: {c}')

def respect():
    print('|================================================|')
    print('|              -=[Respect!]=-                    |')
    print('|================================================|')


working = 'works'
while working !='E':
    print('Введите идентификатор функции')
    working = input('| > ')

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

    elif working == '2':
        print('| Введите знак операции')
        opr1 = input('| > ')
        if opr1 == '+':
            calculator_plus()
        elif opr1 == '-':
            calculator_minus()
        elif opr1 == '*':
            calculator_multiplication()
        elif opr1 == '/':
            calculator_division()

# Тут счётчики
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

    elif working == 'E':
        print('Fuck u!')
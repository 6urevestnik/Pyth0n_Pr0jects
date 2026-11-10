# Тут все функции
#=======================================================================================================================

# Начальное меню
def start_menu():
    print('in progress')

#=======================================================================================================================

# Функция отображения игрового поля
def show_all():
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)
    print(line_5)
    print(line_6)
    print(line_7)
    print(line_8)
    print(line_9)
    print(line_10)
    print(line_11)
    print(line_12)

#=======================================================================================================================

# Проверка вертикальная
def vertical_check():

    print('Vertical check!')

    for i in range(len(line_1)):
        if line_1[i] == line_2[i] == line_3[i]:
            print(f'line 1-3: {i} {i+1} {i+2}')

            line_1[i] = random.choice(['a', 'b', 'c', 'd'])
            line_2[i] = random.choice(['a', 'b', 'c', 'd'])
            line_3[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_2[i] == line_3[i] == line_4[i]:
            print(f'line 2-4: {i} {i+1} {i+2}')

            line_2[i] = random.choice(['a', 'b', 'c', 'd'])
            line_3[i] = random.choice(['a', 'b', 'c', 'd'])
            line_4[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_3[i] == line_4[i] == line_5[i]:
            print(f'line 3-5: {i} {i+1} {i+2}')

            line_3[i] = random.choice(['a', 'b', 'c', 'd'])
            line_4[i] = random.choice(['a', 'b', 'c', 'd'])
            line_5[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_4[i] == line_5[i] == line_6[i]:
            print(f'line 4-6: {i} {i+1} {i+2}')

            line_4[i] = random.choice(['a', 'b', 'c', 'd'])
            line_5[i] = random.choice(['a', 'b', 'c', 'd'])
            line_6[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_5[i] == line_6[i] == line_7[i]:
            print(f'line 5-7: {i} {i+1} {i+2}')

            line_5[i] = random.choice(['a', 'b', 'c', 'd'])
            line_6[i] = random.choice(['a', 'b', 'c', 'd'])
            line_7[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_6[i] == line_7[i] == line_8[i]:
            print(f'line 6-8: {i} {i+1} {i+2}')

            line_6[i] = random.choice(['a', 'b', 'c', 'd'])
            line_7[i] = random.choice(['a', 'b', 'c', 'd'])
            line_8[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_7[i] == line_8[i] == line_9[i]:
            print(f'line 7-9: {i} {i+1} {i+2}')

            line_7[i] = random.choice(['a', 'b', 'c', 'd'])
            line_8[i] = random.choice(['a', 'b', 'c', 'd'])
            line_9[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_8[i] == line_9[i] == line_10[i]:
            print(f'line 8-10: {i} {i+1} {i+2}')

            line_8[i] = random.choice(['a', 'b', 'c', 'd'])
            line_9[i] = random.choice(['a', 'b', 'c', 'd'])
            line_10[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_9[i] == line_10[i] == line_11[i]:
            print(f'line 9-11: {i} {i+1} {i+2}')

            line_9[i] = random.choice(['a', 'b', 'c', 'd'])
            line_10[i] = random.choice(['a', 'b', 'c', 'd'])
            line_11[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_10[i] == line_11[i] == line_12[i]:
            print(f'line 10-12: {i} {i+1} {i+2}')

            line_10[i] = random.choice(['a', 'b', 'c', 'd'])
            line_11[i] = random.choice(['a', 'b', 'c', 'd'])
            line_12[i] = random.choice(['a', 'b', 'c', 'd'])

    print('')

#=======================================================================================================================

# Проверка горизонтальная
def horizontal_check():

    print('Horizontal check!')

    for i in range(len(line_1)-2):
        if line_1[i] == line_1[i+1] == line_1[i+2]:
            print(f'line_1: {i} {i+1} {i+2}')

            line_1[i] = random.choice(['a', 'b', 'c', 'd'])
            line_1[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_1[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_2[i] == line_2[i+1] == line_2[i+2]:
            print(f'line_2: {i} {i+1} {i+2}')

            line_2[i] = random.choice(['a', 'b', 'c', 'd'])
            line_2[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_2[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_3[i] == line_3[i+1] == line_3[i+2]:
            print(f'line_3: {i} {i+1} {i+2}')

            line_3[i] = random.choice(['a', 'b', 'c', 'd'])
            line_3[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_3[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_4[i] == line_4[i+1] == line_4[i+2]:
            print(f'line_4: {i} {i+1} {i+2}')

            line_4[i] = random.choice(['a', 'b', 'c', 'd'])
            line_4[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_4[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_5[i] == line_5[i+1] == line_5[i+2]:
            print(f'line_5: {i} {i+1} {i+2}')

            line_5[i] = random.choice(['a', 'b', 'c', 'd'])
            line_5[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_5[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_6[i] == line_6[i+1] == line_6[i+2]:
            print(f'line_6: {i} {i+1} {i+2}')

            line_6[i] = random.choice(['a', 'b', 'c', 'd'])
            line_6[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_6[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_7[i] == line_7[i+1] == line_7[i+2]:
            print(f'line_7 {i} {i+1} {i+2}')

            line_7[i] = random.choice(['a', 'b', 'c', 'd'])
            line_7[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_7[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_8[i] == line_8[i+1] == line_8[i+2]:
            print(f'line_8 {i} {i+1} {i+2}')

            line_8[i] = random.choice(['a', 'b', 'c', 'd'])
            line_8[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_8[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_9[i] == line_9[i+1] == line_9[i+2]:
            print(f'line_9 {i} {i+1} {i+2}')

            line_9[i] = random.choice(['a', 'b', 'c', 'd'])
            line_9[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_9[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_10[i] == line_10[i+1] == line_10[i+2]:
            print(f'line_10 {i} {i+1} {i+2}')

            line_10[i] = random.choice(['a', 'b', 'c', 'd'])
            line_10[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_10[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_11[i] == line_11[i+1] == line_11[i+2]:
            print(f'line_11 {i} {i+1} {i+2}')

            line_11[i] = random.choice(['a', 'b', 'c', 'd'])
            line_11[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_11[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

        if line_12[i] == line_12[i+1] == line_12[i+2]:
            print(f'line_12 {i} {i+1} {i+2}')

            line_12[i] = random.choice(['a', 'b', 'c', 'd'])
            line_12[(i+1)] = random.choice(['a', 'b', 'c', 'd'])
            line_12[(i+2)] = random.choice(['a', 'b', 'c', 'd'])

    print('')

#=======================================================================================================================
# Получение ввода от пользователя координат элементов чтобы поменять местами
def user_input():
    line_choose_1 = input('|>...')
    element_choose_1 = input('|>...')


    line_choose_2 = input('|>...')
    element_choose_2 = input('|>...')
#=======================================================================================================================

# Begin
import random

GREEN = "\033[32m"
RESET = "\033[0m"

print(GREEN, end='')

print("Welcome to the game!")

letters = ['a', 'b', 'c', 'd']
line_1 = []
line_2 = []
line_3 = []
line_4 = []
line_5 = []
line_6 = []
line_7 = []
line_8 = []
line_9 = []
line_10 = []
line_11 = []
line_12 = []

for i in range(12):
    line_1.append(random.choice(letters))
    line_2.append(random.choice(letters))
    line_3.append(random.choice(letters))
    line_4.append(random.choice(letters))
    line_5.append(random.choice(letters))
    line_6.append(random.choice(letters))
    line_7.append(random.choice(letters))
    line_8.append(random.choice(letters))
    line_9.append(random.choice(letters))
    line_10.append(random.choice(letters))
    line_11.append(random.choice(letters))
    line_12.append(random.choice(letters))

show_all()
horizontal_check()
vertical_check()
show_all()

print(RESET, end='')

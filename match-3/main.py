print('Hello there!')

def show_all():
    print(arr_1)
    print(arr_2)
    print(arr_3)

def vertical_check():
    for i in range(1):
        if arr_1[i] == arr_2[i] == arr_3[i]:
            print('Успех! Три в ряд!')
            print(arr_1[i], arr_2[i], arr_3[i])
        else:
            print('Проверяю дальше...')

def horizontal_check():
    print('in progress...')

def start_menu():
    print('in progress...')
#===========================================================================================

arr_1 = ['b', 'a', 'a' ]
arr_2 = ['d', 'c', 'b' ]
arr_3 = ['a', 'd', 'c' ]
show_all()
print('|==========================================================|')
print('')

# Создаю горизонтальную проверку три-в-ряд в трех массивах

for i in range(1):
    if arr_1[i] == 'a' and arr_1[i+1] == 'a' and arr_1[i+2] == 'a':
        print(arr_1[i], arr_1[i+1], arr_1[i+2])
        print('Три в ряд! Успех')
        print(arr_1.index(arr_1[i]), arr_1.index(arr_1[i+1]), arr_1.index(arr_1[i+2]))

print('|======================|')
print('|   please stand by    |')
print('|======================|')

print('|==========================================================|')

import random

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
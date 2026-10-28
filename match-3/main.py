# Тут все функции

def start_menu():
    print('in progress')

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

def vertical_check():
    for i in range(11):
        if line_1[i] == line_2[i] == line_3[i]:
            print('Успех! Три в ряд!')
            print(line_1[i], line_2[i], line_3[i])

def horizontal_check():
    for i in range(9):
        if line_1[i] == line_1[i+1] == line_1[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)


#===========================================================================================

# Тут начало
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

show_all()

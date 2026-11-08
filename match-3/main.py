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

# Проверка вертикальная
def vertical_check():
    for i in range(11):
        if line_1[i] == line_2[i] == line_3[i]:
            print('line 1-3')
            print(line_1[i], line_2[i], line_3[i])
            line_1[i] = random.choice(['a', 'b', 'c', 'd'])
            line_2[i] = random.choice(['a', 'b', 'c', 'd'])
            line_3[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_2[i] == line_3[i] == line_4[i]:
            print('line 2-4')
            print(line_2[i], line_3[i], line_4[i])
            line_2[i] = random.choice(['a', 'b', 'c', 'd'])
            line_3[i] = random.choice(['a', 'b', 'c', 'd'])
            line_4[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_3[i] == line_4[i] == line_5[i]:
            print('line 3-5')
            print(line_3[i], line_4[i], line_5[i])
            line_3[i] = random.choice(['a', 'b', 'c', 'd'])
            line_4[i] = random.choice(['a', 'b', 'c', 'd'])
            line_5[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_4[i] == line_5[i] == line_6[i]:
            print('line 4-6')
            print(line_4[i], line_5[i], line_6[i])
            line_4[i] = random.choice(['a', 'b', 'c', 'd'])
            line_5[i] = random.choice(['a', 'b', 'c', 'd'])
            line_6[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_5[i] == line_6[i] == line_7[i]:
            print('line 5-7')
            print(line_5[i], line_6[i], line_7[i])
            line_5[i] = random.choice(['a', 'b', 'c', 'd'])
            line_6[i] = random.choice(['a', 'b', 'c', 'd'])
            line_7[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_6[i] == line_7[i] == line_8[i]:
            print('line 6-8')
            print(line_6[i], line_7[i], line_8[i])
            line_6[i] = random.choice(['a', 'b', 'c', 'd'])
            line_7[i] = random.choice(['a', 'b', 'c', 'd'])
            line_8[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_7[i] == line_8[i] == line_9[i]:
            print('line 7-9')
            print(line_7[i], line_8[i], line_9[i])
            line_7[i] = random.choice(['a', 'b', 'c', 'd'])
            line_8[i] = random.choice(['a', 'b', 'c', 'd'])
            line_9[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_8[i] == line_9[i] == line_10[i]:
            print('line 8-10')
            print(line_8[i], line_9[i], line_10[i])
            line_8[i] = random.choice(['a', 'b', 'c', 'd'])
            line_9[i] = random.choice(['a', 'b', 'c', 'd'])
            line_10[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_9[i] == line_10[i] == line_11[i]:
            print('line 9-11')
            print(line_9[i], line_10[i], line_11[i])
            line_9[i] = random.choice(['a', 'b', 'c', 'd'])
            line_10[i] = random.choice(['a', 'b', 'c', 'd'])
            line_11[i] = random.choice(['a', 'b', 'c', 'd'])

        if line_10[i] == line_11[i] == line_12[i]:
            print('line 10-12')
            print(line_10[i], line_11[i], line_12[i])
            line_10[i] = random.choice(['a', 'b', 'c', 'd'])
            line_11[i] = random.choice(['a', 'b', 'c', 'd'])
            line_12[i] = random.choice(['a', 'b', 'c', 'd'])


# Проверка горизонтальная
def horizontal_check():
    for i in range(9):
        if line_1[i] == line_1[i+1] == line_1[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_2[i] == line_2[i+1] == line_2[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_3[i] == line_3[i+1] == line_3[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_4[i] == line_4[i+1] == line_4[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_5[i] == line_5[i+1] == line_5[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_6[i] == line_6[i+1] == line_6[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_7[i] == line_7[i+1] == line_7[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_8[i] == line_8[i+1] == line_8[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_9[i] == line_9[i+1] == line_9[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_10[i] == line_10[i+1] == line_10[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_11[i] == line_11[i+1] == line_11[i+2]:
            print('Успех! Три в ряд!')
            print(i, i+1, i+2)

        if line_12[i] == line_12[i+1] == line_12[i+2]:
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

#print('horizontal')
#horizontal_check()

print('vertical')
vertical_check()

print('|=======================================================================|')
show_all()
print('vertical')
vertical_check()


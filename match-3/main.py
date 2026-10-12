print('Hello there!')

def show_all():
    print(index)
    print('|==========================================================|')
    print(arr_1)
    print(arr_2)
    print(arr_3)

index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
arr_1 = ['b', 'a', 'a', 'a', 'd', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
arr_2 = ['d', 'c', 'b', 'a', 'd', 'c', 'b', 'a', 'd', 'c', 'b', 'a']
arr_3 = ['a', 'd', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'c', 'd', 'b']
show_all()
print('|==========================================================|')
print('')

arr_2[1], arr_2[2] = arr_2[2], arr_2[1]
show_all()
print('|==========================================================|')

# Создаю горизонтальную проверку три в ряд внутри массива
print('')
for i in range(9):
    print(arr_1[i], arr_1[i+1], arr_1[i+2])
    print(arr_2[i], arr_2[i+1], arr_2[i+2])
    print(arr_3[i], arr_3[i+1], arr_3[i+2])
    print('')

for i in range(9):
    if arr_1[i] == 'a' and arr_1[i+1] == 'a' and arr_1[i+2] == 'a':
        print(arr_1[i])
        print(arr_1[i+1])
        print(arr_1[i+2])
        print('Три в ряд! Успех')
    else:
        print('Проверяю дальше...')

print('')
for i in range(9):
    if arr_2[i] == 'a' and arr_2[i+1] == 'a' and arr_2[i+2] == 'a':
        print(arr_2[i])
        print(arr_2[i+1])
        print(arr_2[i+2])
        print('Три в ряд! Успех!')
    else:
        print('Проверяю дальше...')

print('')
for i in range(9):
    if arr_3[i] =='a' and arr_3[i+1] == 'a' and arr_3[i+2] == 'a':
        print(arr_3[i])
        print(arr_3[i+1])
        print(arr_3[i+2])
        print('Три в ряд! Успех!')
    else:
        print('Проверяю дальше...')

print('')
print('|======================|')
print('|   please stand by    |')
print('|======================|')


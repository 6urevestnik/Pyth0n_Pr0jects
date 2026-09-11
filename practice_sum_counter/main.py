a = int(0)
b = int(input('Введите число: '))

print(a)
print(b)

if b != 0:
    while b != 0:
        a = a + b
        print(a)
        b = int(input('Введите число: '))
else:
    print('Вот и сказочке конец')
    input('Введите любой символ чтобы завершить процесс')
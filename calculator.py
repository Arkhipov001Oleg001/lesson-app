A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
C = input('Введите действие(+, -, *, /):')

if  C == '+':
    print('Ответ:', A + B)# Проверка
elif C == '-':
    print('Ответ:', A - B)
elif C == '*':
    print('Ответ:', A * B)
else:
    print('Ответ:', A / B)
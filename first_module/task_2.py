print('Привет! Это простой калькулятор.')

action = input('Выберите операцию (+ или -): ')
first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

if action == '+':
    print(first_number + second_number)
elif action == '-':
    print(first_number - second_number)
else:
    print('Неверное действие, доступно только + или -')

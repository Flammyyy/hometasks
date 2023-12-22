age = int(input('Введите возраст: '))
accompanied = input('С сопровождающим? (Да/Нет): ')
if age < 12:
    print('Билет бесплатный.')
elif age < 18 and accompanied == 'Да':
    print('Билет со скидкой.')
else:
    print('Полная стоимость билета.')

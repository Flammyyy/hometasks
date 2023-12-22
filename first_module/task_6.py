# Код задания начального уровня
def primary_level():
    try:
        num = int(input('Введите целое число: '))
        if num > 0:
            for i in range(0, num + 1):
                print(i)
        elif num < 0:
            for i in range(0, num - 1):
                print(i)
        elif num == 0:
            print(0)

    except ValueError:
        print('Ошибка. Поддерживаются только целые числа.')


# Код задания базового уровня
def basic_level():
    try:
        num = int(input('Введите целое число: '))
        i = 0
        if num > 0:
            while i <= num:
                print(i)
                i += 1
        elif num < 0:
            while i >= num:
                print(i)
                i -= 1
        elif num == 0:
            print(0)

    except ValueError:
        print('Ошибка. Поддерживаются только целые числа.')


# Выбор уровня и заданий
level_select = input('Какой уровень?\n'
                     'Введите "Начальный", чтобы выбрать задание начального уровня\n'
                     'Введите "Базовый", чтобы выбрать задание базового уровня\n'
                     'Ввод: ')
while level_select not in ['Начальный', 'Базовый']:
    level_select = input('Ошибка. Можно ввести только "Начальный" или "Базовый"\n'
                         'Ввод: ')

if level_select == 'Начальный':
    primary_level()
elif level_select == 'Базовый':
    basic_level()

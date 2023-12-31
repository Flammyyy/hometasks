def primary_level():
    nums = [1, 2, 3, 'str', True, 1.234, False, 8, 9, 10]
    print('Список из 10 элементов ', nums)
    print(f'Первые 5 элементов списка {nums[:5]}',
          f'\nПоследние 3 элемента списка {nums[-3:]}',
          f'\nКаждый второй элемент списка {nums[::2]}')
    nums[0], nums[1], nums[2] = 3, 2, 1
    print(f'Список с 3 измененными значениями {nums}')


def basic_level():
    task_num = input('Введите номер задания\n'
                     'Введите "1", чтобы открыть Задание 1: Работа с списками и срезами\n'
                     'Введите "2", чтобы открыть Задание 2: Работа с условиями и циклами\n'
                     'Ввод: ')

    while task_num not in ['1', '2']:
        task_num = input('Ошибка. Можно ввести только "1" или "2"\n'
                         'Ввод: ')
    # Первое задание
    if task_num == '1':
        primary_level()

    # Второе задание
    elif task_num == '2':
        num = int(input('Введите число: '))
        if num % 3 == 0:
            print('Число делится на 3')
        elif num > 10:
            print('Число больше 10')
        else:
            print('Число не соответствует условиям')


# Выбор уровня и заданий
level_select = input('Какой уровень?\n'
                     'Введите "Начальный", чтобы выбрать задание начального уровня\n'
                     'Введите "Базовый", чтобы выбрать задания базового уровня\n'
                     'Ввод: ')
while level_select not in ['Начальный', 'Базовый']:
    level_select = input('Ошибка. Можно ввести только "Начальный" или "Базовый"\n'
                         'Ввод: ')

if level_select == 'Начальный':
    primary_level()
elif level_select == 'Базовый':
    basic_level()

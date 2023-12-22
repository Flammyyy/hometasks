# Код задания начального уровня
def primary_level():
    t = (2, 6, 72, 35, 12, 6)
    print(f'Кортеж: {t}')
    for el in t:
        print(f'{t.index(el) + 1} число: {el}')
    print(sum(t))


# Код задания базового уровня
def basic_level():
    result = 0
    first_list = input('Введите числа в первый список через пробел: ').split()
    second_list = input('Введите числа в второй список через пробел: ').split()
    for el in first_list:
        if el in second_list:
            result += 1
    print(f'Количество пересечений: {result}')

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

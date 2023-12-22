def beginner_level():
    my_dict = {}
    my_dict['name'], my_dict['age'], my_dict['city'] = 'Jonh', 25, 'New York'
    print('\n', my_dict)
    my_dict['age'] = 26
    my_dict['email'] = 'jonh@example.com'
    del my_dict['city']
    for el in my_dict.keys():
        print(f'Ключ: {el}, Значение: {my_dict[el]}')


def basic_level():
    my_dict = {}
    my_dict['name'], my_dict['age'], my_dict['city'] = 'Jonh', 25, 'New York'
    print('\n', my_dict)
    my_dict['age'] = 26
    my_dict['email'] = 'jonh@example.com'
    for el in my_dict.keys():
        if el == 'country':
            print('В словаре есть ключ "country"')
        else:
            print('В словари нету ключа "country"')
        print(f'Ключ: {el}, Значение: {my_dict[el]}')

while True:
    select_level = input('\nВыберите уровень (Введите число с нужным вам уровнем): \n'
                         '"1": Начальный уровень \n'
                         '"2": Базовый уровень \n'
                         'Ввод: ')
    if select_level == '1':
        beginner_level()
    elif select_level == '2':
        basic_level()
    else:
        print('\nОшибка! Выберите уровень: \n'
              '"1": Начальный уровень \n'
              '"2": Базовый уровень \n'
              'Ввод: ')
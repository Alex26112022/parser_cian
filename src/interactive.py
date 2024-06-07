import cianparser


def interactive_func():
    """ Взаимодействие с клиентом. """
    all_cities = []
    for item in cianparser.list_locations():
        all_cities.append(item[0])

    dict_of_type = {'1': 'new', '2': 'secondary'}

    while True:
        city = input('Введите город!\n').title()
        if city not in all_cities:
            print('Данного города нет в базе!!!')
            continue

        print('Выберите тип жилья\n'
              '\t1. Новостройка\n'
              '\t2. Вторичка\n')
        object_type = input()
        if object_type not in ['1', '2']:
            print('Некорректные данные!!!')
            continue
        else:
            object_type = dict_of_type.get(object_type)

        room = 'all'
        room_ = input('Введите количество комнат (1-5) или нажмите ENTER для '
                      'пропуска!\n')
        if room_ in ['1', '2', '3', '4', '5']:
            room = int(room_)

        min_price = 0
        min_price_ = input('Введите минимальную стоимость или нажмите '
                           'ENTER!\n')
        if min_price_.isdigit() and int(min_price_) >= 0:
            min_price = int(min_price_)

        max_price = 1000000000
        max_price_ = input('Введите максимальную стоимость или нажмите '
                           'ENTER!\n')
        if max_price_.isdigit() and int(max_price_) >= 0:
            max_price = int(max_price_)

        min_floor = 1
        min_floor_ = input('Введите минимальный этаж или нажмите ENTER!\n')
        if min_floor_.isdigit() and int(min_floor_) >= 0:
            min_floor = int(min_floor_)

        max_floor = 1000
        max_floor_ = input('Введите максимальный этаж или нажмите ENTER!\n')
        if max_floor_.isdigit() and int(max_floor_) >= 0:
            max_floor = int(max_floor_)

        min_total_floor = 1
        min_total_floor_ = input('Введите минимальное количество этажей в '
                                 'доме или нажмите ENTER!\n')
        if min_total_floor_.isdigit() and int(min_total_floor_) >= 0:
            min_total_floor = int(min_total_floor_)

        max_total_floor = 1000
        max_total_floor_ = input('Введите максимальное количество этажей в '
                                 'доме или нажмите ENTER!\n')
        if max_total_floor_.isdigit() and int(max_total_floor_) >= 0:
            max_total_floor = int(max_total_floor_)

        return (city, room, object_type, min_price, max_price, min_floor,
                max_floor, min_total_floor, max_total_floor)


if __name__ == '__main__':
    print(cianparser.list_locations())

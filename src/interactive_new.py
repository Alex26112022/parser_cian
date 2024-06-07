import json

from config import region_path


def interactive_new_func():
    """ Взаимодействие с клиентом. """
    with open(region_path, encoding='utf-8') as file:
        data_regions = json.load(file)

    decorations = {'1': 'fineWithFurniture', '2': 'fine', '3': 'preFine',
                   '4': 'without'}

    print('Выберите критерии поиска. Для пропуска элемента оставьте поле '
          'пустым и нажмите ENTER!\n')

    region = input('Введите регион поиска...\n').capitalize()
    region = data_regions.get(region)

    rooms = input('Введите количество комнат...\n')
    if rooms not in ['1', '2', '3', '4', '5']:
        rooms = None

    min_floor = input('Введите минимальный этаж...\n')
    if not min_floor.isdigit() or int(min_floor) <= 0:
        min_floor = None

    max_floor = input('Введите максимальный этаж...\n')
    if not max_floor.isdigit() or int(max_floor) <= 0:
        max_floor = None

    min_price = input('Введите минимальную стоимость...\n')
    if not min_price.isdigit() or int(min_price) <= 0:
        min_price = None

    max_price = input('Введите максимальную стоимость...\n')
    if not max_price.isdigit() or int(max_price) <= 0:
        max_price = None

    min_area = input('Введите минимальную площадь...\n')
    if not min_area.isdigit() or int(min_area) <= 0:
        min_area = None

    max_area = input('Введите максимальную площадь...\n')
    if not max_area.isdigit() or int(max_area) <= 0:
        max_area = None

    decoration = input('Выберите вариант отделки квартиры...\n'
                       '\t1. Чистовая с мебелью\n'
                       '\t2. Чистовая\n'
                       '\t3. Предчистовая\n'
                       '\t4. Без отделки\n')
    decoration = decorations.get(decoration)

    material_house = input('Введите материал дома...\n'
                           '\t1. Кирпичный\n'
                           '\t2. Монолитный\n'
                           '\t3. Панельный\n')
    if material_house not in ['1', '2', '3']:
        material_house = None

    full_data = (decoration, material_house, max_floor, max_price, max_area,
                 min_floor, min_price, min_area, region, rooms)

    return full_data


if __name__ == '__main__':
    interactive_new_func()

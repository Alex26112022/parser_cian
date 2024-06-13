import pytest


@pytest.fixture()
def return_test_list_json():
    """ Возвращает список словарей. """
    test_list_json = [
        {
            "author": "ID 12963175",
            "author_type": "official_representative",
            "url": "https://www.cian.ru/sale/flat/279995862/",
            "location": "Москва",
            "deal_type": "sale",
            "accommodation_type": "flat",
            "floor": 2,
            "floors_count": 16,
            "rooms_count": 1,
            "total_meters": 20.0,
            "price_per_month": -1,
            "commissions": 0,
            "price": 6700000,
            "district": "Отрадное",
            "street": "Алтуфьевское шоссе",
            "house_number": "2",
            "underground": "Владыкино",
            "residential_complex": ""
        },
        {
            "author": "БЕСТ-Недвижимость на Баррикадной",
            "author_type": "real_estate_agent",
            "url": "https://www.cian.ru/sale/flat/279800832/",
            "location": "Москва",
            "deal_type": "sale",
            "accommodation_type": "flat",
            "floor": 1,
            "floors_count": 9,
            "rooms_count": 1,
            "total_meters": 30.0,
            "price_per_month": -1,
            "commissions": 0,
            "price": 6370000,
            "district": "Люблино",
            "street": " Верхние Поля",
            "house_number": "27С2",
            "underground": "Братиславская",
            "residential_complex": ""
        }]
    return test_list_json


@pytest.fixture()
def return_new_test_list_json():
    """ Возвращает список словарей. """
    new_dict = [{'Id': 1,
                 'address': 'value5',
                 'area': 'value2',
                 'card_url': 'value11',
                 'date_of_finish': 'value7',
                 'description': 'value8',
                 'developer': 'value10',
                 'floor': 'value3',
                 'price': 'value4',
                 'residence': 'value6',
                 'room': 'value1',
                 'type_of_developer': 'value9'},
                {'Id': 2,
                 'address': 'value55',
                 'area': 'value22',
                 'card_url': 'value110',
                 'date_of_finish': 'value77',
                 'description': 'value88',
                 'developer': 'value100',
                 'floor': 'value33',
                 'price': 'value44',
                 'residence': 'value66',
                 'room': 'value11',
                 'type_of_developer': 'value99'}]

    return new_dict


@pytest.fixture()
def return_new_format() -> list[tuple]:
    """ Возвращает список кортежей данных по новостройкам. """
    list_format = [(1, 'value1', 'value2', 'value3', 'value4', 'value5',
                    'value6', 'value7', 'value8', 'value9', 'value10',
                    'value11'),
                   (2, 'value11', 'value22', 'value33', 'value44', 'value55',
                    'value66', 'value77', 'value88', 'value99', 'value100',
                    'value110')]

    return list_format

import pytest


@pytest.fixture()
def return_test_list_json():
    """ Возвращает список словарей. """
    test_list_json = [{
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

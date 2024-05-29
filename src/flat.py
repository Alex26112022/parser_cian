class Flat:
    """ Класс объект-квартира. """
    __slots__ = ["author", "author_type", "url", "location",
                 "floor", "floors_count", "rooms_count",
                 "total_meters", "price", "district", "street",
                 "house_number", "underground", "residential_complex"]

    def __init__(self, author, author_type, url, location,
                 floor, floors_count, rooms_count,
                 total_meters, price, district, street,
                 house_number, underground, residential_complex):
        self.author = author
        self.author_type = author_type
        self.url = url
        self.location = location
        self.floor = floor
        self.floors_count = floors_count
        self.rooms_count = rooms_count
        self.total_meters = total_meters
        self.price = price
        self.district = district
        self.street = street
        self.house_number = house_number
        self.underground = underground
        self.residential_complex = residential_complex

    def __str__(self):
        return (f'Автор объявления: {self.author}\n'
                f'Тип продавца: {self.author_type}\n'
                f'URL: {self.url}\n'
                f'Локация: {self.location.title()}, {self.district}'
                f',{self.street}, '
                f'{self.house_number}\n'
                f'Станция метро: {self.underground}\n'
                f'Жилой комплекс: {self.residential_complex}\n'
                f'Этаж: {self.floor}\n'
                f'Всего этажей в доме: {self.floors_count}\n'
                f'Количество комнат: {self.rooms_count}\n'
                f'Общая площадь: {self.total_meters} кв.м.\n'
                f'Стоимость: {self.price} руб.\n')

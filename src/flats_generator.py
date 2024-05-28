from src.flat import Flat


class FlatsGenerator:
    """ Генерирует список объектов Flats. """

    def __init__(self, list_json: list[dict]):
        self.list_json = list_json
        self.all_flats = []

    def generate_objects(self):
        for flat in self.list_json:
            author = flat.get('author')
            author_type = flat.get('author_type')
            url = flat.get('url')
            location = flat.get('location')
            accommodation_type = flat.get('accommodation_type')
            floor = flat.get('floor')
            floors_count = flat.get('floors_count')
            rooms_count = flat.get('rooms_count')
            total_meters = flat.get('total_meters')
            price = flat.get('price')
            district = flat.get('district')
            street = flat.get('street')
            house_number = flat.get('house_number')
            underground = flat.get('underground')
            residential_complex = flat.get('residential_complex')

            self.all_flats.append(Flat(author, author_type, url, location,
                                       accommodation_type, floor,
                                       floors_count, rooms_count,
                                       total_meters, price, district,
                                       street, house_number, underground,
                                       residential_complex))

    def get_all_flats(self):
        """ Возвращает список объектов. """
        return self.all_flats

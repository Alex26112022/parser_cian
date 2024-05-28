import cianparser


class ParserCian:
    """ Класс-парсер. """
    __proxies = [
        '117.250.3.58:8080',
        '115.96.208.124:8080',
        '152.67.0.109:80',
        '45.87.68.2:15321',
        '68.178.170.59:80',
        '20.235.104.105:3729',
        '195.201.34.206:80',
    ]

    def __init__(self, city: str):
        self.city = city
        self.my_parser = cianparser.CianParser(location=self.city,
                                               proxies=None)

    def get_search_flats(self, rooms='all', object_type='new', min_price=0,
                         max_price=1000000000, min_floor=1, max_floor=1000,
                         min_total_floor=1, max_total_floor=1000,
                         house_material_type=1, flat_share=2,
                         only_flat=True, only_apartment=False, sort_by="creation_data_from_newer_to_older"):
        """ Парсит готовые квартиры. """
        add_settings = {"start_page": 1, "end_page": 2,
                        "object_type": object_type,
                        "min_price": min_price, "max_price": max_price,
                        "min_floor": min_floor, "max_floor": max_floor,
                        "min_total_floor": min_total_floor,
                        "max_total_floor": max_total_floor,
                        "house_material_type": house_material_type,
                        "flat_share": flat_share, "only_flat": only_flat,
                        "only_apartment": only_apartment,
                        "sort_by": sort_by}
        data = self.my_parser.get_flats(deal_type="sale", rooms=rooms,
                                        additional_settings=add_settings)
        return data

    def get_search_new_flats(self):
        """ Парсит строящиеся объекты. """
        data = self.my_parser.get_newobjects()
        return data

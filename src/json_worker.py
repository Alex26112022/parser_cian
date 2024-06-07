import json


class JsonWorker:
    """ Класс взаимодействия с json-файлом. """

    def __init__(self, cian_path: str, cian_new_path: str):
        self.__flats_info = None
        self.__flats_info_new = None
        self.__cian_path = cian_path
        self.__cian_new_path = cian_new_path

    def write_json_flats(self, list_flats: list[dict]):
        """ Записывает данные о квартирах в json. """
        with open(self.__cian_path, 'w', encoding='utf-8') as file1:
            json.dump(list_flats, file1, ensure_ascii=False, indent=4)

    def write_json_flats_new(self, list_new_flats: list[dict]):
        """ Записывает данные о новостройках в json. """
        with open(self.__cian_new_path, 'w', encoding='utf-8') as file2:
            json.dump(list_new_flats, file2, ensure_ascii=False, indent=4)

    def read_json_flats(self):
        """ Считывает данные о квартирах с json. """
        with open(self.__cian_path, encoding='utf-8') as file3:
            self.__flats_info = json.load(file3)

    def read_json_flats_new(self):
        """ Считывает данные о новостройках с json. """
        with open(self.__cian_new_path, encoding='utf-8') as file4:
            self.__flats_info_new = json.load(file4)

    def get_flats_info(self) -> list[dict]:
        """ Возвращает данные о квартирах. """
        return self.__flats_info

    def get_flats_info_new(self) -> list[dict]:
        """ Возвращает данные о новостройках. """
        return self.__flats_info_new

    def get_new_flats_format(self) -> list[tuple]:
        """ Возвращает список кортежей данных по новостройкам. """
        new_flats_info = []
        for el in self.__flats_info_new:
            id_ = el.get('Id')
            room = el.get('room')
            area = el.get('area')
            floor = el.get('floor')
            price = el.get('price')
            address = el.get('address')
            residence = el.get('residence')
            date_of_finish = el.get('date_of_finish')
            description = el.get('description')
            type_of_developer = el.get('type_of_developer')
            developer = el.get('developer')
            card_url = el.get('card_url')
            full_info = (id_, room, area, floor, price, address, residence,
                         date_of_finish, description, type_of_developer,
                         developer, card_url)
            new_flats_info.append(full_info)

        return new_flats_info



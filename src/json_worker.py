import json


class JsonWorker:
    """ Класс взаимодействия с json-файлом. """
    def __init__(self, cian_path: str, cian_new_path: str):
        self.__flats_info = None
        self.__cian_path = cian_path
        self.__cian_new_path = cian_new_path

    def write_json_flats(self, list_flats: list[dict]):
        """ Записывает данные о квартирах в json. """
        with open(self.__cian_path, 'w', encoding='utf-8') as file:
            json.dump(list_flats, file, ensure_ascii=False, indent=4)

    def write_json_flats_new(self, list_new_flats: list[dict]):
        """ Записывает данные о новостройках в json. """
        with open(self.__cian_new_path, 'w', encoding='utf-8') as file:
            json.dump(list_new_flats, file, ensure_ascii=False, indent=4)

    def read_json_flats(self):
        """ Считывает данные о квартирах с json. """
        with open(self.__cian_path, encoding='utf-8') as file_:
            self.__flats_info = json.load(file_)

    def get_flats_info(self) -> list[dict]:
        """ Возвращает данные о квартирах. """
        return self.__flats_info

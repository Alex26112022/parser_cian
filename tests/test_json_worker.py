from config import cian_path_test, cian_path_new_test
from src.json_worker import JsonWorker

test_list_dict = [{'key1': 'value1'}, {'key2': 'value2'}]
new_worker = JsonWorker(cian_path_test, cian_path_new_test)


def test_write_json_flats():
    """ Записывает тестовый список словарей в тестовый json. """
    new_worker.write_json_flats(test_list_dict)


def test_read_json_flats():
    """ Проверяет чтение данных с json. """
    new_worker.read_json_flats()
    assert new_worker.get_flats_info() == [{'key1': 'value1'},
                                           {'key2': 'value2'}]


def test_write_json_flats_new(return_new_test_list_json):
    """ Записывает тестовый список словарей в тестовый json. """
    new_worker.write_json_flats_new(return_new_test_list_json)


def test_read_json_flats_new(return_new_test_list_json, return_new_format):
    """ Проверяет чтение данных с json. """
    new_worker.read_json_flats_new()
    assert new_worker.get_flats_info_new() == return_new_test_list_json
    assert new_worker.get_new_flats_format() == return_new_format

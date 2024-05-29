from src.parser_cian import ParserCian

new_search = ParserCian('москва')


def mock_get(*args):
    """ Подменяет функцию get_search_flats. """
    return [{'key1': 'value1'}, {'key2': 'value2'}]


def test_get_search_flats(monkeypatch):
    """ Тест парсера. """
    monkeypatch.setattr('src.parser_cian.ParserCian.get_search_flats',
                        mock_get)
    assert new_search.get_search_flats() == [{'key1': 'value1'},
                                             {'key2': 'value2'}]

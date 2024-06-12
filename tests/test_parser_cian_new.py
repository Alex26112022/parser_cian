from src.parser_cian_new import ParserCianNew

values1 = ('value1', 'value2', 'value3', 'value4', 'value5',
           'value6', 'value7', 'value8', 'value9', 'value10', 'value11')

values2 = ('value11', 'value22', 'value33', 'value44', 'value55',
           'value66', 'value77', 'value88', 'value99', 'value100', 'value110')

new_search = ParserCianNew(*values1[:-1])


def new_mock_get(*args):
    """ Подменяет функцию get_response. """
    new_search.info.append(values1)
    new_search.info.append(values2)


def test_get_search_new_flats(monkeypatch, return_new_test_list_json):
    """ Тест парсера. """
    monkeypatch.setattr('src.parser_cian_new.ParserCianNew.get_response',
                        new_mock_get)
    assert new_search.get_info_cards() == []
    new_search.get_response()
    assert new_search.get_info_cards() == [values1, values2]
    assert new_search.info_cards_format_json() == return_new_test_list_json

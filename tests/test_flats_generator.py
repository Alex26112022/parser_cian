from src.flats_generator import FlatsGenerator


def test_generate_objects(return_test_list_json):
    """ Проверяет генерацию объектов. """
    new_generator = FlatsGenerator(return_test_list_json)
    new_generator.generate_objects()
    res = new_generator.get_all_flats()
    assert len(res) == 2
    assert res[0].author == 'ID 12963175'
    assert res[1].price == 6370000

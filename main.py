from config import cian_path
from src.flats_generator import FlatsGenerator
from src.json_worker import JsonWorker
from src.parser_cian import ParserCian

# new_search = ParserCian('москва')
# flats = new_search.get_search_flats(rooms=1, object_type='secondary',
#                                     min_price=1000000, max_price=8000000,
#                                     house_material_type=3)
json_worker = JsonWorker(cian_path)
# json_worker.write_json_flats(flats)
json_worker.read_json_flats()
info = json_worker.get_flats_info()
new_list_flats = FlatsGenerator(info)
new_list_flats.generate_objects()
list_result = new_list_flats.get_all_flats()

print(len(list_result))
for el in list_result:
    print(el, '\n')


if __name__ == '__main__':
    pass

    # for el in flats:
    #     print(el, '\n')

    # new_flats = new_search.get_search_new_flats()
    # for item in new_flats:
    #     print(item, '\n')

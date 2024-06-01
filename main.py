from config import cian_path
from src.db_create import DbCreate
from src.db_insert import DbInsert
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

new_database = DbCreate()
new_database.create_drop_db()
new_database.create_table()

new_insert = DbInsert(new_database.engine)
new_insert.insert_flats(list_result)

if __name__ == '__main__':
    pass

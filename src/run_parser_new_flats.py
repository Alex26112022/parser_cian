from config import cian_path, cian_new_path
from src.db_create import DbCreate
from src.db_insert import DbInsert
from src.flats_generator import FlatsGenerator
from src.interactive_new import interactive_new_func
from src.json_worker import JsonWorker
from src.parser_cian_new import ParserCianNew

input_data = interactive_new_func()

new_pars = ParserCianNew(*input_data)
new_pars.get_response()
new_flats_json = new_pars.info_cards_format_json()

new_worker_json = JsonWorker(cian_path, cian_new_path)
new_worker_json.write_json_flats_new(new_flats_json)
new_worker_json.read_json_flats()
new_worker_json.read_json_flats_new()

new_flats_result = new_worker_json.get_new_flats_format()

info_flats = new_worker_json.get_flats_info()
list_flats = FlatsGenerator(info_flats)
list_flats.generate_objects()
flats_result = list_flats.get_all_flats()

new_database = DbCreate()
new_database.create_drop_db()
new_database.create_table()

new_insert = DbInsert(new_database.engine)
new_insert.insert_flats(flats_result)
new_insert.insert_flats_new(new_flats_result)

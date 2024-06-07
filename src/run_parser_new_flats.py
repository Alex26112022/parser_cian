from config import cian_path, cian_new_path
from src.json_worker import JsonWorker
from src.parser_cian_new import ParserCianNew

new_pars = ParserCianNew()
new_pars.get_response()
new_flats_json = new_pars.info_cards_format_json()

new_worker_json = JsonWorker(cian_path, cian_new_path)
new_worker_json.write_json_flats_new(new_flats_json)

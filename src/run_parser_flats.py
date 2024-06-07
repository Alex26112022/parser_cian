from config import cian_path
from src.db_create import DbCreate
from src.db_insert import DbInsert
from src.flats_generator import FlatsGenerator
from src.interactive import interactive_func
from src.json_worker import JsonWorker
from src.parser_cian import ParserCian


def run_parser():
    """ Запускает главный цикл парсера готового жилья. """
    input_data = interactive_func()
    print(input_data)

    new_search = ParserCian(input_data[0])
    flats = new_search.get_search_flats(rooms=input_data[1],
                                        object_type=input_data[2],
                                        min_price=input_data[3],
                                        max_price=input_data[4],
                                        min_floor=input_data[5],
                                        max_floor=input_data[6],
                                        min_total_floor=input_data[7],
                                        max_total_floor=input_data[8])

    json_worker = JsonWorker(cian_path)
    json_worker.write_json_flats(flats)
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
    run_parser()

from src.run_parser_flats import run_parser
from src.run_parser_new_flats import run_parser_new


def main():
    """ Запуск программы. """
    parser_dict = {'1': run_parser, '2': run_parser_new}

    print('Выберите нужный парсер!\n'
          '\t1. Парсер готового жилья\n'
          '\t2. Парсер строящегося жилья')

    user_input = input()
    if user_input in ['1', '2']:
        parser_dict.get(user_input)()
    else:
        print('Некорректный ввод!')


if __name__ == '__main__':
    main()

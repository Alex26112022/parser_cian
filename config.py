import os
from dotenv import load_dotenv

ROOT_DIR = os.path.dirname(__file__)
cian_path = os.path.join(ROOT_DIR, 'src', 'cian.json')
cian_new_path = os.path.join(ROOT_DIR, 'src', 'cian_new.json')
region_path = os.path.join(ROOT_DIR, 'src', 'dict_regions.json')
cian_path_test = os.path.join(ROOT_DIR, 'tests', 'cian_test.json')
cian_path_new_test = os.path.join(ROOT_DIR, 'tests', 'cian_new_test.json')

load_dotenv()


class DbConfig:
    """ Класс-конфигуратор БД. """

    USER_NAME = os.getenv('USER_NAME')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')

    def settings_psycopg2(self):
        """ Настройки подключения к БД через psycopg2. """
        settings_dict = {
            'user': self.USER_NAME,
            'password': self.PASSWORD,
            'host': self.HOST,
            'port': self.PORT
        }
        return settings_dict

    def settings_sqlalchemy(self):
        """ Настройки подключения к БД через sqlalchemy. """
        return (f'postgresql+psycopg2://{self.USER_NAME}:{self.PASSWORD}@'
                f'{self.HOST}:{self.PORT}/')

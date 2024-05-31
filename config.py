import os
from dotenv import load_dotenv

ROOT_DIR = os.path.dirname(__file__)
cian_path = os.path.join(ROOT_DIR, 'src', 'cian.json')
cian_path_test = os.path.join(ROOT_DIR, 'tests', 'cian_test.json')

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


def settings_psycopg2():
    settings_dict = {
        'user': USER_NAME,
        'password': PASSWORD,
        'host': HOST,
        'port': PORT
    }
    return settings_dict


def settings_sqlalchemy():
    return f'postgresql+psycopg2://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/'

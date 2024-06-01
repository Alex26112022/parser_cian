import psycopg2
from sqlalchemy import create_engine

from config import DbConfig
from src.db_models import Base


class DbCreate:
    """ Класс, формирующий структуру БД, """

    my_config = DbConfig()  # Конфигурация подключения к БД.
    ps_conf = my_config.settings_psycopg2()
    alchemy_conf = my_config.settings_sqlalchemy()

    engine = create_engine(f'{alchemy_conf}cian_db', echo=True)

    def create_drop_db(self):
        """ Пересоздает БД. """
        conn = psycopg2.connect(dbname='postgres', **self.ps_conf)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute('DROP DATABASE IF EXISTS cian_db')
            cur.execute('CREATE DATABASE cian_db')
            conn.commit()
            conn.close()

    def create_table(self):
        """ Формирует таблицы. """
        Base.metadata.create_all(self.engine)

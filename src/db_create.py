import psycopg2
from sqlalchemy import create_engine

from config import settings_sqlalchemy, settings_psycopg2
from src.db_models import Base

ps_conf = settings_psycopg2()
alchemy_conf = settings_sqlalchemy()

conn = psycopg2.connect(dbname='postgres', **ps_conf)
conn.autocommit = True
with conn.cursor() as cur:
    cur.execute('DROP DATABASE IF EXISTS cian_db')
    cur.execute('CREATE DATABASE cian_db')
    conn.commit()
    conn.close()

engine = create_engine(f'{alchemy_conf}cian_db', echo=True)

Base.metadata.create_all(engine)

# with engine.connect() as conn:
#     res = conn.execute(text("SELECT * FROM currency"))
#     for el in res.all():
#         print(el)
# conn.commit()

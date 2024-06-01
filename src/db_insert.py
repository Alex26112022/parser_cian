from sqlalchemy.orm import sessionmaker

from src.db_models import DbFlats
from src.flat import Flat


class DbInsert:
    """ Класс, заполняющий БД данными. """

    def __init__(self, engine):
        self.engine = engine

    def insert_flats(self, list_objects: list[Flat]):
        """ Заполняет таблицу flats. """
        new_session = sessionmaker(bind=self.engine)
        list_db = []

        for el in list_objects:
            list_db.append(
                DbFlats(author=el.author, author_type=el.author_type,
                        url=el.url, location=el.location,
                        floor=el.floor, floors_count=el.floors_count,
                        rooms_count=el.rooms_count,
                        total_meters=el.total_meters, price=el.price,
                        district=el.district, street=el.street,
                        house_number=el.house_number,
                        underground=el.underground,
                        residential_complex=el.residential_complex))

        with new_session() as session:
            session.add_all(list_db)
            session.commit()

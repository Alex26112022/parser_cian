from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class DbFlats(Base):
    __tablename__ = 'flats'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    author: Mapped[str | None]
    author_type: Mapped[str | None]
    url: Mapped[str | None]
    location: Mapped[str | None]
    floor: Mapped[int | None]
    floors_count: Mapped[int | None]
    rooms_count: Mapped[int | None]
    total_meters: Mapped[float | None]
    price: Mapped[float | None]
    district: Mapped[str | None]
    street: Mapped[str | None]
    house_number: Mapped[str | None]
    underground: Mapped[str | None]
    residential_complex: Mapped[str | None]

    def __repr__(self):
        return (f'Id: {self.id}\n'
                f'Автор объявления: {self.author}\n'
                f'Тип продавца: {self.author_type}\n'
                f'URL: {self.url}\n'
                f'Локация: {self.location.title()}, {self.district}'
                f',{self.street}, '
                f'{self.house_number}\n'
                f'Станция метро: {self.underground}\n'
                f'Жилой комплекс: {self.residential_complex}\n'
                f'Этаж: {self.floor}\n'
                f'Всего этажей в доме: {self.floors_count}\n'
                f'Количество комнат: {self.rooms_count}\n'
                f'Общая площадь: {self.total_meters} кв.м.\n'
                f'Стоимость: {self.price} руб.\n')


class DbFlatsNew(Base):
    __tablename__ = 'flats_new'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    room: Mapped[int | None]
    area: Mapped[float | None]
    floor: Mapped[str | None]
    price: Mapped[int | None]
    address: Mapped[str | None]
    residence: Mapped[str | None]
    date_of_finish: Mapped[str | None]
    type_of_developer: Mapped[str | None]
    developer: Mapped[str | None]
    card_url: Mapped[str | None]
    description: Mapped[str | None]

    def __repr__(self):
        return (f'Id: {self.id}\n'
                f'Количество комнат: {self.room}\n'
                f'Площадь: {self.area} кв.м.\n'
                f'Этаж: {self.floor}\n'
                f'Стоимость: {self.price} руб.\n'
                f'Адрес: {self.address}\n'
                f'Жилой комплекс: {self.residence}\n'
                f'Дата постройки: {self.date_of_finish}\n'
                f'Описание: {self.description}\n'
                f'Тип продавца: {self.type_of_developer}\n'
                f'Застройщик: {self.developer}\n'
                f'URL: {self.card_url}\n')

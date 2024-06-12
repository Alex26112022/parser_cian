import requests
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from fake_headers import Headers


# full_url = ('https://www.cian.ru/cat.php?currency=2&deal_type=sale&decorations_list%5B0%5D=without&engine_version=2&house_material%5B0%5D=2&maxfloor=10&maxprice=20000000&maxtarea=100&minfloor=2&minprice=5000000&mintarea=60&object_type%5B0%5D=2&offer_type=flat&only_flat=1&p=1&region=4593&room3=1')


class ParserCianNew:
    """ Класс-парсер строящегося жилья. """
    __url = 'https://www.cian.ru/cat.php'
    __headers = Headers(os="win", headers=True).generate()

    def __init__(self, decoration, house_material, maxfloor, maxprice,
                 maxtarea, minfloor, minprice, mintarea, region, room):
        if room is None:
            self.is_room = None
            self.room = 'room'
        else:
            self.is_room = '1'
            self.room = 'room' + room
        self.info = []
        self.params = {'currency': '2', 'deal_type': 'sale',
                       'decorations_list%5B0%5D': decoration,
                       'engine_version': '2',
                       'house_material%5B0%5D': house_material,
                       'maxfloor': maxfloor, 'maxprice': maxprice,
                       'maxtarea': maxtarea, 'minfloor': minfloor,
                       'minprice': minprice, 'mintarea': mintarea,
                       'object_type%5B0%5D': '2', 'offer_type': 'flat',
                       'only_flat': '1', 'p': 0, 'region': region,
                       self.room: self.is_room}

    def get_response(self):
        while True:
            try:
                self.params['p'] += 1
                print(f'Страница... {self.params['p']}')
                response = requests.get(self.__url, headers=self.__headers,
                                        params=self.params)

                soup = BeautifulSoup(response.text, 'lxml')

                div_cards = soup.find_all('article',
                                          class_='_93444fe79c--container--Povoi '
                                                 '_93444fe79c--cont--OzgVc')
                print(len(div_cards))

                for card in div_cards:
                    header_card = card.find('a',
                                            class_='_93444fe79c--link--VtWj6')
                    card_title = header_card.find('span').find(
                        'span').text.split()
                    room = int(card_title[0][0])
                    area = float(card_title[2].replace(',', '.'))
                    floor = card_title[-2]
                    card_url = header_card.get('href')

                    residence = card.find('a',
                                          class_='_93444fe79c--jk--dIktL').text

                    date_of_finish = card.find('span',
                                               class_='_93444fe79c--color_gray60_100--mYFjS '
                                                      '_93444fe79c--lineHeight_20px--fX7_V '
                                                      '_93444fe79c--fontWeight_normal--JEG_c '
                                                      '_93444fe79c--fontSize_14px--reQMB '
                                                      '_93444fe79c--display_inline--ySCqY '
                                                      '_93444fe79c--text--e4SBY '
                                                      '_93444fe79c--text_letterSpacing__normal--tfToq').text

                    address_ifo = card.find_all('a',
                                                class_='_93444fe79c--link--NQlVc')
                    address = ''

                    for el in address_ifo:
                        address += f'{el.text}. '

                    price = card.find('span', {'data-mark': 'MainPrice'})
                    price = int(price.find('span').text[:-1].replace(' ', ''))

                    description = card.find('p',
                                            class_='_93444fe79c--color_black_100--Ephi7 '
                                                   '_93444fe79c--lineHeight_20px--fX7_V '
                                                   '_93444fe79c--fontWeight_normal--JEG_c '
                                                   '_93444fe79c--fontSize_14px--reQMB '
                                                   '_93444fe79c--display_block--KYb25 '
                                                   '_93444fe79c--text--e4SBY '
                                                   '_93444fe79c--text_letterSpacing__normal--tfToq').text.replace(
                        '\n', '')

                    type_of_developer = card.find('span',
                                                  class_='_93444fe79c--color_gray60_100--mYFjS '
                                                         '_93444fe79c--lineHeight_4u--E1SPG '
                                                         '_93444fe79c--fontWeight_bold--BbhnX '
                                                         '_93444fe79c--fontSize_10px--c1NGZ '
                                                         '_93444fe79c--display_block--KYb25 '
                                                         '_93444fe79c--text--e4SBY '
                                                         '_93444fe79c--text_textTransform__uppercase--JygPH').text

                    developer = card.find('span',
                                          class_='_93444fe79c--color_current_color--vhuGI '
                                                 '_93444fe79c--lineHeight_6u--cedXD '
                                                 '_93444fe79c--fontWeight_bold--BbhnX '
                                                 '_93444fe79c--fontSize_16px--QNYmt '
                                                 '_93444fe79c--display_block--KYb25 '
                                                 '_93444fe79c--text--e4SBY').text

                    full_data = (room, area, floor, price, address, residence,
                                 date_of_finish, description,
                                 type_of_developer,
                                 developer, card_url)

                    if full_data not in self.info:
                        self.info.append(full_data)
                    else:
                        return

                sleep(randint(1, 3))
            except:  # noqa
                return

    def get_info_cards(self) -> list[tuple]:
        """ Возвращает список кортежей данных по объявлениям. """
        return self.info

    def info_cards_format_json(self) -> list[dict]:
        """ Форматирует данные в список словарей. """
        info_json = []
        for num_, card in enumerate(self.info):
            new_dict = dict()
            new_dict['Id'] = num_ + 1
            new_dict['room'] = card[0]
            new_dict['area'] = card[1]
            new_dict['floor'] = card[2]
            new_dict['price'] = card[3]
            new_dict['address'] = card[4]
            new_dict['residence'] = card[5]
            new_dict['date_of_finish'] = card[6]
            new_dict['description'] = card[7]
            new_dict['type_of_developer'] = card[8]
            new_dict['developer'] = card[9]
            new_dict['card_url'] = card[10]
            info_json.append(new_dict)

        return info_json

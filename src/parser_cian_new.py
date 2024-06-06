import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


# full_url = ('https://www.cian.ru/cat.php?currency=2&deal_type=sale&decorations_list%5B0%5D=without&engine_version=2&house_material%5B0%5D=2&maxfloor=10&maxprice=20000000&maxtarea=100&minfloor=2&minprice=5000000&mintarea=60&object_type%5B0%5D=2&offer_type=flat&only_flat=1&p=1&region=4593&room3=1')


class ParserCianNew:
    """ Класс-парсер строящегося жилья. """
    __url = 'https://www.cian.ru/cat.php'
    __headers = Headers(os="win", headers=True).generate()

    def __init__(self):
        self.params = {'currency': '2', 'deal_type': 'sale',
                       'decorations_list%5B0%5D': 'without',
                       'engine_version': '2', 'house_material%5B0%5D': '2',
                       'maxfloor': '10', 'maxprice': '20000000',
                       'maxtarea': '100', 'minfloor': '2',
                       'minprice': '5000000', 'mintarea': '60',
                       'object_type%5B0%5D': '2', 'offer_type': 'flat',
                       'only_flat': '1', 'p': '1', 'region': '4593',
                       'room3': '1'}

    def get_response(self):
        response = requests.get(self.__url, headers=self.__headers,
                                params=self.params)

        soup = BeautifulSoup(response.text, 'lxml')

        div_cards = soup.find_all('div',
                                  class_='_93444fe79c--card--ibP42 _93444fe79c--wide--gEKNN')
        for card in div_cards:
            header_card = card.find('a', class_='_93444fe79c--link--VtWj6')
            card_title = header_card.find('span').find('span').text.split()

            room = int(card_title[0][0])
            area = float(card_title[2].replace(',', '.'))
            floor = card_title[-2]
            card_url = header_card.get('href')

            complex_ = card.find('a', class_='_93444fe79c--jk--dIktL').text

            date_of_finish = card.find('span',
                                       class_='_93444fe79c--color_gray60_100--mYFjS '
                                              '_93444fe79c--lineHeight_20px--fX7_V '
                                              '_93444fe79c--fontWeight_normal--JEG_c '
                                              '_93444fe79c--fontSize_14px--reQMB '
                                              '_93444fe79c--display_inline--ySCqY '
                                              '_93444fe79c--text--e4SBY '
                                              '_93444fe79c--text_letterSpacing__normal--tfToq').text

            address_ifo = card.find_all('a', class_='_93444fe79c--link--NQlVc')
            address = ''

            for el in address_ifo:
                address += f'{el.text}. '

            price = card.find('span',
                              class_='_93444fe79c--color_black_100--Ephi7 '
                                     '_93444fe79c--lineHeight_28px--KFXmc '
                                     '_93444fe79c--fontWeight_bold--BbhnX '
                                     '_93444fe79c--fontSize_22px--sFuaL '
                                     '_93444fe79c--display_block--KYb25 '
                                     '_93444fe79c--text--e4SBY '
                                     '_93444fe79c--text_letterSpacing__normal--tfToq')
            price = int(price.find('span').text[:-1].replace(' ', ''))

            description = card.find('p',
                                    class_='_93444fe79c--color_black_100--Ephi7 '
                                           '_93444fe79c--lineHeight_20px--fX7_V '
                                           '_93444fe79c--fontWeight_normal--JEG_c '
                                           '_93444fe79c--fontSize_14px--reQMB '
                                           '_93444fe79c--display_block--KYb25 '
                                           '_93444fe79c--text--e4SBY '
                                           '_93444fe79c--text_letterSpacing__normal--tfToq').text

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

            print(developer)

        # a_cards = soup.find_all('a', class_='_93444fe79c--link--VtWj6')
        # total_cards = soup.find('h5').text.split()[1]
        # total_pages = int(total_cards)//28
        #
        # print(total_cards)
        # print(total_pages)
        #
        # for el in a_cards:
        #     print(el.get('href'))


new_pars = ParserCianNew()
new_pars.get_response()

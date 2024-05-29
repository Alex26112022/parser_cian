from src.flat import Flat

params_init = ['param1', 'param2', 'param3', 'param4', 'param5', 'param6',
               'param7', 'param8', 'param9', 'param10', 'param11', 'param12',
               'param13', 'param14', ]

new_flat = Flat(*params_init)


def test_flat():
    """ Проверяет инициализацию класса. """
    print(new_flat)

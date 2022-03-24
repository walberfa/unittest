from datetime import datetime
from is_weekend import Calendario
import unittest
from unittest.mock import Mock
import requests


sabado = datetime(year=2022, month=3, day=26)
quinta = datetime(year=2022, month=3, day=24)
datetime = Mock()


class TestCalendario(unittest.TestCase):
    def test_saturday_is_weekend(self):

        datetime.today.return_value = sabado
        test_calendario = Calendario(datetime)
        assert test_calendario.is_weekend()

    def test_thursday_is_weekend(self):

        datetime.today.return_value = quinta
        test_calendario = Calendario(datetime)
        assert not test_calendario.is_weekend()


if __name__ == '__main__':
    unittest.main()

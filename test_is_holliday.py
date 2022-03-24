import unittest
from unittest.mock import Mock
import requests

requests = Mock()


def get_feriados(self):
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendario(unittest.TestCase):
    def fake_request(self, url):

        print(f'Fazendo request a {url}')
        print('Request recebido!')

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Natal",
            "07/09": "Independencia do Brasil",
            "03/06": "Aniversário de Maracanaú"
        }
        return response_mock

    def test_get_feriados(self):
        requests.get.side_effect = self.fake_request
        assert get_feriados(self)["03/06"] == "Aniversário de Maracanaú"


if __name__ == '__main__':
    unittest.main()

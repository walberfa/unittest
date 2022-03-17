import unittest
import calculadora
import login
import re


def set_up():
    print('set up test')


def tear_down():
    print('tear down test')


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # primeiro teste de assertEqual
        self.assertEqual('teste'.upper(), 'TESTE')

    def test_lower(self):
        # primeiro teste de assertNotEqual
        self.assertNotEqual('teste'.lower(), 'TESTE')

    def test_isupper(self):
        # teste de assertTrue e assertFalse
        self.assertTrue('TESTE'.isupper())
        self.assertFalse('Teste'.isupper())

    def test_is(self):
        a = "a"
        b = "abc"
        self.assertIs(a, a)
        self.assertIsNot(a, b)


class TestCalculadora(unittest.TestCase):

    def test_adicao(self):
        # Soma com dois números positivos
        self.assertEqual(calculadora.adicao(13, 13), 26)
        # Soma com dois números negativos
        self.assertEqual(calculadora.adicao(-3, -6), -9)
        # Soma com um número positivo e um negativo
        self.assertEqual(calculadora.adicao(2, -1), 1)

    def test_subtracao(self):
        # Subtração com dois números positivos
        self.assertEqual(calculadora.subtracao(12, 6), 6)
        # Subtração com um número positivo e um negativo
        self.assertEqual(calculadora.subtracao(-2, 2), -4)
        # Subtração com um dois números negativos
        self.assertEqual(calculadora.subtracao(-3, -3), 0)

    def test_multiplicacao(self):
        # Multiplicação com zero
        self.assertEqual(calculadora.multiplicacao(0, 5), 0)
        # Multiplicação com número negativo e com 1
        self.assertEqual(calculadora.multiplicacao(-1, 6), -6)
        # Multiplicação com dois números negativos
        self.assertEqual(calculadora.multiplicacao(-2, -5), 10)

    def test_divisao(self):
        # Divisão com números positivos
        self.assertEqual(calculadora.divisao(10, 2), 5)
        # Divisão com número negativo e com 1
        self.assertEqual(calculadora.divisao(-3, 1), -3)
        # Divisão com resultado não inteiro
        self.assertEqual(calculadora.divisao(1, 2), 0.5)

    def test_divisao_por_zero(self):
        # Exceção para divisão com zero
        with self.assertRaises(ValueError):
            calculadora.divisao(2, 0)


class TestLogin(unittest.TestCase):

    def test_admin_login(self):
        # Testando a tupla do admin
        self.assertTupleEqual(login.usuarios[0], ('admin', 'admin123'))

    '''def test_nome_usario_sem_carac_especial(self):
        users = []
        for value in login.usuarios:
            users.append(value[0])
        # self.assertRegex()'''


if __name__ == '__main__':
    unittest.main()

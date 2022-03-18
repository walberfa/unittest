import unittest
import calculadora


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


if __name__ == '__main__':
    unittest.main()
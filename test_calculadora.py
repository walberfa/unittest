import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    """Teste para uma calculadora simples.
    """

    def test_adicao(self):
        """Testando a função soma.
        """
        with self.subTest("utilizando argumentos válidos"):
            self.assertEqual(calculadora.adicao(13, 13), 26)

        with self.subTest("forçando exceção inserindo parâmetro inválido"):
            with self.assertRaises(TypeError):
                self.assertEqual(calculadora.adicao(2, "a"), -4)

    def test_subtracao(self):
        """Testando a função subtração.
        """
        with self.subTest("utilizando argumentos válidos"):
            self.assertEqual(calculadora.subtracao(12, 6), 6)

        with self.subTest("forçando exceção inserindo parâmetro inválido"):
            with self.assertRaises(TypeError):
                self.assertEqual(calculadora.subtracao(-2, "2"), -4)

    def test_multiplicacao(self):
        """Testando a função multiplicação.
        """
        with self.subTest("utilizando argumentos onde um deles é zero"):
            self.assertEqual(calculadora.multiplicacao(0, 5), 0)

        with self.subTest("utilizando argumentos com número negativo"):
            self.assertEqual(calculadora.multiplicacao(-1, 6), -6)

    def test_divisao(self):
        """Testando a função subtração.
        """
        with self.subTest("utilizando argumentos válidos"):
            self.assertEqual(calculadora.divisao(10, 2), 5)

        with self.subTest("forçando exceção inserindo parâmetro inválido"):
            with self.assertRaises(TypeError):
                self.assertEqual(calculadora.divisao("1", 1), 1)

        with self.subTest("forçando uma exceção inserindo o zero no parâmetro y"):
            with self.assertRaises(ZeroDivisionError):
                calculadora.divisao(2, 0)


if __name__ == '__main__':
    unittest.main()
"""Calculadora simples com as quatro operações básicas.
"""


def adicao(x, y):
    """Calculo de adição.
    Args:
        x (float): Primeiro parâmetro da soma.
        y (float): Segundo parâmetro da soma.
    Return:
        Resultado da soma.
    """
    return x + y


def subtracao(x, y):
    """Calculo de subtração.
    Args:
        x (float): Primeiro parâmetro da subtração.
        y (float): Segundo parâmetro da subtração.
    Return:
        Resultado da subtração.
    """
    return x - y


def multiplicacao(x, y):
    """Calculo de multiplicação.
    Args:
        x (float): Primeiro parâmetro da multiplicação.
        y (float): Segundo parâmetro da multiplicação.
    Return:
        Resultado da multiplicação.
    """
    return x * y


def divisao(x, y):
    """Calculo de divisão.
    Args:
        x (float): Primeiro parâmetro da divisão.
        y (float): Segundo parâmetro da divisão. Tem que ser diferente de zero.
    Return:
        Resultado da divisão.
    """
    if y == 0:
        raise ZeroDivisionError("Não pode realizar divisão por zero")
    return x / y


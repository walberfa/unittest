
def adicao(x, y):
    # Calculo de adição
    return x + y


def subtracao(x, y):
    # Calculo de subtração
    return x - y


def multiplicacao(x, y):
    # Calculo de multiplicação
    return x * y


def divisao(x, y):
    # Calculo de divisão
    if y == 0:
        raise ValueError("Não pode realizar divisão por zero")
    return x / y


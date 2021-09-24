# 1 - imports - bibliotecas
import pytest

# 2 - class - classe

# 3 - definitions - definições = métodos e funções

def print_hi(name):

    print(f'Oi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Não dividirás por zero'

if __name__ == '__main__':
    print_hi('KarlaDaiany')

    # soma de 2 números
    resultado = somar(1,2)
    print(f'O resultado da soma é: {resultado}')

    #subtração de 2 números
    resultado = subtrair(5,3)
    print(f'O resultado da subtração é: {resultado}')

    #multiplicação de 2 números
    resultado = multiplicar(2,4)
    print(f'O resultado da multiplicação é: {resultado}')

    #divisão
    resultado = dividir(9,0)
    print(f'O resultado da divisão é: {resultado}')



# Testes unitários / Testes de Unidade

    #teste da função de somar
def test_somar_didatico():

    # 1 - Configura / Prepara (input - entrada | output - saída, resultado)
    num1 = 8
    num2 = 5
    resultado_esperado = 13

    # 2 - Executa
    resultado_atual = somar(num1,num2)

    # 3 - Check / Valida
    assert resultado_atual == resultado_esperado

def test_somar():
    assert somar(8,5) == 13

def test_subtrair():
    assert subtrair(4,5) == -1

def test_multiplicar():
    assert multiplicar(3,7) == 21

def test_dividir():
    assert dividir(8,4) == 2
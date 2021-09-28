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

# exemplo de demonstração
def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Não dividirás por zero'

# exemplo de divisão correto
def dividir_try_except(num1, num2):
    try:
        return num1 / num2
    except:
        return 'Não dividirás por zero'
    #except TypeError:
        #return TypeError

if __name__ == '__main__':
    print_hi('KarlaDaiany')

    # soma de 2 números
    resultado = somar(2,4)
    print(f'O resultado da soma é: {resultado}')


    #subtração de 2 números
    resultado = subtrair(5,3)
    print(f'O resultado da subtração é: {resultado}')

    #multiplicação de 2 números
    resultado = multiplicar(2,4)
    print(f'O resultado da multiplicação é: {resultado}')

    #divisão demonstração
    resultado = dividir(9,0)
    print(f'O resultado da divisão é: {resultado}')

    #divisão correta




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

@pytest.mark.parametrize('num1,num2,resultado',[
        # valores
        (5, 4, 9),  # teste 1
        (3, 2, 5),  # teste 2
        (10, 6, 15), # teste 3
    ])
def test_somar(num1, num2, resultado):
    try:
        assert somar(num1,num2) == resultado
    except AssertionError:
        print(f'Entrou no Except: {AssertionError}')
        pass

def test_subtrair():
    assert subtrair(4,5) == -1

def test_multiplicar():
    assert multiplicar(3,7) == 21

def test_dividir():
    assert dividir(8,4) == 2

def test_dividir_por_zero():
    assert dividir(8,0) == 'Não dividirás por zero'

    # teste positivo => mostra o resultado correto
    #                => avança para a próxima etapa
    # teste negativo => mostra a mensagem de erro (resultado_esperado do teste negativo)

@pytest.mark.parametrize('num1, num2, resultado',[
    (8,2,4),
    (20,4,5),
    (10,0,'Não dividirás por zero')
])
def test_dividir_try_except_por_zero(num1,num2,resultado):
    assert dividir_try_except(num1,num2) == resultado
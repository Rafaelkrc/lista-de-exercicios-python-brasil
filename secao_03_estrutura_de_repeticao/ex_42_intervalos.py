"""
Exercício 42 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-1, 10, 15, 20, 50, 13, 78, 22, 14, 16]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    7 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[14, -5, 10, 2, 80, 99]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    2 número(s) entre o intervalo de zero a 25
    2 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-55, 144, 5, 32, 18, 43, 12, 26, 76]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    3 número(s) entre o intervalo de zero a 25
    3 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[3, 5, 100, -5, 70, 88, 28, 12]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    1 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 51 a 75
    1 número(s) entre o intervalo de 76 a 100

"""


def listar_numeros_para_avaliacao():
    """Escreva aqui em baixo a sua solução"""
    num_ate_25 = num_ate_50 = num_ate_75 = num_ate_100 = 0
    while True:
        numeros = int(input('Informe um número positivo para continuar, ou um numero negativo para sair: '))
        if numeros < 0:
            break
        else:
            if numeros <= 25:
                num_ate_25 += 1
            if 25 < numeros <= 50:
                num_ate_50 += 1
            if 50 < numeros <= 75:
                num_ate_75 += 1
            if 75 < numeros <= 100:
                num_ate_100 += 1

    if num_ate_25 == 0:
        pass
    else:
        print(f'{num_ate_25} número(s) entre o intervalo de zero a 25')
    if num_ate_50 == 0:
        pass
    else:
        print(f'{num_ate_50} número(s) entre o intervalo de 26 a 50')
    if num_ate_75 == 0:
        pass
    else:
        print(f'{num_ate_75} número(s) entre o intervalo de 51 a 75')
    if num_ate_100 == 0:
        pass
    else:
        print(f'{num_ate_100} número(s) entre o intervalo de 76 a 100')

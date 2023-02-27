"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(saque: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    partes = 0
    nota100_str = nota50_str = nota10_str = nota5_str = nota1_str = ''
    nota_100, saque = divmod(saque, 100)
    if nota_100 > 1:
        nota100_str = f'{nota_100} notas de R$ 100'
        partes += 1
    elif nota_100 == 1:
        nota100_str = f'{nota_100} nota de R$ 100'
        partes += 1
    nota_50, saque = divmod(saque, 50)
    if nota_50 > 1:
        nota50_str = f'{nota_50} notas de R$ 50'
        partes += 1
    elif nota_50 == 1:
        nota50_str = f'{nota_50} nota de R$ 50'
        partes += 1
    nota_10, saque = divmod(saque, 10)
    if nota_10 > 1:
        nota10_str = f'{nota_10} notas de R$ 10'
        partes += 1
    elif nota_10 == 1:
        nota10_str = f'{nota_10} nota de R$ 10'
        partes += 1
    nota_5, nota_1 = divmod(saque, 5)
    if nota_5 > 1:
        nota5_str = f'{nota_5} notas de R$ 5'
        partes += 1
    elif nota_5 == 1:
        nota5_str = f'{nota_5} nota de R$ 5'
        partes += 1
    if nota_1 > 1:
        nota1_str = f'{nota_1} notas de R$ 1'
        partes += 1
    elif nota_1 == 1:
        nota1_str = f'{nota_1} nota de R$ 1'
        partes += 1

    if partes == 1:
        print(f"'{nota100_str + nota50_str + nota10_str + nota5_str + nota1_str}'")
    elif partes == 2:
        if nota100_str != '':
            segunda_parte = nota50_str + nota10_str + nota5_str + nota1_str
            if segunda_parte != '':
                print(f"'{nota100_str} e {segunda_parte}'")
        elif nota100_str == '' and nota50_str != '':
            segunda_parte = nota10_str + nota5_str + nota1_str
            if segunda_parte != '':
                print(f"'{nota50_str} e {segunda_parte}'")
        elif nota100_str == '' and nota50_str == '' and nota10_str != '':
            segunda_parte = nota5_str + nota1_str
            if segunda_parte != '':
                print(f"'{nota10_str} e {segunda_parte}'")
    elif partes > 2:
        if nota100_str and nota50_str and nota10_str and nota5_str and nota1_str != '':
            print(f"'{nota100_str}, {nota50_str}, {nota10_str}, {nota5_str} e {nota1_str}'")
        elif nota1_str == '':
            print(f"'{nota100_str}, {nota50_str}, {nota10_str} e {nota5_str}'")
        elif nota5_str == '':
            print(f"'{nota100_str}, {nota50_str}, {nota10_str} e {nota1_str}'")
        elif nota10_str == '':
            print(f"'{nota100_str}, {nota50_str}, {nota5_str} e {nota1_str}'")
        elif nota50_str == '':
            print(f"'{nota100_str}, {nota10_str}, {nota5_str} e {nota1_str}'")
        elif nota100_str == '':
            print(f"'{nota50_str}, {nota10_str}, {nota5_str} e {nota1_str}'")


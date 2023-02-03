"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""
import math


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""

    area = float(input('Informe a área a ser pintada em mt2: '))
    litro = round((area / 6) * 1.12)
    latas18 = math.ceil(litro / 18)
    valor18 = latas18 * 80
    sobra18 = math.ceil(latas18 * 18 - litro)
    latas3 = math.ceil(litro / 3.6)
    valor3 = latas3 * 25
    sobra3 = round(latas3 * 3.6 - litro, 1)
    mixlatas18 = math.trunc(litro / 18)
    mixlata3 = math.ceil((litro - (mixlatas18 * 18)) / 3.6)
    sobrat = round(mixlatas18 * 18 + mixlata3 * 3.6 - litro, 1)
    total_mix = (mixlatas18 * 80) + (mixlata3 * 25)

    print(f'Você deve comprar {litro} litros de tinta.')
    print(f'Você pode comprar {latas18} lata(s) de 18 litros a um custo de R$ {valor18}. Vão sobrar {sobra18:.1f} '
          f'litro(s) de tinta.')
    print(f'Você pode comprar {latas3} lata(s) de 3.6 litros a um custo de R$ {valor3}. Vão sobrar {sobra3:.1f} '
          f'litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {mixlatas18} lata(s) de 18 litros e {mixlata3} galão(ões) de 3.6 '
          f'litros a um custo de R$ {total_mix}. Vão sobrar {sobrat} litro(s) de tinta.')

"""
Exercício 33 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

Mostre a média com uma casa decimal.

    >>> calcular_estatisticas()
    'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    >>> calcular_estatisticas(1)
    'Maior temperatura: 1. Menor temperatura: 1. Média: 1.0'
    >>> calcular_estatisticas(1, 2)
    'Maior temperatura: 2. Menor temperatura: 1. Média: 1.5'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior temperatura: 2. Menor temperatura: -1. Média: 0.7'


"""


def calcular_estatisticas(*temperaturas) -> str:
    """Escreva aqui em baixo a sua solução"""
    todas_temperaturas = []
    for t in temperaturas:
        todas_temperaturas.append(t)
    if len(todas_temperaturas) == 0:
        print("'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'")
    else:
        media = sum(todas_temperaturas) / len(todas_temperaturas)
        print(f"'Maior temperatura: {max(todas_temperaturas)}. Menor temperatura: {min(todas_temperaturas)}. "
              f"Média: {media:.1f}'")

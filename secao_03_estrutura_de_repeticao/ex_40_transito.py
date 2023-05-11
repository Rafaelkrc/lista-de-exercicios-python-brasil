"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    maior_indice_acidentes = 0
    cidade_maior_indice = ''
    menor_indice_acidentes = 0
    cidade_menor_indice = ''
    soma_de_veiculos = 0
    cidades_menor_150_000 = []
    total_de_acidentes = 0
    for c, v, a in cidades:
        indice_acidentes = (a / v) * 1000
        soma_de_veiculos += v

        if indice_acidentes < menor_indice_acidentes or menor_indice_acidentes == 0:
            cidade_menor_indice = c
            menor_indice_acidentes = indice_acidentes

        if indice_acidentes > maior_indice_acidentes or maior_indice_acidentes == 0:
            cidade_maior_indice = c
            maior_indice_acidentes = indice_acidentes

        if v <= 150_000:
            total_de_acidentes += a
            cidades_menor_150_000.append(c)

    media_de_veiculos = soma_de_veiculos / len(cidades)
    media_de_acidentes = total_de_acidentes / len(cidades_menor_150_000)

    print(f'O maior índice de acidentes é de {cidade_maior_indice}, '
          f'com {maior_indice_acidentes:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {cidade_menor_indice}, '
          f'com {menor_indice_acidentes:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {media_de_veiculos:.0f}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_de_acidentes} acidentes.')

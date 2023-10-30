"""
Exercício 24 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

A partir de uma simulação de lançamento de dados, foram armazenados os valores de cada lançamento.
Mostre na tela:
1)Quantas vezes o dado foi lançado;
2)Quantas vezes cada valor foi obtido;
3)Qual lado caiu mais vezes (e quantas vezes.)

    >>> lancar_dados(2, 2, 2, 5, 3, 3, 1, 3, 4, 2, 6, 4, 3, 4, 4, 2, 6, 3, 6, 3, 4,
    ... 3, 5, 5, 5, 1, 2, 1, 6, 5, 6, 3, 1, 6, 1, 1, 6, 5, 1, 6, 1, 1, 2, 1, 1, 2, 2,
    ... 4, 4, 4, 2, 1, 4, 6, 6, 4, 2, 4, 4, 2, 5, 3, 6, 1, 2, 5, 4, 4, 5, 3, 4, 6, 6)
    O dado foi lançado 73 vezes
    O número 1 caiu 13 vezes
    O número 2 caiu 13 vezes
    O número 3 caiu 10 vezes
    O número 4 caiu 15 vezes
    O número 5 caiu 9 vezes
    O número 6 caiu 13 vezes
    O lado com o número 4 caiu mais vezes (15 vezes)

    >>> lancar_dados(6, 6, 2, 5, 4, 5, 3, 3, 5, 1, 4, 5, 4, 4, 2, 4, 6, 3, 6, 1,
    ... 6, 6, 6, 6, 5, 5, 6, 6, 3, 5, 5, 1, 5, 5, 5, 2, 6, 4, 5, 5, 1, 3, 2, 3, 3,
    ... 6, 3, 4, 3, 4, 1, 6, 6, 3, 1, 1, 2, 2, 2, 4, 4, 3, 1, 2, 6, 2, 5, 2, 2)
    O dado foi lançado 69 vezes
    O número 1 caiu 8 vezes
    O número 2 caiu 11 vezes
    O número 3 caiu 11 vezes
    O número 4 caiu 10 vezes
    O número 5 caiu 14 vezes
    O número 6 caiu 15 vezes
    O lado com o número 6 caiu mais vezes (15 vezes)

"""


def lancar_dados(*valor_lancamentos):
    """Escreva aqui em baixo a sua solução"""
    numeros_do_dado = {}
    total_de_lancamentos = len(valor_lancamentos)

    for v in valor_lancamentos:
        if v in numeros_do_dado:
            numeros_do_dado[v] += 1
        else:
            numeros_do_dado[v] = 1

    print(f'O dado foi lançado {total_de_lancamentos} vezes')

    dicionario_ordenado = dict(sorted(numeros_do_dado.items()))
    for numero_dado, frequencia in dicionario_ordenado.items():
        print(f'O número {numero_dado} caiu {frequencia} vezes')

    numero_mais_frequente = None
    vezes_mais_frequente = 0

    for numero, frquencia in numeros_do_dado.items():
        if frquencia > vezes_mais_frequente:
            numero_mais_frequente = numero
            vezes_mais_frequente = frquencia

    print(f'O lado com o número {numero_mais_frequente} caiu mais vezes ({vezes_mais_frequente} vezes)')

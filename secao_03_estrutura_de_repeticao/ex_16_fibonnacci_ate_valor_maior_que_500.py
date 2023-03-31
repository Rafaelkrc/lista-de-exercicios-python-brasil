"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
 valor seja maior que 500.

    >>> calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500()
    '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610'
"""


def calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500() -> str:
    """Escreva aqui em baixo a sua solução"""
    t1 = 0
    t2 = 1
    lista = [t1, t2]
    cont = 2
    while cont <= 500:
        t3 = t1 + t2
        lista.append(t3)
        t1 = t2
        t2 = t3
        cont += 1
        if t3 > 500:
            break
    print(f"""'{", ".join(map(str, lista))}'""")

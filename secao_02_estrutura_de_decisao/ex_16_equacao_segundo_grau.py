"""
Exercício 16 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
 valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
 demais valores, sendo encerrado;
b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário.

Mostrar raízes com uma casa decimal.

    >>> resolver_equacao_do_segundo_grau(0, 3, 4)
    'Valor do coeficiente a deve ser diferente de 0'
    >>> resolver_equacao_do_segundo_grau(2, 1, 2)
    'Delta negativo (-15), por isso não existem raízes reais'
    >>> resolver_equacao_do_segundo_grau(1, 2, 1)
    'Delta é 0, raíz única no valor de -1.0'
    >>> resolver_equacao_do_segundo_grau(1, 4, 3)
    'Delta é 4, raízes são -1.0 e -3.0'

"""


def resolver_equacao_do_segundo_grau(a: float, b: float, c: float):
    """Escreva aqui em baixo a sua solução"""
    if a == 0:
        print("'Valor do coeficiente a deve ser diferente de 0'")
    else:
        d = (b ** 2) - (4 * a * c)
        if d < 0:
            print(f"'Delta negativo ({d}), por isso não existem raízes reais'")
        elif d == 0:
            x1 = (-b + d ** (1 / 2)) / (2 * a)
            x2 = (-b - d ** (1 / 2)) / (2 * a)
            if x1 > 0:
                print(f'A equação possui apenas uma raiz real que para x1 é {x1}')
            elif x2 > 0:
                print(f'A equação possui apenas uma raiz real que para x2 é {x2}')
            else:
                print(f"'Delta é {d}, raíz única no valor de -1.0'")
        elif d > 0:
            x1 = (-b + d ** (1 / 2)) / (2 * a)
            x2 = (-b - d ** (1 / 2)) / (2 * a)
            print(f"'Delta é {d}, raízes são {x1} e {x2}'")

"""
Exercício 39 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais alto
 e o número do aluno mais baixo, junto com suas alturas.
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162))
    'O maior aluno é o Renzo com 162 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165))
    'O maior aluno é o Clara com 165 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))
    'O maior aluno é o Oscar com 199 cm. O menor aluno é o Renzo com 162 cm'

"""


def calcular_aluno_mais_baixo_e_mais_alto(*alunos) -> str:
    """Escreva aqui em baixo a sua solução"""

    mais_alto = 0
    aluno_mais_alto = ''
    mais_baixo= 0
    aluno_mais_baixo = ''
    for i, v in alunos:
        if v < mais_baixo or mais_baixo == 0:
            mais_baixo = v
            aluno_mais_baixo = i
        if v > mais_alto:
            mais_alto = v
            aluno_mais_alto = i

    print(f"'O maior aluno é o {aluno_mais_alto} com {mais_alto} cm. "
          f"O menor aluno é o {aluno_mais_baixo} com {mais_baixo} cm'")



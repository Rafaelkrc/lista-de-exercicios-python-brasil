"""
Exercício 12 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Foram anotados os nomes, as idades e alturas de de vários alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses
alunos.

Mostre a média com uma casa decimal.

    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162))
    Média de altura: 162.0 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158))
    Média de altura: 160.0 centímetros.
    Existe(m) 1 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210))
    Média de altura: 176.7 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210), ('Criança', 7, 100)
    ... )
    Média de altura: 157.5 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210),
    ...     ('Criança', 7, 100), ("Shaquille O'Neal", 25, 216)
    ... )
    Média de altura: 169.2 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade

"""


def calcular_baixinhos_com_mais_de_13_anos(*alunos):
    """Escreva aqui em baixo a sua solução"""
    altura = 0
    aluno = 0
    aluno_baixo= 0
    for n, i, a in alunos:
        altura += a
        aluno += 1
    media_altura = altura / aluno
    print(f'Média de altura: {media_altura:.1f} centímetros.')
    for n, i, a in alunos:
        if i > 13 and a < media_altura:
            aluno_baixo += 1

    if aluno_baixo < 1:
        print('Não há nenhum aluno abaixo da média')
    else:
        print(f'Existe(m) {aluno_baixo} aluno(s) com altura abaixo da média com mais de 13 anos:')

    indice = 0
    for n, i, a in alunos:
        if a < media_altura and i > 13:
            indice += 1
            print(f'{indice}. {n}, com {a} centímetros e {i} ano(s) de idade')






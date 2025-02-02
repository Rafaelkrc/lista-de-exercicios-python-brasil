"""
Exercício 14 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""


def investigar(*respostas):
    """Escreva aqui em baixo a sua solução"""
    sim = 0

    for i in respostas:
        if i == 'Sim':
            sim += 1
        else:
            pass

    if sim == 2:
        print("'Suspeito'")
    elif 2 < sim <= 4:
        print("'Cúmplice'")
    elif sim == 5:
        print("'Assassino'")
    else:
        print("'Inocente'")




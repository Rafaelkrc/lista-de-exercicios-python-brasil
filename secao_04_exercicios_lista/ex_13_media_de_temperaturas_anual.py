"""
Exercício 13 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule e MOSTRE A MÉDIA ANUAL das temperaturas e MOSTRE TODAS AS TEMPERATURAS ACIMA DA MÉDIA ANUAL,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

-as temperaturas só serão dadas em inteiro
-todos os meses do ano serão passados à funçao, começando de janeiro e terminando em dezembro.
 Todos seguidos de sua temperatura mensal

(Funçoês recomendadas para estudo:
    - .ljust()
    - enumerate()
    - sum()
    - len()


    >>> from secao_04_exercicios_lista import ex_13_media_de_temperaturas_anual

    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '30']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 24.75 Graus
     1 - Janeiro:       30°
     2 - Fevereiro:     33°
     3 - Março:         27°
     4 - Abril:         25°
     5 - Maio:          29°
     6 - Junho:         25°
    11 - Novembro:      33°
    12 - Dezembro:      25°
    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '35']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 25.17 Graus
     1 - Janeiro:       35°
     2 - Fevereiro:     33°
     3 - Março:         27°
     5 - Maio:          29°
    11 - Novembro:      33°

"""


def temperaturas_acima_da_media():
    """Escreva aqui sua solução: """
    temperaturas = []
    for i in range(12):
        temperatura = int(input('Informe a temperatura: '))
        temperaturas.append(temperatura)

    media_anual = sum(temperaturas) / len(temperaturas)
    print(f'Média anual: {media_anual:.2f} Graus')
    for i, temp in enumerate(temperaturas):
        i += 1
        if temp > media_anual:
            if i == 1:
                mes = 'Janeiro:'
            elif i == 2:
                mes = 'Fevereiro:'
            elif i == 3:
                mes = 'Março:'
            elif i == 4:
                mes = 'Abril:'
            elif i == 5:
                mes = 'Maio:'
            elif i == 6:
                mes = 'Junho:'
            elif i == 7:
                mes = 'Julho:'
            elif i == 8:
                mes = 'Agosto:'
            elif i == 9:
                mes = 'Setembro:'
            elif i == 10:
                mes = 'Outubro:'
            elif i == 11:
                mes = 'Novembro:'
            else:
                mes = 'Dezembro:'
            print(f'{i:>2} - {mes.ljust(14)} {temp}°')
        else:
            pass





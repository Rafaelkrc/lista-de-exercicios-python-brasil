"""
Exercício 38 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
1) Esse funcionário foi contratado em 2018;
2) Em 2019 recebeu aumento de 1,5% sobre seu salário inicial;
3) A partir de 2020 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine a evolução salarial do funcionário em 5 anos

Os valores devem ser exibidos com duas casas decimais

    >>> calcular_salarios_anuais(1000)
    Salário em 2018: R$ 1000.00
    Salário em 2019: R$ 1015.00. Aumento porcentual: 1.50%
    Salário em 2020: R$ 1045.45. Aumento porcentual: 3.00%
    Salário em 2021: R$ 1108.18. Aumento porcentual: 6.00%
    Salário em 2022: R$ 1241.16. Aumento porcentual: 12.00%
    Salário em 2023: R$ 1539.04. Aumento porcentual: 24.00%
    >>> calcular_salarios_anuais(1500)
    Salário em 2018: R$ 1500.00
    Salário em 2019: R$ 1522.50. Aumento porcentual: 1.50%
    Salário em 2020: R$ 1568.17. Aumento porcentual: 3.00%
    Salário em 2021: R$ 1662.27. Aumento porcentual: 6.00%
    Salário em 2022: R$ 1861.74. Aumento porcentual: 12.00%
    Salário em 2023: R$ 2308.55. Aumento porcentual: 24.00%
    
"""


def calcular_salarios_anuais(salario: float):
    """Escreva aqui em baixo a sua solução"""
    salario_inicial = salario
    taxa_aumento = 1.50
    ano = 2019
    print(f'Salário em 2018: R$ {salario_inicial:.2f}')
    salario_atual = 0
    while ano < 2023:
        for i in range(5):
            if ano == 2019:
                salario_atual = float(salario_inicial + (salario_inicial * (taxa_aumento/100)))
                print(f'Salário em {ano}: R$ {salario_atual:.2f}. Aumento porcentual: {taxa_aumento:.2f}%')
                ano += 1
            else:
                taxa_aumento *= 2
                salario_atual = float(salario_atual + (salario_atual * (taxa_aumento/100)))
                print(f'Salário em {ano}: R$ {salario_atual:.2f}. Aumento porcentual: {taxa_aumento:.2f}%')
                ano += 1

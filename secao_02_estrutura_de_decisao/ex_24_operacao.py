"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


def fazer_operacao_e_classificar(num1: float, num2: float, opcao: str):
    """Escreva aqui em baixo a sua solução"""
    resultado = 0
    par_str = pos_str = int_str = ''

    if opcao == '+':
        resultado = num1 + num2
    elif opcao == '-':
        resultado = num1 - num2
    elif opcao == '*':
        resultado = num1 * num2
    elif opcao == '/':
        resultado = num1 / num2
    elif opcao != 1 or 2 or 3 or 4:
        print('Opção inválida! Tente novamente!')

    if resultado % 2 == 0:
        par_str = 'par,'
    elif resultado % 2 != 0:
        par_str = 'impar,'

    if resultado > 0:
        pos_str = 'positivo'
    elif resultado < 0:
        pos_str = 'negativo'
    else:
        pos_str = 'neutro'

    if int(resultado) == resultado:
        int_str = 'inteiro'
    else:
        int_str = 'decimal'

    if int_str == 'decimal':
        print(f'Resultado: {resultado:.2f}')
        print(f'Número é {pos_str} e {int_str}.')
    else:
        print(f'Resultado: {resultado:.2f}')
        print(f'Número é {par_str} {pos_str} e {int_str}.')


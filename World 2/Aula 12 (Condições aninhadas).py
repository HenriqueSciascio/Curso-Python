"""
#Desafio 36

valor = float(input('qual o valor da casa? '))
salario = float(input('qual o seu salario? '))
anos = int(input('quantos anos vc vai pagar o emprestimo? '))

prestacao = valor/(anos*12)

if prestacao < salario * 0.3:
    print(f'emprestimo aprovado, o valor do seu emprestimo é de {prestacao:,.2f}R$ ao mes')
else:
    print('Emprestimo negado pois a prestação mensal é maior que 30% do seu salario')
"""

#Desafio 37
"""
num = int(input('escreva um numero inteiro: '))
base = int(input('escreva a base desejada: 1-Binario 2-Octal 3-Hexa: '))
NumBin = ''
NumHex = ''


if base == 1:
    while num != 0:
        bin = num % 2
        NumBin += str(bin)
        num = num // 2
    print(NumBin[::-1])
elif base == 2:
    while num != 0:
        bin = num % 8
        NumBin += str(bin)
        num = num // 8
    print(NumBin[::-1])
elif base == 3:
    while num != 0:
        hex = num % 16
        if hex == 10 :
            hexL = 'A'
            NumHex += hexL
        if hex == 11 :
            hexL = 'B'
            NumHex += hexL
        if hex == 12 :
            hexL = 'C'
            NumHex += hexL
        if hex == 13 :
            hexL = 'D'
            NumHex += hexL
        if hex == 14 :
            hexL = 'E'
            NumHex += hexL
        if hex == 15 :
            hexL = 'F'
            NumHex += hexL
        if hex not in [10, 11, 12, 13, 14, 15]:
            NumHex += str(hex)
        num = num // 16
    print(NumHex[::-1])
"""

# Desafio 38
"""
num1 = int(input('escreva um numero: '))
num2 = int(input('escreva outro numero: '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num1 == num2:
    print('Os dois valores são iguais')
else:
    print('O segundo valor é maior')
"""

#Desafio 39
"""
ano = int(input('escreva o ano que você nasceu: '))

anocomp = 2023 - ano # ano atual

if anocomp > 18:
    print('já passou do tempo para você se alistar!')
    print(f'você devia ter se alistado a {anocomp - 18}')
elif anocomp == 18:
    print('está na hora de se alistar!')
else:
    print(f'ainda falta {18 - anocomp} anos para você se alistar')
"""
#Desafio 40
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
"""
nota1 = float(input('escreva a primeira nota: '))
nota2 = float(input('escreva a segunda nota: '))

media = (nota1+nota2)/2

if media >= 7:
    print('APROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
"""
#Desafio 41
"""
ano = int(input('coloque o ano do nascimento: '))

anocomp = 2023 - ano

if anocomp <= 9:
    print('Você é um nadador(a) Mirim')
elif 9 < anocomp <= 14:
    print('Você é um nadador(a) Infantil')
elif 14 < anocomp <= 19:
    print('Você é um nadador(a) Junior')
elif 19 < anocomp <= 20:
    print('Você é um nadador(a) Sênior')
else:
    print('Você é um nadador(a) Master')
"""
#Desafio 42
"""
a = float(input("escreva o primeiro lado: "))
b = float(input("escreva o segundo lado: "))
c = float(input("escreva o terceiro lado: "))

if abs(b - c) < a < b + c:
    print('primeira fase passou')
    if abs(a - c) < b < a + c:
        print('segunda fase passou')
        if abs(a - b) < c < a + b:
            print('pode ser um triangulo')
            if a == b == c:
                print('este é um triangulo equilatero')
            elif a == b or a == c or b == c:
                print('este é um triangulo isóceles')
            elif a != b != c:
                print('este é um triangulo escaleno')
        else:
            print('falhou na terceira')
    else:
        print('falhou na segunda')
else:
    print('falhou na primeira')
"""
#Desafio 43
"""
peso = float(input('Escreva seu peso (em kg): '))
alt = float(input('Escreva sua altura (em m): '))

imc = peso/alt**2

if imc < 18.5:
    print(f'Seu peso é: {imc:,.2f}, e seu imc é Abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Seu peso é: {imc:,.2f}, e seu imc é Peso Ideal')
elif 25 <= imc < 30:
    print(f'Seu peso é: {imc:,.2f}, e seu imc é Sobrepeso')
elif 30 <= imc < 40:
    print(f'Seu peso é: {imc:,.2f}, e seu imc é Obesidade')
elif imc < 40:
    print(f'Seu peso é: {imc:,.2f}, e seu imc é Obsesidade Mórbida')
"""
#Desafio 44
"""
valor = float(input('escreva o valor do produto: '))
condi = int(input('escreva a condição de pagamento:\n'
                  'à Vista no dinheiro ou cheque    - 1\n'
                  'à Vista no cartão                - 2\n'
                  'em até duas vezes no cartão      - 3\n'
                  'em três vezes ou mais no cartão  - 4\n'))

if condi == 1:
    print(f'O valor do Item ficou: {valor-(valor*0.1)}')
elif condi == 2:
    print(f'O valor do Item ficou: {valor-(valor*0.05)}')
elif condi == 3:
    print(f'O valor do Item ficou: {valor}')
elif condi == 4:
    print(f'O valor do Item ficou: {valor+(valor*0.2)}')
"""
# Desafio 45
"""
import random

print("JOGO DE JOKEMPO")
EscP = int(input('faça sua escolha:\n'
                '1-Pedra; 2-Papel; 3-Tesoura\n'))

EscC = random.choice((1,2,3)) # 1-pedra, 2-papel, 3-tesoura

if EscP == EscC:
    print('foi um empate!')
elif EscP == 1 and EscC == 3:
    print('Você venceu! Você escolheu Pedra e o computador Tesoura')
elif EscP == 1 and EscC == 2:
    print('Você perdeu... Você escolheu Pedra e o computador Papel')
elif EscP == 2 and EscC == 1:
    print('Você venceu! Você escolheu Papel e o computador Pedra')
elif EscP == 2 and EscC == 3:
    print('Você perdeu... Você escolheu Papel e o computador Tesoura')
elif EscP == 3 and EscC == 1:
    print('Você perdeu... Você escolheu Tesoura e o computador Pedra')
elif EscP == 3 and EscC == 2:
    print('Você venceu! Você escolheu Tesoura e o computador Papel')
"""
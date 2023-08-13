# desafio 28
"""
from random import choice

num = int(input('escolha um numero de 1 a 5: '))
num1 = choice(range(1, 5))

if num == num1:
    print(f'Você acertou o numero! O numero que escolhi era: {num1}')
else:
    print(f'Você não acertou o numero... O numero que escolhi era: {num1}')
"""
# desafio 29
"""
km = int(input("escreva a velocidade do carro: "))

if km > 80:
    print('O seu carro foi multado\n')
    print(f'A multa sairá no valor: {7*(km-80):,.2f}R$')
else:
    print('Ta tudo certo :)')
"""
# desafio 30
"""
n = int(input('escolha um numero: '))

if n%2 == 1:
    print(f'o seu numero ({n}) é impar')
else:
    print(f'o seu numero ({n}) é par')
"""
# desafio 31
"""
km = int(input('qual a distancia da sua viajem? '))

if km <= 200:
    print(f'o preço de sua passagem será: {km * 0.5}')
else:
    print(f'o preço de sua passagem será: {km * 0.45}')
"""
# desafio 32
"""
ano = int(input('escolha um ano: '))

if ano % 4 == 0:
    print('O ano que você escolheu é bisexto')
else:
    print('O ano que você escolheu não é bisexto')
"""
# desafio 33
"""
n1 = int(input('escolha o primeiro numero: '))
n2 = int(input('escolha o segundo numero: '))
n3 = int(input('escolha o terceiro numero: '))

if n1 > n2 > n3 or n1 > n2 == n3 or n1 == n2 > n3:
    print(f'O maior é o numero {n1} e o menor numero é o {n3}')
elif n1 > n3 > n2 or n1 > n3 == n2 or n1 == n3 > n2:
    print(f'O maior é o numero {n1} e o menor numero é o {n2}')
elif n2 > n1 > n3 or n2 > n1 == n3 or n2 == n1 > n3:
    print(f'O maior é o numero {n2} e o menor numero é o {n3}')
elif n2 > n3 > n1 or n2 > n3 == n1 or n2 == n3 > n1:
    print(f'O maior é o numero {n2} e o menor numero é o {n1}')
elif n3 > n1 > n2 or n3 > n1 == n2 or n3 == n1 > n2:
    print(f'O maior é o numero {n3} e o menor numero é o {n2}')
elif n3 > n2 > n1 or n3 > n2 == n1 or n3 == n2 > n1:
    print(f'O maior é o numero {n3} e o menor numero é o {n1}')
elif n1 == n3 == n2:
    print(f'Todos os numeros são iguais')
"""
# desafio 34
"""
sal = float(input('escreva seu salario: '))

if sal > 1250.00:
    print(f'Seu novo salario é de {sal*1.1:,.2f}')
else:
    print(f'Seu novo salario é de {sal*1.15:,.2f}')
"""
# desafio 35
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
        else:
            print('falhou na terceira')
    else:
        print('falhou na segunda')
else:
    print('falhou na primeira')
"""
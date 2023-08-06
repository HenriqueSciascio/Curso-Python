#Desafio 22
"""
nome = str(input('escreva seu nome: '))
divisao = nome.split()
print(f'seu nome com todas as letras maiusculas ficará: {nome.upper()}\n'
      f'seu nome com todas as letras minusculas ficará: {nome.lower()}\n'
      f'seu nome sem espaços tem {len(nome)-nome.count(" ")} letras\n'
      f'seu primeiro nome contem {len(divisao[0])} letras')
"""
#Desafio 23 Parte 1 (era impossivel com str sem if)
"""
num = str(input('escreva um numero de 0 a 9999: '))

print(f'seu numero tem {len(num)} algarismo(s)')
if len(num) == 4:
    print(f'milhar: {num[0]}')
    print(f'centena: {num[1]}')
    print(f'dezena: {num[2]}')
    print(f'unidade: {num[3]}')
if len(num) == 3:
    print(f'centena: {num[0]}')
    print(f'dezena: {num[1]}')
    print(f'unidade: {num[2]}')
if len(num) == 2:
    print(f'dezena: {num[0]}')
    print(f'unidade: {num[1]}')
if len(num) == 1:
    print(f'unidade: {num[0]}')
"""
#Desafio 23 parte 2
"""
from math import trunc
num = int(input('escreva um numero de 0 a 9999: '))

print(f'seu numero é {num}')
print(f'milhar: {trunc(num/1000)}')
print(f'centena: {trunc(num// 100 % 10)}')
print(f'dezena: {trunc(num// 10 % 10)}')
print(f'unidade: {trunc(num// 1 % 10)}')
"""


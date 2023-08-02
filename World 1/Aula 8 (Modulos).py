#exercicio 16
"""
from math import trunc
num = float(input('escreva um numero: '))

print(f'a parte inteira do numero {num} é igual a {trunc(num)}')
"""
#exercicio 17
"""
from math import sqrt
cat1 = float(input('escreva o cateto adjacente: '))
cat2 = float(input('escreva o cateto oposto: '))

print(f'sendo o cateto adjacente {cat1} e o cateto oposto {cat2} a hipotenusa será aproximadamente {sqrt((cat1**2)+(cat2**2)):.2f}')
"""
#exercicio 18
"""
from math import sin, cos, tan
x = float(input('escreva um angulo qualquer: '))
print(f'o seno do seu ângulo é {sin(x):.2f}\n'
      f'o cosseno do seu ângulo é {cos(x):.2f}\n'
      f'a tangente do seu ângulo é {tan(x):.2f}')
"""
#exercicio 19
"""
from random import choice

a1 = str(input('escolha o nome do primeiro aluno: '))
a2 = str(input('escolha o nome do segundo aluno: '))
a3 = str(input('escolha o nome do terceiro aluno: '))
a4 = str(input('escolha o nome do quarto aluno: '))

print(f'o aluno escolhido para apagar o quadro foi o(a) {choice([a1, a2, a3, a4])}')
"""
#exercicio 20
"""
from random import shuffle

a1 = str(input('escolha o nome do primeiro aluno: '))
a2 = str(input('escolha o nome do segundo aluno: '))
a3 = str(input('escolha o nome do terceiro aluno: '))
a4 = str(input('escolha o nome do quarto aluno: '))

list = [a1, a2, a3, a4]
shuffle(list)

print(f'A ordem de apresentação ficou: {list}')
"""
#exercicio 21
"""
import time
from pygame import mixer
#se eu instalasse vlc tambem funcionaria
mixer.init()
mixer.music.load('C:/Users/henri/Downloads/mp3 teste.mp3')
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
"""
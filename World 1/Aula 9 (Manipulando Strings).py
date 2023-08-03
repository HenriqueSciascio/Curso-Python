frase = 'Curso em Vídeo Python'

#Fatiamento
print(frase[9])         # V

print(frase[9:13])      # Víde

print(frase[9:21])      # Vídeo Python

print(frase[9:21:2])    # VdoPto

print(frase[:5])        # Curso

print(frase[15:])       # Python

print(frase[9::3])      # VePh

#Análise
len(frase)              # 21

frase.count('o')        # 3
frase.count('o',0,13)   # já com fatiamento / 1

frase.find('deo')       # 11
frase.find('Android')   # -1 (404 not found)
'Curso' in frase        # true

#Transformação

frase.replace('Python', 'Android')  # Curso em Vídeo Android

frase.upper()                       # CURSO EM VÍDEO PYTHON
frase.lower()                       # curso em vídeo python
frase.capitalize()                  # Curso em vídeo python
frase.title()                       # Curso Em Vídeo Python

frase.strip()                       # tirar todos os espaços (esquerda e direita)
frase.rstrip(), frase.lstrip()      # tirar os espaços direita e esquerda respectivamente

#Divisão

frase.split()                       # [Curso] [em] [Vídeo] [Python]

#Junção

'-'.join(frase)                     # Curso-em-Vídeo-Python
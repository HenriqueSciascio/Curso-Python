"""#exercicio 3
x = int(input('digite um valor: '))
y = int(input('digite outro valor: '))
print(f'A soma entre {x} e {y} é igual a {x+y}!')
"""
#exercicio 4
x = input('Digite algo: ')

print(f'o tipo dessa variavel é: {type(x)}\n'
      f'Só tem espaços? {x.isspace()}\n'
      f'é um numero? {x.isnumeric()}\n'
      f'é alfabetico? {x.isalpha}\n'
      f'é alfanumerico? {x.isalnum()}\n'
      f'esta em maiusculas? {x.isupper()}\n'
      f'esta em minusculas? {x.islower()}\n'
      f'esta capitalizada? {x.istitle()}'
      )

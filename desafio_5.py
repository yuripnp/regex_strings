import re

"""
Renan está desenvolvendo um sistema que verifica se os links de sites parceiros 
começam com https:// e terminam com .com. Esses critérios são obrigatórios para que 
o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize essa 
validação de forma automática.

Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?

input:
Digite a URL: https://www.exemplo.com
output:
A URL é válida.
"""
ulr = input("Digite a URL: ")
# Expressão regular para verificar se a URL começa com https:// e termina com .com
regex = r'^https://.*\.com$'
# Verifica se a URL corresponde à expressão regular
if re.match(regex, ulr):
    print("A URL é válida.")
else:
    print("A URL é inválida.")

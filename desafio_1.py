"""
Victor trabalha em um sistema de e-commerce e precisa organizar os nomes dos produtos que 
estão sendo cadastrados pelos lojistas. Esses nomes geralmente vêm com letras misturadas 
entre maiúsculas e minúsculas, além de espaços desnecessários no início e no final.

Ajude Victor a criar um programa que receba um nome de produto e o padronize, deixando todas 
as letras minúsculas e removendo os espaços extras.

input: 
Digite o nome do produto: ChocoLAte Branco

output:
chocolate branco
"""

texto = input("Digite o nome do produto: ")

# Remover espaços em branco no início e no final
texto = texto.strip()
# Converter para letras minúsculas
texto = texto.lower()
# Remover espaços extras entre as palavras
texto = ' '.join(texto.split())
print(texto)

"""
Rafaela trabalha na área de marketing e quer criar mensagens personalizadas para os clientes. 
Ela precisa de um programa que permita exibir saudações baseadas no nome do cliente e na cidade 
onde ele mora.

Crie um programa que solicite o nome e a cidade de um cliente e exiba uma mensagem de boas-vindas 
personalizada.

input:
Digite o nome do cliente: Ana
Digite a cidade do cliente: São Paulo
output:
Olá Ana, seja bem-vindo(a) à nossa loja! Você está em São Paulo.
"""

nome = input("Olá Cliente, qual o seu nome? ")
cidade = input("Qual a sua cidade? ")

print(f"Olá {nome}, seja bem-vindo(a) à nossa loja! Você está em {cidade}.")
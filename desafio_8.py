import re
"""
Lorena trabalha no setor de cadastros de uma empresa e precisa garantir que os nomes 
inseridos pelos clientes estejam no formato correto. O padrão esperado é que os nomes 
comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais). 
Para facilitar o trabalho, ela quer um programa que valide automaticamente os nomes fornecidos.

Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.

input: "Ana Clara"
output: "Nome válido."
input: "ana clara"
output: "Nome inválido."
input: "Ana123"
output: "Nome inválido."
"""

nome = input("Digite o nome do cliente para validar: ")
# Expressão regular para validar o nome
expressao_regular = r'^[A-Z][a-z]+(\s[A-Z][a-z]+)*$'
# Verifica se o nome corresponde à expressão regular
if re.match(expressao_regular, nome):
    print("Nome válido.")
else:
    print("Nome inválido.")

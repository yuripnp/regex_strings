
"""
Sara trabalha no setor de atendimento de uma empresa e precisa verificar rapidamente 
se os clientes estão digitando seus números de CPF no formato correto antes de registrar 
os dados no sistema.

O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), 
seguidos por um bloco de 2 dígitos separados por um traço (-).

Ajude Sara a criar um programa que solicite o CPF de um cliente e verifica se ele está no 
formato correto.

input: "123.456.789-01"
output: "CPF válido."
input: "12345678901"
output: "CPF inválido."
"""

import re


numero_cpf = input("Digite o CPF do cliente para validar: ")
# Expressão regular para validar o CPF
expressao_regular = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
# Verifica se o CPF corresponde à expressão regular
if re.match(expressao_regular, numero_cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")


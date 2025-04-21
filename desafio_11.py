
"""
Carlos é analista de dados em um hospital e está organizando informações de pacientes em 
um banco de dados. Ele recebe os dados no formato: "PrimeiroNome Sobrenome - Ano". Por exemplo, 
“Monalisa Silva - 1994”.

Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, 
o sobrenome e o ano de nascimento para preencher os campos do sistema.

Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de 
um paciente e exiba-os separadamente.

input: "Monalisa Silva - 1994"
output: 
Nome: Monalisa
Sobrenome: Silva
Ano de nascimento: 1994
"""
import re


nome_ano = input("Digite o nome completo e o ano de nascimento: ")
primeiro_nome = nome_ano.split()[0]
nome_do_meio = " ".join(nome_ano.split()[1:-1])
ano_nascimento = nome_ano.split()[-1]
# Expressão regular para validar o ano de nascimento
expressao_regular = r'^\d{4}$'
# Verifica se o ano de nascimento corresponde à expressão regular
if re.match(expressao_regular, ano_nascimento):
    print(f"Nome: {primeiro_nome}")
    print(f"Ano de nascimento: {ano_nascimento}")
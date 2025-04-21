import re
"""
João é atendente em uma farmácia e precisa verificar se um cliente forneceu um número de 
receita válido em uma descrição. O número da receita é sempre o único número presente no 
texto fornecido pelo cliente. Ele quer um programa que extraia esse número diretamente e 
confirme se o texto está correto, sem a necessidade de trabalhar com listas ou loops.

Com base nesse cenário, crie um programa que receba um texto com uma descrição e exiba uma 
mensagem com o número encontrado.

input: "O cliente Yuri Pimentel deu o número de receita 1234391 entregue hoje."
output: "Número da receita: 1234391"
"""

textoDescritivo = "O cliente Yuri Pimentel deu o número de receita 1234391 entregue hoje."
# Extraindo o número da receita
numero_receita = re.search(r'\d+', textoDescritivo)
if numero_receita:
    print(f"Número da receita: {numero_receita.group()}")

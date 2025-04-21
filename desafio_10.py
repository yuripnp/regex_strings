import re
"""

"""

texto = input("Digite o texto: ")
letra_inicial = input("Digite a letra inicial: ")
palavras_com_letra = []
# Expressão regular para encontrar palavras que começam com a letra fornecida
expressao_regular = rf'\b{letra_inicial}\w*'
# Encontra todas as palavras que começam com a letra fornecida
palavras_com_letra = re.findall(expressao_regular, texto)
# Verifica se foram encontradas palavras
if palavras_com_letra:
    print(f"Palavras que começam com '{letra_inicial}': {', '.join(palavras_com_letra)}")
else:
    print(f"Nenhuma palavra encontrada que comece com '{letra_inicial}'.")
textoUm = 'Isso aqui é um texto'
textoDois = "Isso aqui é outro texto"
textoTres = '''Isso aqui é um texto
que ocupa mais de uma linha'''

textoQuatro = """Isso aqui é um texto
que ocupa mais de uma linha
e tem mais de uma linha"""

remover_espacos = '   Olá, Mundo!   '
remover_espacos = remover_espacos.strip()  # Remove espaços em branco do início e do fim
remover_espacos = remover_espacos.lstrip()  # Remove espaços em branco do início
remover_espacos = remover_espacos.rstrip()  # Remove espaços em branco do fim
remover_espacos = remover_espacos.replace(' ', '')  # Remove todos os espaços em branco
remover_espacos = remover_espacos.split()  # Divide a string em uma lista de palavras
juntar = textoUm.join(' ')  # Junta a lista de palavras em uma string
juntar = ' '.join(remover_espacos)  # Junta a lista de palavras em uma string
maiusculo = textoUm.upper()  # Converte a string para maiúsculo
minusculo = textoUm.lower()  # Converte a string para minúsculo

formato = 'Olá, {}!'.format('Mundo')  # Formata a string com o valor da variável
print(textoUm[5])
print(textoUm[0:5])  # Imprime os primeiros 5 caracteres da string
print(textoUm[5:])  # Imprime os caracteres da string a partir do índice 5
print(textoUm[-1])  # Imprime o último caractere da string
print(textoUm[-5:])  # Imprime os últimos 5 caracteres da string
print(textoUm[::2])  # Imprime os caracteres da string com passo 2
print(textoUm[::-1])  # Imprime a string invertida
print("texto" in textoUm)
print("python" not in textoUm)
print(textoDois.startswith('Isso'))  # Verifica se a string começa com 'Isso'
print(textoDois.endswith('texto'))  # Verifica se a string termina com 'texto'
print(textoUm.find('texto'))  # Encontra a posição da substring 'texto' na string
print(textoUm.count('texto'))  # Conta o número de vezes que a substring 'texto' aparece na string

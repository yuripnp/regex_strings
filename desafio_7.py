import re

"""
Nathalia é uma escritora que está revisando um texto para publicação. Durante o processo, 
ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, 
como "ótimo". Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências 
da palavra "bom" por "ótimo" no texto.

Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. 
O programa deve exibir o texto com as alterações aplicadas.

input: "O dia está bom, a comida está boa e o filme é bom."
input: "bom"
input: "ótimo"
output: "O dia está ótimo, a comida está boa e o filme é ótimo."
"""

textoDescritivo = input("Digite o texto descritivo: ")
palavraSerSubstituida = input("Digite a palavra a ser substituída: ")
palavra_que_substitui = input("Digite a palavra que irá substituir: ")

if palavraSerSubstituida not in textoDescritivo:
    print("A palavra não existe no texto.")
else:
    novo_texto = textoDescritivo.replace(palavraSerSubstituida, palavra_que_substitui)
    print(f"Texto modificado: {novo_texto}")
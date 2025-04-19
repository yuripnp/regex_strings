import math

"""
Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores 
recebem dicas baseadas em partes específicas de uma palavra-chave. Sua missão é 
desenvolver um programa que extraia trechos importantes de qualquer palavra digitada.

Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e 
as três últimas letras.

input:
Digite a palavra-chave: python
output:
Primeiras letras: pyt
Últimas letras: hon
"""

palavra_chave = input("Digite a palavra-chave: ")
primeiras = ""
ultimas = ""
palavra_chave = palavra_chave.replace(" ", "")
# Remover espaços em branco no início e no final

if(len(palavra_chave) <= 0):
    print("Palavra-chave inválida")
elif(len(palavra_chave) > 20):
    print("Palavra-chave muito longa")
else:
    if(len(palavra_chave)%2 == 0):
        primeiras = palavra_chave[:len(palavra_chave)//2]
        ultimas = palavra_chave[len(palavra_chave)//2:]
    else:
        valorBaixo = math.floor(len(palavra_chave)/2)
        valorAlto = math.floor(len(palavra_chave)/2)
        primeiras = palavra_chave[:valorBaixo]
        ultimas = palavra_chave[valorAlto:]
    print(f"Primeiras letras: {primeiras}")
    print(f"Últimas letras: {ultimas}")
        
    
    
    
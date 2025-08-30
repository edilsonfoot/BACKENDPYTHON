'''
Contando frequência de palavras

Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
'''


def contar(palavras):
    contagem = {}
    for p in palavras:
        if p in contagem:
            contagem[p] += 1
        else:
            contagem[p] = 1
    return contagem

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(contar(palavras))

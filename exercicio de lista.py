
""" Q1
livros = ["romance", "religião", "politica"]
print(livros)

"""

""" Q2

livros = ["romance", "religião", "politica"]    #imprimindo apenas "o primeiro e ultimo"
livros.remove("religião")
print(livros)

"""

""" Q3

livros = ["romance", "religião", "politica"]
livros.append(["sociologia","matematica"])
print(livros)

"""

""" Q4

livros = ["romance", "religião", "politica"]
livros.insert(2, "Duna")
print(livros)

"""

""" Q5

livros = ["romance", "religião", "politica"]
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")
print(livros)

"""

""" Q6

numeros = [1, 2, 3, 2, 4, 2, 4, 5]
numeros.count([2])
print(numeros)

"""


#método def
livros = ["romance", "religião", "Duna", "politica", "sociologia", "matematica"]
def elementos_interessantes(lista):
    for elemento in lista:
        print(f"O elemento '{elemento}' é interessante!")

""" 

idades = [12, 18, 25, 14, 30]
for i in idades:
    if i >= 18:
        print(i)

"""



valores = [10, 20, 30, 40]
soma = 0
for v in valores:
    soma += v
print(soma)

"""

"''

notas = []
for i in range(2):
    aluno = []
    for j in range(3):
        n = float(input("Nota: "))
        aluno.append(n)
    notas.append(aluno)
for aluno in notas:
    media = sum(aluno) / len(aluno)
    print(media)

"""
#Usando linha de comprehension, crie um tabuleiro vazio


import numpy as np       # biblioteca que questão pediu
tabuleiro = [["[ ]" for i in range(8)] for j in range(8)]
tabuleiro[0] = ["tor","cav","bis","rai","rei","bis","cav","tor"]
tabuleiro[1] = ["pea"]*8
tabuleiro[6] = ["pea"]*8
tabuleiro[7] = ["tor","cav","bis","rai","rei","bis","cav","tor"]
print(np.array(tabuleiro))

tabuleiro = [["[]" for casa in range (8)] for linha in range(8)]
print(tabuleiro)
linha_peões = ["pea"]*8
print(linha_peões)
lista_peças = ["tor, "cav", "bis", "rai", rei", "bis", "cav", "tor"]

tabuleiro[0] = linha_pecas.copy()
tabuleiro[-1] = linha_pecas[::-1].copy()
tabuleiro[1] = linha_peoes.copy()
tabuleiro[-2] = linha_peoes.copy()
'''
tabuleiro.insert


for linha in tabuleiro:
    print(linha)
'''

print()
for linha in tabuleiro:
    print(linha)



#subistituido a ultima linha
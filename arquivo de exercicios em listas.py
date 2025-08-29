'''1
lista = ["3 livros diferentes"]
livros = ["romance", "religião", "politica"]
print(livros)

'''

'''2
#Método .remove()
livros = ["romance", "religião", "politica"]    #imprimindo apenas "o primeiro e ultimo"
livros.remove("religião")
print(livros)

'''

'''3
#Método .append()
livros = ["romance", "religião", "politica"]
livros.append(["sociologia","matematica"])
print(livros)

'''

'''4
#Método .insert()
livros = ["romance", "religião", "politica"]
livros.insert(2, "Duna")
print(livros)

'''

'''5
#condicional while
livros = ["romance", "religião", "politica"]
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
    print("livro encontrado")
else:
    print("Livro não encontrado")
print(livros)
'''

'''6
#Método .count()
numeros = [1, 2, 3, 2, 4, 2, 4, 5]
quantidade = numeros.count(2)
print(f"O numero 2 aparece {quantidade} vezes.")
'''


'''
#método def
livros = ["romance", "religião", "Duna", "politica", "sociologia", "matematica"]
def elementos_interessantes(lista):
    for elemento in lista:
        print(f"O elemento '{elemento}' é interessante!")
'''


'''

idades = [12, 18, 25, 14, 30]
for i in idades:
    if i >= 18:
        print(i)
'''


'''

valores = [10, 20, 30, 40]
soma = 0
for v in valores:
    soma += v
print(soma)

'''
''
'''
#Método 
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
'''




import numpy as np()                                                                 
tabuleiro = [["[ ]" for i in range(8)] for j in range(8)]
tabuleiro[0] = ["tor","cav","bis","rai","rei","bis","cav","tor"]
tabuleiro[1] = ["pea"]*8
tabuleiro[6] = ["pea"]*8
tabuleiro[7] = ["tor","cav","bis","rai","rei","bis","cav","tor"]
print(np.array(tabuleiro))


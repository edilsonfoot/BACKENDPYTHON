
""" Q1
aluno = {"nome": "Edilson", "Idade": 52, "nota": 9.0}
print(aluno["Idade"])

"""

""" Q2
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print(produto["nome"], produto["estoque"])

"""

""" Q3
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"
print(pessoa)

"""

""" Q4

carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
carro.pop("ano")
print(carro)

"""

""" Q5

contato = {"nome": "Ana", "email": "ana@email.com"}
contato_buscado = input("telefone:")
if contato_buscado in contato:
    print("contato encontrado")
else:
    print("contato não encontrado")

"""

""" Q6

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

"""

""" Q7

d = {"a": 1, "b": 2, "c": 3}
invertido = {}
for k, v in d.items():
    invertido[v] = k
print(invertido)

"""

""" Q8
notas = {"Ana": [7, 8, 9], "Carlos": [6, 5, 7]}
for aluno in notas:
    media = sum(notas[aluno]) / len(notas[aluno])
    print(aluno, media)

"""

""" Q9
def mesclar(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
print(mesclar(a, b))

"""

""" Q10

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
for k, v in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
    print(k, v)

"""
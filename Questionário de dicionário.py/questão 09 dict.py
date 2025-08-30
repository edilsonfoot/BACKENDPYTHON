'''
Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
'''


#Usando a função "def" no método ".copy" com a  função "return"
def mesclar(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
print(mesclar(a, b))

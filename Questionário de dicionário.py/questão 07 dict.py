'''
Invertendo um dicionário

Dado o dicionário:

d = {"a": 1, "b": 2, "c": 3}
Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
'''



d = {"a": 1, "b": 2, "c": 3}
invertido = {}
for k, v in d.items():
    invertido[v] = k
print(invertido)

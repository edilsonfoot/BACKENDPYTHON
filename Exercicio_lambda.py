'''
Dobro dos números (map + lambda)

Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.
Filtrar pares (filter + lambda)
'''

'''
numeros = [1, 2, 3, 4, 5]
dobrados = map(lambda x: x * 2, numeros)
print(list(dobrados))

lista = [1,2,3,4,5]
print(list(filter(lambda num:num % 2 != 0, lista)))
'''

'''
Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.
Soma dos números (reduce + lambda)
'''
'''
numeros = [10, 15, 20, 25, 30]

# Usando filter e lambda para pegar apenas os números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)
'''
'''
from functools import reduce


lista = [10, 15, 20, 25, 30]
print(reduce(lambda x, y : x + y, lista))
'''


'''
Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].
Ordenação por comprimento da palavra (sorted + lambda)
'''
'''
from functools import reduce

# Lista de exemplo
numeros = [1, 2, 3, 4, 5]
'''


'''
Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.
Primeira letra maiúscula (map + lambda)
'''
'''
lista = ["uva", "banana", "maçã", "laranja"]

# Ordenando por tamanho da palavra
ordenado_tamanho = sorted(lista, key=lambda palavra: len(palavra))
print("Ordem por tamanho:", ordenado_tamanho)
'''

'''
lista = ["uva", "banana", "maçã", "laranja"]

# Usando map com str.title para capitalizar as primeiras letras
resultado = list(map(str.title, lista))

print(resultado)
'''


'''
Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].
Produto dos números (reduce + lambda)
'''

'''
lista = ["ana", "pedro", "maria"]

resultado = list(map(str.title, lista))

print(resultado)
'''


'''
Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].
Ordenar por último caractere (sorted + lambda)
'''
'''
lista = [2, 3, 4, 5]
from functools import reduce

# Lista de exemplo
numeros = [2, 3, 4, 5]

# Multiplicando todos os elementos da lista
resultado = reduce(lambda x, y: x * y, numeros)

print(resultado)
'''

'''
Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.
'''

lista = ["banana", "uva", "maçã", "laranja"]


ordenado = sorted(lista, key=lambda palavra: palavra[-1])

print(ordenado)


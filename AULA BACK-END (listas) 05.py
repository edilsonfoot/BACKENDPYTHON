"""
LISTAS

"""
#lista = []
#print(type(listas))

frutas = ["limão", "banana", "morango", "coco"]
print(frutas)



                                                                        ### adicionando elementos
frutas.insert(1, "maça")
print(frutas)

frutas.append("kiwi")                                                  ### outra forma de adicionar elementos
print(frutas)

frutas_vermelhas = ["morango", "uva", "amora", "framboesa"]
print(frutas_vermelhas)

frutas+=frutas_vermelhas                                              #juntou os dois conjuntos de listas de frutas
print(frutas)

### remover elementos
print("removendo elementos")
print(frutas.count("morango"))                                       ### diz a posição do elemento selecionado
frutas.remove("morango")
print(frutas)

print("primeiro pop")                                                ### removendo o ultimo elemento
frutas.pop()

print("segundo pop")                                                 ### removendo o elemento (4)
frutas.pop(4)
print(frutas)

del frutas [5]
print(frutas)

del frutas[2:5]                                                      ### remove apenas de 2, 3, 4
print(frutas)

frutas2 = frutas[:]
print(frutas)

### Copia de lista
print("--------")
frutas2 = frutas[:]
frutas2 = frutas.copy()
print(frutas2)
print(id(frutas))
print(id(frutas2))


### acrescenta elemento a lista
frutas.extend("morango")

### encontra o elemento pela localização
frutas.index()
print(frutas)

### inverte as ordens dos elementos
frutas.reverse()
print(frutas)

frutas.sort()
print(frutas)

    



### lista com numeros
numeros = [ 3, 5, 77, 4, 1]
numeros2 = numeros

numeros2.append("42")
print(id(numeros))
print(id(numeros2))



família = ["Edilson", "Elisângela", "Lavínia", "Luiz"]
#              0          1             2         3
#             -4         -3            -2        -1

#print(família[3])     - retorna um indice
#print(família[-3])    - retorna um indice de traz pra frente
#print(família[2:])    - retorna a partir do indice 2
#print(família[2:3])   -retorna a partir do indice 2 até 3, excluindo o 3

print(família)
família[3] = "Edilson"                #trocou o nome Luiz por Edilson
print(família)

família.extend(["Eraldo", "Laíde"])   #acrescentou os nomes Eraldo e Laíde, sempre no final
print(família)

família.insert(1, "Balula")           #insere uma pessoa na posição escolhida
print(família)

família.pop()                          #remove o último nome
print(família)

família.remove("Eraldo")               #remove o nome escolhido

print(família)

família.clear()

família = ["Edilson", "Elisângela", "Lavínia", "Luiz"]
print(família)

idade_família = [53, 50, 22, 13]
print(idade_família)
idade_família.sort()
print(idade_família)

idade_família.reverse()
print(idade_família)


#copiar uma nova familia, apatir da atual (cópia)
família2 = família()

#remover um elemento
família.remove("Edilson")
print(família)

'''
Função id() em Python
A função id() em Python é usada para retornar a identidade única de um objeto. Essa identidade é representada por um número inteiro que corresponde ao endereço de memória onde o objeto está armazenado (embora o valor exato dependa da implementação do Python).
Características principais:

O valor retornado por id() permanece constante durante toda a vida útil do objeto.
É útil para verificar se dois objetos são, de fato, o mesmo (compartilham o mesmo espaço na memória).

Exemplo de uso:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))  # Exibe o ID de 'a'
print(id(b))  # Mesmo ID de 'a', pois 'b' é uma referência a 'a'
print(id(c))  # Diferente, pois 'c' é um novo objeto com o mesmo conteúdo

# Verificando se são o mesmo objeto
print(a is b)  # True
print(a is c)  # False

Quando usar id()?

Para depuração, quando você precisa entender como objetos estão sendo manipulados na memória.
Para confirmar se duas variáveis apontam para o mesmo objeto.

Se precisar de mais exemplos ou explicações, é só avisar! 😊
'''
#Multiplicando elementos de uma lista
nova_lista = [5, 4, 3]
resultado = [x * 5 for x in nova_lista]
print(resultado)

'''
5) Use o slice para criar uma nova lista que inclua apenas os elementos com índice 
3 e 4 da lista a seguir: 
[ 1,2,3,4,5,6 ]  

resultado esperado: [4,5]
'''

#MÉTODO SLICE

lista = [ 1,2,3,4,5,6 ]          #slice você precisa digitar um indice maior parar obter o anterior, se vc que quer como resultado (3,4))
fatiamento = slice(3, 5)         #deve digitar (3,5)
resultado = lista[fatiamento]
print(resultado)








      


















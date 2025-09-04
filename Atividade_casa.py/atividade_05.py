'''
5) Use o slice para criar uma nova lista que inclua apenas os elementos com índice 
3 e 4 da lista a seguir: 
[ 1,2,3,4,5,6 ]  

resultado esperado: [4,5]
'''


lista = [ 1,2,3,4,5,6 ]          #slice você precisa digitar um indice maior parar obter o anterior, se vc que quer como resultado (3,4))
fatiamento = slice(3, 5)         #deve digitar (3,5)
resultado = lista[fatiamento]
print(resultado)


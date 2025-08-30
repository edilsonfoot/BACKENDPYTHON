'''
Dicionário com listas

Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
'''



#Usando as funções "sum" e "len" para encontrar média de cada aluno

notas = {"Ana": [7, 8, 9], "Carlos": [6, 5, 7]}
for aluno in notas:
    media = sum(notas[aluno]) / len(notas[aluno])
    print(aluno, media)

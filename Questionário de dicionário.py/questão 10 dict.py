'''
Ordenando dicionário por valor

Dado o dicionário:

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
'''

#usando os métodos "sorted() e o "".items" auxiliados pelas funções "for" e "in" para ordenar um dicionariopor valor

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
for k, v in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
    print(k, v)


#criando um dicionário

dicionario_vazio = {}                   #no minimo dois elementos
print(type(dicionario_vazio))
print(dicionario_vazio)

dicionario = {
    "Nome": "Edilson",
    "Idade": 52,
    "Nacionalidade": "Brasileiro",
    "Rico": "False",
    "Filmes favoritos": ["Sharknado", "Anaconda 3", "A bala do pistoleiro"],
}
  
dicionario_vazio["PROFISSÃO"] = "Desenvolvedor"
dicionario["filmes favoritos"][1] = "zumbi vs robo"    
print(dicionario)                                          
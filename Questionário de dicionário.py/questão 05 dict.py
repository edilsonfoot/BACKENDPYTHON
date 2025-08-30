'''
Verificando existência de uma chave

Verifique se a chave "telefone" existe no dicionário:

contato = {"nome": "Ana", "email": "ana@email.com"}
'''

#função 
contato = {"nome": "Ana", "email": "ana@email.com"}
contato_buscado = ("telefone")
if contato_buscado in contato:
    print("contato encontrado")
else:
    print("contato não encontrado")

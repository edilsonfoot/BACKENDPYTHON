'''
Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

"Olá, [nome]!"

          Caso o nome não seja informado, mostre "Olá, visitante!".

'''

def função_mensagem(nome):
    if nome:
        return f"Olá, {nome}"
    else:
        return "Olá, visitante"

print(função_mensagem("nome"))
print(função_mensagem(None))






'''
def mensagem(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

def Olá(nome):
    print(f"Olá, {mome}! seja ben-vindo(a)!")
'''


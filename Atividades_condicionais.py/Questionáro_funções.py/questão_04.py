'''
Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

"Olá, [nome]!"

          Caso o nome não seja informado, mostre "Olá, visitante!".
'''

saudação = "Olá, [nome]!"
def Olá(nome = "nome" ):
    if nome:
        return f"Olá, {nome}"
    else:
        return "Olá, visitante"

print(saudação("nome"))
print(saudação())
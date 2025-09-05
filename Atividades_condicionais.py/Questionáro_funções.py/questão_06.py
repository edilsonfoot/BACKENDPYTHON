'''
Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes
'''

def calcular_media(*numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

media = calcular_media(3, 5, 7)
print(f"A média é: {media}")





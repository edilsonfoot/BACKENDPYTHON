'''
3) Escreva um programa que recebe dois números do usuário e depois compara os 
dois imprimindo qual dos dois é o maior. 
'''

# Solicita os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


numero1 = 25.9
numero2 = 20.5

numero1 = float(input("25.9: "))
numero2 = float(input("20.5: "))


# Compara os números e exibe o resultado
if numero1 > numero2:
    print(f"O primeiro número ({numero1}) é maior que o segundo número ({numero2}).")
elif numero2 > numero1:
    print(f"O segundo número ({numero2}) é maior que o primeiro número ({numero1}).")
else:
    print("Os dois números são iguais.")



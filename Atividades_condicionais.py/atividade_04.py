'''
4) Escreva um programa que ler a idade fornecida pelo usuário e imprime: 
● "Criança" (até 12 anos) 
● "Adolescente" (13 a 17 anos) 
● "Adulto" (18 a 64 anos) 
● "Idoso" (65 ou mais) 
'''


idade = int(input("30:"))

if idade >= 65:
    print("Idoso")
elif idade < 64 and idade >= 18:
    print("Adulto")
elif idade < 18 and idade >= 12:   # ELIF é else + if 
    print("Adolescente")
else:                              # ELSE é exceção, não tem condição própria
    print("Criança")







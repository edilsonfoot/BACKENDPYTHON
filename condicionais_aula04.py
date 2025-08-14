idade = int(input("Digite a sua idade: "))

if idade >= 65:
    print("Idoso")
elif idade < 64 and idade >= 18:
    print("Adulto")
elif idade < 18 and idade >= 12:   # ELIF é else + if 
    print("Adolescente")
else:                              # ELSE é exceção, não tem condição própria
    print("Criança")
idade = int(input("Digite a sua idade: "))

if idade >= 65:
    print("Idoso")
elif idade < 64 and idade >= 18:
    print("Adulto")
elif idade < 18 and idade >= 12:   # ELIF é else + if 
    print("Adolescente")
else:                              # ELSE é exceção, não tem condição própria
    print("Criança")


#definindo se um numero é par ou ímpar usando def

    def verificar_par_ou_impar(numero):              #def = defina (se um numero é par ou impar)
    if numero % 2 == 0:                          #if = (se um numero for divissível por dois e diferente de zero, ele é par)
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."

print(verificar_par_ou_impar(1))  
print(verificar_par_ou_impar(76))   




# Solicita os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os números e exibe o resultado
if numero1 > numero2:
    print(f"O primeiro número ({numero1}) é maior que o segundo número ({numero2}).")
elif numero2 > numero1:
    print(f"O segundo número ({numero2}) é maior que o primeiro número ({numero1}).")
else:
    print("Os dois números são iguais.")
Como funciona:
O programa solicita dois números ao usuário.
Ele utiliza estruturas condicionais (if, elif, else) para comparar os números.
Exibe o resultado com base na comparação.



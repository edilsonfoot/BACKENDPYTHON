'''
1) Escreva um programa que peça para o usuário digitar um número e imprima se 
esse número é par ou ímpar. 
'''



def verificar_par_ou_impar(numero):              #def = defina (se um numero é par ou impar)
    if numero % 2 == 0:                          #if = (se um numero for divissível por dois e diferente de zero, ele é par)
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."

print(verificar_par_ou_impar(1))  
print(verificar_par_ou_impar(76))   






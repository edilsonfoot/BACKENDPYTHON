'''
2) Escreva um programa que recebe a nota de um aluno e imprima:  
● "Aprovado" se a nota for ≥ 7, 
● "Recuperação" se estiver entre 5 e 6.9, 
● "Reprovado" se for < 5.
'''


nota = int(input("8: "))

if nota >= 7:
    print(int("Aprovado"))
elif  nota < 5 and nota <= 6.9:
    print(int("Recuperação"))
else:                              # ELSE é exceção, não tem condição própria
    print(int("Reprovado"))




   
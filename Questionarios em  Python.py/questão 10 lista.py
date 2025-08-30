'''
Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.
'''


#lista principal
notas = []

#coletando notas de 2  alunos
for i in range(2):
    aluno_notas = []
    print(f"\ndigite as três notas do aluno {i + 1}:")    #i + 1


    for j in range(3):
        n = float(input("Nota {7.0, 8.0, 9.0}: "))                
        aluno_notas.append(nota) 


notas.append(aluno_notas)
'''
#calculando a média de cada aluno e exibindo-as
for i, aluno in enumerate(notas, start=1):
    media = sum(aluno) / len(aluno)
    print(f"A media do aluno {i} é: {media:.2f}")
'''
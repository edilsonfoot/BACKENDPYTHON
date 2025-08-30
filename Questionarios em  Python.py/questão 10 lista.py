'''
Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.
'''

#coletando notas de 2  alunos

for i in range(2):
    aluno_notas = []
    print(f"\nDigite as 3 notas do aluno {i + 1}:")    


    for j in range(3):
        n = float(input("Nota {j + 1}:"))                
        aluno_notas.append(n) 


n.append(aluno_notas)

#calculando a média de cada aluno e exibindo
for i, aluno in enumerate(n, start=1):
    media = sum(aluno) / len(aluno)
    print(f"A media do aluno {i} é: {media:.2f}")


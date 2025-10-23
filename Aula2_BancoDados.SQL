--SELECT *
--FROM Aluno
--LEFT JOIN Turma
--ON id_turma = Turma.id


--SELECT Aluno.nome. Turma.nome
--FROM Aluno
--RIGHT JOIN Turma
--ON id_turma = Turma.id


SELECT Aluno.nome. Turma.nome
FROM Aluno
RIGHT
 JOIN Turma
ON id_turma = Turma.id
WHERE (Aluno.nota1 + Aluno.nota2)/2 >
= 7

























'''
Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
'''

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"
    
    def __repr__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade})"


p1 = Pessoa("Edilson",53)
p2 = Pessoa("Elisângela",51)
print(p1)
lista = [p1, p2]

print([p1,p2])










'''
        self.cor = cor
        self.altura = altura


    def adicionar_objeto(self, objeto):
        self.objetos.append("cor")

        print(f"Objeto {objeto} adicionado com sucesso!
'''











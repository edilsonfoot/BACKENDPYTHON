class Pessoa:  
    def __init__(self,nome,idade,profissão):
        self.nome = nome
        self.idade = idade
        self.profissão = profissão

    def __str__(self):
        print(self.nome)



user2 = Pessoa("Fred", 36, "Desenvolvedor")
user1 = Pessoa("João", 25, "PO")


usuarios = []

usuarios.append(user1. __str__())
usuarios.append(user2)

print(usuarios)

print(usuarios[0].nome)








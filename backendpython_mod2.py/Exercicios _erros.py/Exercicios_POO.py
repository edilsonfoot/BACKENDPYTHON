'''
Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
'''
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

print(lista)                               # esperava que ele imprimisse os dois objetos, 
'''

'''
Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.
'''

'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Testando o método apresentar()
p1 = Pessoa("João", 25)
p1.apresentar()                                       #aqui não deveria apresentar a função anterior junto com o novo método?
'''     
    


'''
Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.
'''

'''
class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Slef: {self.marca}\nNome: {self.modelo}\nModelo: {self.ano}"   
    

Onix = Carro("Chevrolet", "Onix", 2018)
'''

'''
Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
'''

'''
class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

        self.marca = "Chevrolet"
        self.modelo = "Onix"
        self.ano = 2018
        
        self.ano1 = 2018
        self.ano2 = 2020

    def excluir_objeto(self, id):
        if id in self.objetos:
           del self.objetos[id]
           print(f"Objeto com ID {id} foi excluído.")
'''

'''
Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
'''

'''
import datetime

class ContaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.operacoes = []

    def __str__(self):
        return f"ContaBancaria(titular {self.titular} tem {self.saldo} de saldo)"
    
    def __repr__(self):
        return f"ContaBancaria(titular={self.titular!r}, saldo={self.saldo!r})"

    def deposito(self, valor):
        self.saldo += valor
        self.registra_operacao("deposito", valor)
        print(f"Foi depositado {valor} reais na sua conta")
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registra_operacao("saque", valor)
            print(f"Foi sacado {valor} reais na sua conta")
        else:
            print("Saldo insuficiente para saque.")

    def extrato(self):
        for index, operacao in enumerate(self.operacoes):
            print(f"{index+1}. {operacao[0]} - {operacao[1]}: {operacao[2]}")
        print(f"Saldo: {self.saldo}")

    def registra_operacao(self, tipo, valor):
        data_operacao = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        self.operacoes.append([data_operacao, tipo, valor])
    
conta1 = ContaBancaria("Edilson")
print(conta1)

conta1.deposito(500)
conta1.saque(100)
'''

'''
Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.
'''

'''
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def verificar_saldo(self, valor):
        """
        Verifica se o saldo é suficiente para realizar uma operação.
        Retorna True se o saldo for suficiente, caso contrário False.
        """
        return self.saldo >= valor

# Exemplo de uso
conta = ContaBancaria("João", 500)

# Verificar se é possível sacar 300
print(conta.verificar_saldo(300))  # Saída: True

# Verificar se é possível sacar 600
print(conta.verificar_saldo(600))  # Saída: False
'''

'''
Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.
'''

'''
class Aluno:

    def __init__(self, aluno, nota):
        self.aluno = aluno
        self.nota = nota


class Turma:

    def __init__(self, alunos=None):
        if alunos is None:
            self.alunos = []
        else:
            self.alunos = alunos

    # adicionando aluno
    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            print(f"Aluno {aluno.aluno} adicionado à turma.")
        else:
            print("Erro: O objeto fornecido não é um aluno válido.")
'''

'''
Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.
'''

class Aluno:

    def __init__(self, nome:str, nota:float):     # Método construtor
        self.nome = nome
        self.nota = nota

        self.nome = "Maria"
        self.nota = 9.5

    def __str__(self):
        return f"Aluno: {self.aluno}\nNome: \n:Nota{self.nota}"
    
    







 














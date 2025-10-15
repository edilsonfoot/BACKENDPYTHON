'''
Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.
'''

'''
# Classe Pessoa representando uma pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # Inicialmente a pessoa não possui livros
        self.livros = []
    
    # Método para adicionar um livro à pessoa
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    # Método para mostrar livros da pessoa
    def mostrar_livros(self):
        if not self.livros:
            print(f"{self.nome} não possui livros.")
        else:
            print(f"Livros de {self.nome}:")
            for livro in self.livros:
                print(f"- {livro.titulo} de {livro.autor}")

# Classe Livro representando um livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Demonstração da associação
if __name__ == "__main__":
    # Criando instâncias de Pessoa
    pessoa1 = Pessoa("Elisangela", 51)
    pessoa2 = Pessoa("Edilson", 53)
    
    # Criando instâncias de Livro
    livro1 = Livro("1984", "George Orwell")
    livro2 = Livro("Dom Casmurro", "Machado de Assis")
    livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
    
    # Associando livros às pessoas
    pessoa1.adicionar_livro(livro1)
    pessoa1.adicionar_livro(livro2)
    pessoa2.adicionar_livro(livro3)
    
    # Mostrando os livros de cada pessoa
    pessoa1.mostrar_livros()
    pessoa2.mostrar_livros()
'''


'''
Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.
'''

''''
class Onibus:
    def __init__(self, numero, capacidade):
        self.numero = numero          # Número do ônibus
        self.capacidade = capacidade  # Capacidade máxima de passageiros
        self.passageiros = []         # Lista de passageiros

    def embarcar(self, aluno):
        if len(self.passageiros) < self.capacidade:
            self.passageiros.append(aluno.nome)
            print(f"{aluno.nome} embarcou no ônibus {self.numero}.")
        else:
            print(f"Ônibus {self.numero} está cheio! {aluno.nome} não pode embarcar.")

    def mostrar_passageiros(self):
        print(f"Passageiros no ônibus {self.numero}: {self.passageiros}")


class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método que utiliza a classe Onibus
    def pegar_onibus(self, onibus: Onibus):
        print(f"{self.nome} está tentando pegar o ônibus {onibus.numero}...")
        onibus.embarcar(self)

aluno1 = Aluno(nome="Maria", idade=16)
aluno2 = Aluno(nome="João", idade=17)
aluno3 = Aluno(nome="Ana", idade=15)

# Criando uma instância de Onibus antes de usá-la
onibus1 = Onibus(numero=101, capacidade=2)

aluno1.pegar_onibus(onibus1)
aluno2.pegar_onibus(onibus1)
aluno3.pegar_onibus(onibus1)
'''


'''
Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.
'''

'''
class Funcionario:
    def __init__(self, nome, salario, data_admissao):
        self.nome = nome
        self.salario = salario
        self.data_admissao = data_admissao

    def __str__(self):
        return f"Nome: {self.nome}, Salário: R${self.salario:.2f}, Data de Admissão: {self.data_admissao}"


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.funcionarios.append(funcionario)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância da classe Funcionario.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            return "Nenhum funcionário neste departamento."
        return "\n".join(str(funcionario) for funcionario in self.funcionarios)

    def calcular_total_salarios(self):
        return sum(funcionario.salario for funcionario in self.funcionarios)


# Exemplo de uso
if __name__ == "__main__":
    # Criando funcionários
    funcionario1 = Funcionario("Ana Silva", 3000.00, "2023-01-15")
    funcionario2 = Funcionario("Carlos Souza", 4500.00, "2022-06-10")
    funcionario3 = Funcionario("Maria Oliveira", 5000.00, "2021-03-20")

    # Criando departamento
    departamento = Departamento("Recursos Humanos")

    # Adicionando funcionários ao departamento
    departamento.adicionar_funcionario(funcionario1)
    departamento.adicionar_funcionario(funcionario2)
    departamento.adicionar_funcionario(funcionario3)

    # Listando funcionários
    print(f"Funcionários no departamento {departamento.nome}:")
    print(departamento.listar_funcionarios())

    # Calculando total de salários
    print(f"\nTotal de salários pagos pelo departamento: R${departamento.calcular_total_salarios():.2f}")
'''


'''
Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.
'''

'''
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"Jogador: {self.nome}, Posição: {self.posicao}"

class Time:
    def __init__(self, nome_time):
        self.nome_time = nome_time
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        if not self.jogadores:
            return "Nenhum jogador no time."
        return "\n".join(str(jogador) for jogador in self.jogadores)

    def __str__(self):
        return f"Time: {self.nome_time}, Jogadores: {len(self.jogadores)}"


# Exemplo de uso
if __name__ == "__main__":
    # Criando jogadores
    jogador1 = Jogador("Carlos", "Atacante")
    jogador2 = Jogador("João", "Goleiro")

    # Criando um time
    time = Time("Estrelas FC")

    # Adicionando jogadores ao time
    time.adicionar_jogador(jogador1)
    time.adicionar_jogador(jogador2)

    # Exibindo informações do time
    print(time)
    print(time.listar_jogadores())
'''


'''
Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto.
'''

'''
# Classe Motor, criada dentro da classe Carro
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        print(f"Motor de {self.potencia} cavalos criado.")
    
    def __del__(self):
        print("Motor destruído.")

# Classe Carro que possui um Motor
class Carro:
    def __init__(self, marca, potencia_motor):
        self.marca = marca
        self.motor = Motor(potencia_motor)  # Criação do Motor dentro do Carro
        print(f"Carro {self.marca} criado com motor de {self.motor.potencia} cavalos.")
    
    def __del__(self):
        print(f"Carro {self.marca} destruído.")

# Testando a criação e destruição do Carro e Motor
print("Criando o carro...")
meu_carro = Carro("Toyota", 120)

print("
Apagando o carro...")
del meu_carro  # Quando o carro é deletado, o motor também é destruído automaticamente
'''


'''
Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.
'''


# Classe Comodo representa um cômodo individual
class Comodo:
    def __init__(self, nome, area):
        self.nome = nome  # Nome do cômodo, ex: "Sala"
        self.area = area  # Área em metros quadrados

    def __str__(self):
        return f"{self.nome} ({self.area} m²)"

# Classe Casa contém vários cômodos
class Casa:
    def __init__(self, endereco):
        self.endereco = endereco  # Endereço da casa
        self.comodos = []  # Lista de cômodos

    # Adiciona um novo cômodo à casa
    def adicionar_comodo(self, nome, area):
        comodo = Comodo(nome, area)
        self.comodos.append(comodo)

    # Retorna uma lista com os nomes de todos os cômodos
    def listar_comodos(self):
        if not self.comodos:
            return "A casa não possui cômodos cadastrados."
            return "\n".join(str(comodo) for comodo in self.comodos)

# Exemplo de uso
if __name__ == "__main__":
    minha_casa = Casa("Rua das Flores, 123")
    
    # Adicionando cômodos à casa
    minha_casa.adicionar_comodo("Sala", 20)
    minha_casa.adicionar_comodo("Cozinha", 15)
    minha_casa.adicionar_comodo("Quarto", 12)
    minha_casa.adicionar_comodo("Banheiro", 5)
    
# Listar todos os cômodos
print(f"Endereço da casa: {minha_casa.endereco}")
print("Cômodos da casa:")
print(minha_casa.listar_comodos())
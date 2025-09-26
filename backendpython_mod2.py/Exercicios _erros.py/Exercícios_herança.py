'''
Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.
'''


class Usuario:

    def __init__(self, nome, email):
        self.nome = "nome"
        self.email = "email"

    def contatos(self):
        print("nome, email")


# Classe Filha que herda de usuario
class Cliente(Usuario):
    def __init__(self, nome, email, celular):
        # Chama o construtor da classe pai para inicializar os atributos herdados
        super().__init__(nome, email)
        self.celular = celular # Atributo específico do cliente



'''
Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.
'''
'''
class Usuario:

    def __init__(self, nome, email):
        self.nome = "nome"
        self.email = "email"

    def contatos(self):
        print("nome, email")

def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        
class Cliente(Usuario):
    def __init__(self, nome, email, celular):
        super().__init__(nome, email)
        self.celular = celular 

def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"celukar: {self.celular}")

def __call__(self):
        print(f"O método foi chamado! Olá, {self.nome}!")
'''


'''
Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
'''

'''
class Usuario:

    def __init__(self, nome, email):
        self.nome = "nome"
        self.email = "email"

    def contatos(self):
        print("nome, email")


def saudacao(self):
 return f"Olá, {self.nome}! Seja bem-vindo(a)!" # Método de saudação
'''



'''
Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().
'''

'''
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def contatos(self):
        print(f"{self.nome}, {self.email}")

    def saudacao(self):
        return f"Olá, {self.nome}! Seja bem-vindo(a)!"

class Cliente(Usuario):
    def __init__(self, nome, email, celular):
    # Chama o construtor da classe pai para inicializar os atributos herdados
        super().__init__(nome, email)
        self.celular = celular                  # Atributo específico do cliente

    # Função para adicionar um novo atributo
    def adicionar_atributo(self, nome_saldo, valor):
        setattr(self, nome_saldo, valor)        
'''


'''
Crie uma classe Funcionario que herda de Us:uario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.
'''

'''
# Classe base Usuario
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

#Classe Funcionario que herda de Usuario
class Funcionario(Usuario):
    def init(self, nome, email, salario):
     super().init(nome, email)  # Chama o construtor da classe Usuario
     self.salario = salario

#Classe Gerente que herda de Funcionario
class Gerente(Funcionario):
    def init(self, nome, email, salario, departamento):
     super().init(nome, email, salario)  # Chama o construtor da classe Funcionario
     self.departamento = departamento

#Instanciando um objeto da classe Gerente
gerente = Gerente("Eraldo Silva", "eraldo.silva@email.com", 8000, "Financeiro")

#Acessando os atributos do gerente
print(f"Nome: {gerente.nome}")
print(f"Email: {gerente.email}")
print(f"Salário: R${gerente.salario}")
print(f"Departamento: {gerente.departamento}")
'''

'''
Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?
'''


'''
# Classe Autenticacao
class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            return "Login bem-sucedido!"
        return "Usuário ou senha incorretos."
    

#Classe Permissao
class Permissao:
    def verificar_permissao(self, usuario):
     if usuario == "admin":
      return "Permissão concedida."
     return "Permissão negada."
    
#Classe Administrador herdando de Autenticacao e Permissao

class Administrador(Autenticacao, Permissao):
 pass

# Usando os métodos herdados
admin = Administrador()

# Testando o método login()
resultado_login = admin.login("admin", "1234")
print(resultado_login)  # Saída: Login bem-sucedido!

# Testando o método verificar_permissao()
resultado_permissao = admin.verificar_permissao("admin")
print(resultado_permissao)  # Saída: Permissão concedida.
'''


'''
Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.
'''

'''
# Classe Autenticacao
class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            return "Login bem-sucedido!"
        return "Usuário ou senha incorretos."
    
    def status(self):
        print(f"Usuario: {self.usuario}, senha: {self.senha}")
    

#Classe Permissao
class Permissao:
    def verificar_permissao(self, usuario):
     if usuario == "admin":
      return "Permissão concedida."
     return "Permissão negada."
    
def status(self):
        print(f"Usuario: {self.usuario}")

    
#Classe Administrador herdando de Autenticacao e Permissao

class Administrador(Autenticacao, Permissao):
 pass

#Classe Permissao
class Permissao:
    def verificar_permissao(self, usuario):
     if usuario == "admin":
      return "Permissão concedida."
     return "Permissão negada."
    
#Classe Administrador herdando de Autenticacao e Permissao

class Administrador(Autenticacao, Permissao):
 pass
'''























                                        

                                                                                                                                                   

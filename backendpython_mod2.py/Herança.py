'''
# Classe Pai
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("Acelerando o veículo...")

# Classe Filha que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        # Chama o construtor da classe pai para inicializar os atributos herdados
        super().__init__(marca, modelo)
        self.cor = cor # Atributo específico do Carro

    def ligar_radio(self):
        print("Ligando o rádio do carro...")

# Cria um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", "Vermelho")

# Acesso a métodos e atributos herdados
print(meu_carro.marca) # Saída: Toyota
meu_carro.acelerar()   # Saída: Acelerando o veículo...

# Acesso a um atributo e método específicos da classe Carro
print(meu_carro.cor) # Saída: Vermelho
meu_carro.ligar_radio() # Saída: Ligando o rádio do carro...
'''




class Personagem: 
  def __init__(self, nome, vida): 
      self.nome = nome
      self.vida = vida


  class Heroi(Personagem):  
      def __init__(self, nome, vida, habilidade):
          super().__init__(nome, vida)
          self.habilidade = habilidade


  class Vilao(Personagem):  # Adicionando a classe Vilão
      def __init__(self, nome, vida, poder):
          super().__init__(nome, vida)
          self.poder = poder


  def atacar(personagem):  # Função para atacar, pode ser chamada por heróis ou vilões
      print(f"{personagem.nome} está atacando!")


  heroi1 = Heroi("Superman", 100, "Voo")  
  vilao1 = Vilao("Lex Luthor", 80, "Inteligência")


  atacar(heroi1)  # Chamando a função atacar() com um herói
  atacar(vilao1)  # Chamando a função atacar() com um vilão









'''
Crie uma interface chamada Pagamento com um método abstrato processar(valor). Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. Mostre como chamar processar() para cada uma.

Interface múltipla
'''

'''
from abc import ABC, abstractmethod

# Definição da interface
class Pagamento(ABC):

    @abstractmethod
    def processar(self, valor):
        """Método abstrato para processar pagamento"""
        pass

# Implementação da interface por CartaoCredito
class CartaoCredito(Pagamento):
    
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} no cartão de crédito... Pagamento aprovado!")

# Implementação da interface por Boleto
class Boleto(Pagamento):
    
    def processar(self, valor):
        print(f"Gerando boleto no valor de R${valor:.2f}... Boleto emitido com sucesso!")

# Função para demonstrar pagamento usando interface múltipla
def realizar_pagamento(pagamento: Pagamento, valor):
    pagamento.processar(valor)

# Exemplo de uso
if __name__ == "__main__":
    cartao = CartaoCredito()
    boleto = Boleto()
    
    # Chamando processar para Cartão de Crédito
    realizar_pagamento(cartao, 450.00)
    
    # Chamando processar para Boleto
    realizar_pagamento(boleto, 500.00)
'''

'''
Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). Crie uma classe Computador que implemente ambas. Mostre seu uso.

Interface em herança múltipla
'''

'''
from abc import ABC, abstractmethod

# Interface Ligavel
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

# Interface Desligavel
class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

# Classe Computador implementando ambas as interfaces
class Computador(Ligavel, Desligavel):
    def __init__(self):
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("Computador ligado.")
        else:
            print("O computador já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Computador desligado.")
        else:
            print("O computador já está desligado.")

# Demonstração de uso
if __name__ == "__main__":
    meuPC = Computador()
    meuPC.ligar()     # Saída: Computador ligado.
    meuPC.ligar()     # Saída: O computador já está ligado.
    meuPC.desligar()  # Saída: Computador desligado.
    meuPC.desligar()  # Saída: O computador já está desligado.
'''


'''
Crie uma interface Imprimivel com o método imprimir(). Crie outra interface Exportavel com o método exportar(). Implemente uma classe Relatorio que herde de ambas e implemente os métodos.
Forçando contrato.
'''


'''
from abc import ABC, abstractmethod

# Interface Imprimivel
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        """Método que deve ser implementado para imprimir conteúdo"""
        pass

# Interface Exportavel
class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        """Método que deve ser implementado para exportar conteúdo"""
        pass

# Classe Relatorio que implementa ambas as interfaces
class Relatorio(Imprimivel, Exportavel):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def imprimir(self):
        # Implementação do método imprimir
        print(f"Imprimindo relatório: {self.conteudo}")

    def exportar(self):
        # Implementação do método exportar
        filename = "relatorio.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.conteudo)
        print(f"Relatório exportado para {filename}")

# Exemplo de uso
if __name__ == "__main__":
    relatorio = Relatorio("Dados importantes do mês de outubro")
    relatorio.imprimir()
    relatorio.exportar()
'''

'''
Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. O que acontece quando você tenta instanciá-la? Corrija o código.
'''


# Definindo a interface Repositorio usando Python
from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

# Classe de exemplo para armazenar
class Objeto:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

# Implementação correta da classe RepositorioMemoria
class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.armazenamento = {}

    def salvar(self, objeto):
        self.armazenamento[objeto.get_id()] = objeto

    def buscar(self, id):
        return self.armazenamento.get(id)

# Teste de uso
if __name__ == "__main__":
    repositorio = RepositorioMemoria()

    obj1 = Objeto(1, "Objeto 1")
    repositorio.salvar(obj1)

    resultado = repositorio.buscar(1)
    if resultado:
        print("Buscado id 1:", resultado.get_nome())
    else:
        print("Objeto não encontrado.")








class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print("Carro já está ligado, nada acontece")
        else:
            print("Carro ligado")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print("Carro desligado")
            self.ligado = False
        else:
            print("Carro já está desligado, nada acontece")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade}km/h")
        else:
            print("Não é possível acelerar, carro desligado")

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade}km/h")
        else:
            print("Não é possível frear, carro desligado")


fusca = Carro("Volks", "Fusca", "Azul", "Gasolina")

fusca.ligar()
fusca.ligar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()              
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.frear()
fusca.desligar()


ferrari = Carro("ferrari", "ferrari 911", "Vermalha", "Gasolina")
Tesla = Carro("Tesla", "Cibertruck", "Cinza", "Eletrico")





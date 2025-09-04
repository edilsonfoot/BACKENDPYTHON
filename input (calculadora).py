nome = input("digite seu nome: ")                        #criando uma calculadora
idade = int(input(f"qual a sua idade {nome}?"))    

nascimento = 2025 - idade

print(f"{nome} você nasceu em {nascimento}")



num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero "))
resultado = num1 + num2

print(f"resultado é: {resultado}")


Aqui está um exemplo simples de uma função de calculadora em Python que realiza as quatro operações básicas: adição, subtração, multiplicação e divisão.
def calculadora():
    print("Bem-vindo à Calculadora!")
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Solicita ao usuário que escolha uma operação
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    # Solicita os números para a operação
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return

    # Realiza a operação com base na escolha
    if escolha == '1':
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif escolha == '2':
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif escolha == '3':
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif escolha == '4':
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Por favor, escolha entre 1, 2, 3 ou 4.")

# Chama a função calculadora
calculadora()

Explicação:

O programa apresenta um menu com as operações disponíveis.
O usuário escolhe a operação e insere dois números.
A função realiza a operação correspondente e exibe o resultado.
Inclui tratamento de erros para entradas inválidas e divisão por zero.

Você pode expandir essa função para incluir mais operações ou até mesmo criar uma interface gráfica, dependendo das suas necessidades! 😊
      



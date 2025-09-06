'''
Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.
'''


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
        if nmit -mum2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Por favor, escolha entre 1, 2, 3 ou 4.")

# Chama a função calculadora
calculadora()


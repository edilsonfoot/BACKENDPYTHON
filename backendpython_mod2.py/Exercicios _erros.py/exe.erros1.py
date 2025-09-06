'''
1.Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.
'''
try:
  
   numero = int(input("Digite um numero inteiro: "))
   print(f"Voce digitou {numero}")
except ValueError:
   print("Erro: isoo não é um numero inteiro")  
'''
    
'''
# 2.Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.


def multiplicar_numeros():
     try:
        # Solicita os dois números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
     except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
'''

'''
# 3.Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
'''
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: O valor digitado não é um número inteiro.")
else:
    print(f"Você digitou o número inteiro: {numero}")

'''
4.Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.
'''

try:
    arquivo = open("dados.txt", "w")
    arquivo.write("Exemplo de escrita no arquivo.\n")
except Exception as e:
    print(f"Ocorreu um erro ao abrir ou escrever no arquivo: {e}")
finally:
    print("Encerrando programa")
    if 'arquivo' in locals():
        arquivo.close()
'''

5.Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("não é posssível dividir por zero.")
    return a / b
print(dividir(20, 4))
print(dividir(20, 0))





6.Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.


class IdadeInvalidaError(Exception):
    pass
    
def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("A idade não pode ser negativa!")
    print(e)
    return f"Idade {idade} cadastrada com sucesso."

print(cadastrar_idade(30))    
   print(cadastrar_idade(-3))


   
'''
7.Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:
'''

try:
    
   a = int(input("Digite o primeiro número: "))
   b = int(input("Digite o segundo número: "))
   resultado = a / b
except ValueError:
    print("Erro: você deve digitar números válidos.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
else:
    print(f"O resultado da divisão é{resultado}")   
'''



'''
8.Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
'''
'''
try para a conversão,

else para verificar se é par ou ímpar,
finally para exibir "Fim do programa".
'''


'''
try:
    # Solicita ao usuário um número inteiro
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
else:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
finally:
    # Mensagem final exibida independentemente do que aconteceu
    print("Fim do programa.")
'''


'''
9.Crie uma função sacar(saldo, valor) que:
Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.

class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para saque.")
    return saldo - valor

saldo_atual = 100

try:
    novo_saldo = sacar(saldo_atual, 150)
    print(f"Saque realizado.  Novo saldo: {novo_saldo}")
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
'''

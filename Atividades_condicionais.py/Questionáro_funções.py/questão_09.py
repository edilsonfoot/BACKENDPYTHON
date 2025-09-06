'''
Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:
'''

def soma(a, b): return a + b

def aplicar_operacao(a, b, func):
    return func(a, b)
def soma(num1, num2):
    return num1+num2
def multiplicacao(num1, num2):
    return num1*num2

# Exemplo de uso com multiplicação
print(aplicar_operacao(3, 4, multiplicacao))


aplicar_operacao = multiplicacao(soma(3,4), soma(3,4))
print(aplicar_operacao)







'''
def soma(a, b): return a + b

def aplicar_operacao(a, b, func):
	return func(a, b)

print(aplicar_operacao(3, 4, soma)
'''






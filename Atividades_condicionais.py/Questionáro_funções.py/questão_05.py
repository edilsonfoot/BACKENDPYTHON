'''
Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.
'''

#função de adição retornando a soma
def operações(num1, num2):
    return operações(num1 + num2)

#função de subtração
def operações(a, b):
    return operações(a - b)

#função muultiplicação
def operações(num1, num2):
    return operações(num1 *num2)

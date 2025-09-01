#fUNÇÃO DAS FUNÇÕES É EVITAR A REPETIÇÃO E MODULARIZAR O CÓDIGO

#Funções arquivos separados (print, str,...)
'''
nome_funcao():
    print("Olá mundo")
'''  
    
'''
def ola():
     print("ola mundo")
     
def ola (msg):
     print(msg)  
     
ola("ola mundo")       
       
       
def ola(msg, numero): 
    print(msg + numero)  
    
ola("ola mundo", "2")       
print(casa)

def soma(num1 + num2):
    valor_somado = (num1+num2):
    print(valor_somado)
'''  

'''
valor = soma(2, 2)
print(f"A soma retornou: {valor}")

   
def soma(num1, num2):
    global valor_somado
    valor_somado = num1+num2
    if valor_somado >= 1:
        return "maior que 1"
    if valor_somado <= 1:
        return"menor que 1"
    
    
valor = soma(0,1)
print(valor_somado)
print(f" retorna valor <1")    
'''

# como funciona:
    # def nome_da_funcao(parametros):
        # instrução 1
        # instrução 2
        # instrução 3
        # return valor (opcional)
         
        
def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2

    return imposto


preço_produto1 = 2500
preço_produto2 = 3500
imposto_produto1 = calcular_imposto(preço_produto1)
imposto_produto2 = calcular_imposto(preço_produto2)

















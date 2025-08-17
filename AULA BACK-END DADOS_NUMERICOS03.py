num1 = 5            #string int
num2 = 3.5          #string float

print(type(num1))
print(type(num2))

a = float(num1)      #transformar string int para float
print(a)
print(type(a))
 
b = int(num2)         #transforma string float em int
print(b)
print(type(b))        #sempre arredonda pra baixo, neste caso de 3.5 para 3

a = "5"
b = "3.5"

print(type(a))
print(type(b))

a = "5"
a = int("5")           #transformando uma string em int (inteiro)
a = float("5")         #transformando uma string em float (flutuante ou decimal)

a = int(float("5.3"))  #se precisar deste numero ineiro, primeiro transfomar pra float e depoispara inteiro
b = "3.5"


print(num1 + num2) 
print(num1+num2)
                           # Operadores aritimeticos
num1 - num2
print(num1-num2)

num1 * num2
print(num1*num2)

num1 / num2
print(10 / 3)

num1 // num2
print(10 // 3)

num1 ** num2
print(2 ** 3)

print(3 + 5 *7 + 3)
print((3+5) * (7+3))
        

print(abs(-15))                 #funções
print(pow(3,3))
print(max(1,85,17,-55,5))
print(min(1,85,17,-55,5))
print(round(8.8))

import math                     # biblioteca de matamática

print(math.floor(8.999))        # arredondamento pra baixo (fllor =chão)
print(math.ceil(8.000001))      # arrendondar pra cima (ceil = céu)
print(math.sqrt(9))             #raiz quadradada

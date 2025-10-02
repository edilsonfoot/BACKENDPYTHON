#função lambda elevando um numero ao quadrado.      #função lambda é escrita numa unica linha.

[]lambda num: num ** 2  
                       #primeira parte (chave)  (1 lambda)
lambda num_1, num_2: (num_1, + num_2) **2        #segunada parte (parametro seguido por dois pontos). (num)

def square(num):                                    #square = quadrado
    return num ** 2                                #terceira parte (dois pontos )

def cube (num):                                    #cube = cubo
            return num ** 3
            
def transform_list(nums_list, transform_item):
  transformed_0 = transform_item(nums_list[0])
  transformed_1 = transform_item(nums_list[1])
  return [transformed_0, transformed_1]|

my_list = [2, 3]
transform_list(my_list, square)                #para transformar em cubo é só subistituir square por cube

[4, 9]                                         #[8, 9]  transformando em cubo


transform_lis([2, 3], lambda num: num ** 3)|   #transformando uma função simples em cubo 

[8, 27]


#como usar as funções map()  filter()

nums_list = [2, 3, 4, 5, 6]

(map(lambda num: num ** 3, nums_list))|             #usando (map)

<map at 0x7ed754c1d930>                             #mostrou o código

list(map(lambda num: num ** 3, nums_list))|          
[8, 27, 64, 125, 216]


#filter()

filter(lambda num: num % 2 == 0)             #diferente de map, filter precisa de um argumento
                                             #retornando true ou false (true inclui na lista)
[2, 4, 6]                                     












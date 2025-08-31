#match = expressão

'''
num = input("imforme um numero de 1 a 5: ")
match num:
    case "1" 
        print(f'você digitou {num}")
    case "2" 
        print(f'você digitou {num}")     
    case "3" 
        print(f'você digitou {num}")                
    case "4" 
        print(f'você digitou {num}")
    case "0"  
'''  
            


''''
#dias da semana 

def dia_semana(dia):
    if dia == 1:
        return " domingo"

    elif dia == 2:
        return "segunda"
    elif dia == 3:
        return "terça-feira"
    elif dia == 4:
        return "quarta-feira"
    elif dia == 5:
        return "quinta-feira"    
    elif dia == 6:
        return "sexta-feira"
    elif dia == 7:
        return "sábado"    
    else:
        return "valor {} invalido".format(dia)          
       dia_semana() > if dia == 1
''''''


def dia_semana(dia):
    match dia:
           case 1:
               return " domingo"
           case 2:
               return "segunda"
           case 3:
               return "terça-feira"
           case 4:
               return "quarta-feira"
           case 5:
               return "quinta-feira"    
           case  6:
               return "sexta-feira"
           case 7:
               return "sábado"  
           case _:
              return "valor {} inválido".format(dia)
    

print(dia_semana(1))
print(dia_semana(5))

       


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
        dia_semana()  >  dia == 1

       

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
print(dia_semana(7))
print(dia_semana({}))       
print(dia_semana(6))
print(dia_semana(3))
print(dia_semana(2))
print(dia_semana(4))


def mês_ano(mês):
    match mês:
        case 1:
            return "janeiro"
        case 2:
            return "fevereiro"
        case 3:
            return "março"
        case 4:
            return "abril"
        case 5:
            return "maio"
        case 6:
            return "junho"
        case 7:
            return "julho"
        case 8:
            return "agosto"
        case 9:
            return "setembro"
        case 10:
            return "outubro"
        case 11:
            return "novembro"
        case 12:
            return "dezembro"
        case _:
            return "valor {} inválido".format(mês)
        
        
print(mês_ano(1))
print(mês_ano(2))
print(mês_ano(4))
print(mês_ano(5))
print(mês_ano(6))
print(mês_ano(7))
print(mês_ano(8)) 
print(mês_ano(9))
print(mês_ano(10))
print(mês_ano(11))
print(mês_ano(12))
print(mês_ano({}))

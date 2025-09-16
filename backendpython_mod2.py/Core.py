import utils.classes



users = []
print("Y miniblog\nBem vindo")
while True:
    print()
    print("1 login")
    print("2 criar usuário")
    opção = input("opção: ")
    match(opção):
        case "1":
            user_name = input("Nome do Usuaário")
            user_password = input("Senha")
            for user in users:
                if user.user_name and user.password == user_password:
                    print("bem vindo user.user_name")
                    while True:
                        print("opções")
                        "1- Visualizar perfil"\
                        
                else:
                    print("Informações erradas")

        case "2":    
            user_name = input("Nome do Usuaário")
            user_password = input("Senha")
            user_email = input("email: ")
            users.append(utils.classes.User(user_name,user_password, user_email))
            print(users)

        case  "0":

      





class user:
    def __init__(self, user_name,password, email):
        self.user_name = user_name
        self.__passsword = password
        self.email = email

    def __str__(self):
        return f"Usuários: {self.user_name}, Email: {self.email}"
    
    def __repr__(self):
        return f"{"User._qualname__}: (user__name: {self.user__name}"
    
    def seguir(self, user_name, users):
        if not user.user_name == user_name:
            print("Usuário não existe")
        if user_name not in self.seguidores:    
            self.seguidores.append(user_name)
    


user01 = user("fred", "1234", "fred@fred.com")
user02 = user("Maria", "4321", "maria@gmail.com")
users = [user01, user02] 

user01.seguir("Maria")
print(user01.seguidores)
                  
class LoginValidationError(Exception):
    pass

class User():
    username: str
    password: str
    is_valid: bool = False

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.validate_new_user()
    
    def validate_new_user(self):
        try:
            if len(self.username) < 5:
                raise LoginValidationError("O nome de usuário deve conter pelo menos 5 caracteres.")
            
            if len(self.password) < 8:
                raise LoginValidationError("A senha deve conter pelo menos 8 caracteres.")
            
            self.is_valid = True
        
        except LoginValidationError as err:
            self.is_valid = False
            print(str(err))
    

while True:
    username = input("Digite seu nome de usuário\t->")
    password = input("Digite sua senha\t->")

    user = User(username, password)
    if user.is_valid:
        print("\nCadastro realizado com sucesso!")
        break
    
    print('') #espaço adicional

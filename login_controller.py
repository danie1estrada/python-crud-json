from user_controller import UserController

class LoginController:
    def __init__(self):
        self.controller = UserController()

    def login(self, username, password):
        user = self.controller.find(username)

        if not user:
            raise Exception('Usuario no existe')

        if not user.password == self.controller.encrypt_password(password):
            raise Exception('Contraseña incorrecta')

        return user
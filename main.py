from user_controller import UserController
from login_window import LoginWindow
from user import User

def menu():
    controller = UserController()
    
    while True:
        [print(it) for it in '\n1. Leer usuarios,2. Crear usuario,3. Editar usuario,4. Eliminar usuario,5. Salir'.split(',')]
        
        selected = input('\nSeleccione una opción: ')
        while True:
            if selected in [str(i) for i in range(1, 5)]:
                { '1': read, '2': create,'3': update, '4': delete }[selected](controller)
                break
            elif selected == '5':
                return
            selected = input('Seleccione una opción válida: ')

def create(controller):
    username = input('Ingrese el usuario: ')
    name = input('Ingrese el nombre: ')
    role = input('Ingrese el rol: ')
    password = password_input(controller)
    
    try:
        controller.create(User(username, name, role, password))
    except:
        print('Error: El usuario ya existe')
    
def read(controller):
    [print(user.to_string()) for user in controller.get_users()]

def update(controller):
    username = input('Ingrese el usuario a editar: ')
    user = controller.find(username)
    if user:
        user.name = input('Ingrese el nuevo nombre: ')
        user.role = input('Ingrese el nuevo rol: ')
        user.password = password_input(controller)
        controller.update(user)
    else:
        print('Error: El usuario que intenta editar no existe')

def delete(controller):
    username = input('Ingrese el usuario a eliminar: ')
    user = controller.find(username)
    if user:
        controller.delete(user)
    else:
        print('Error: El usuario que intenta eliminar no existe')

def password_input(controller):
    password = input('Ingrese la contraseña: ')
    while True:
        if len(password) == 4 and password.isdigit():
            return controller.encrypt_password(password)
        password = input('Ingrese una contraseña válida: ')

if __name__ == '__main__':
    # menu()
    LoginWindow().main()
import hashlib

class User:
    def __init__(self, username='', name='', role='', password=''):
        self.username = username
        self.name = name
        self.role = role
        self.password = password

    def to_dict(self):
        return {
            'username': self.username,
            'name': self.name,
            'role': self.role,
            'password': self.password
        }

    def to_string(self):
        return f'Usuario: {self.username}, Nombre: {self.name}, Rol: {self.role}'

    def encrypt_password(self):
        self.password = hashlib.md5(bytes(self.password, encoding='utf-8')).hexdigest()
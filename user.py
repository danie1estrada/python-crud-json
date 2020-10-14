from dataclasses import dataclass, asdict

@dataclass
class User:
    username: str
    name: str
    role: str
    password: str

    def to_dict(self):
        return asdict(self)

    def to_string(self):
        return f'Usuario: {self.username}, Nombre: {self.name}, Rol: {self.role}'

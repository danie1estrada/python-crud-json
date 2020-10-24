from user import User
import hashlib
import json

class UserController:

    def __init__(self):
        self.file_name = 'users_db.json'
    
    def find(self, username, users=None):
        filtered = [user for user in users or self.get_users() if user.username == username]
        return filtered.pop() if filtered else None

    def get_users(self):
        with open(self.file_name, encoding='utf-8') as db:
            return list(map(lambda user_dict: User(**user_dict), json.load(db) or []))
    
    def create(self, user):
        if self.find(user.username):
            raise Exception('El usuario ya existe')
        
        users = self.get_users()
        users.append(user)

        with open(self.file_name, 'w', encoding='utf-8') as db:
            json.dump(list(map(lambda user: user.to_dict(), users)), db, indent=4)

    def update(self, user):
        users = self.get_users()
        users[users.index(self.find(user.username, users))] = user

        with open(self.file_name, 'w', encoding='utf-8') as db:
            json.dump(list(map(lambda user: user.to_dict(), users)), db, indent=4)

    def delete(self, user):
        users = self.get_users()
        user_to_delete = self.find(user.username, users)
        users.remove(user_to_delete)

        with open(self.file_name, 'w', encoding='utf-8') as db:
            json.dump(list(map(lambda user: user.to_dict(), users)), db, indent=4)

    def encrypt_password(self, password):
        return hashlib.md5(bytes(password, encoding='utf-8')).hexdigest()

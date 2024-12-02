from repositories.auth_repository import AuthRepository
from models.auth_model import AuthModel
import bcrypt

class AuthService:
    
    def __init__(self):
        self.repository = AuthRepository()

    def login(self, usuario, password):
        user = self.repository.login(usuario)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return user
        return None
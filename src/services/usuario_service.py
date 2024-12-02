import time
import bcrypt
from repositories.usuario_repository import UsuarioRepository
from models.usuario_model import Usuario

class UsuarioService:

    def __init__(self):
        self.repository = UsuarioRepository()

    def get_all_usuarios(self):
        return self.repository.get_all_usuarios()
    
    def get_usuario_by_id(self, id):
        return self.repository.get_usuario_by_id(id)
    
    def create_usuario(self, data_usuario):
        if self.repository.get_by_user(data_usuario['usuario']):
            return {'error': 'Usuario ya existe'}
        hashed = bcrypt.hashpw(data_usuario['password'].encode('utf-8'), bcrypt.gensalt())
        data_usuario['password'] = hashed.decode('utf-8')
        usuarioNuevo = Usuario(**data_usuario)
        return self.repository.create_usuario(usuarioNuevo)
    
    def update_usuario(self, id, data_usuario):
        if not self.repository.get_usuario_by_id(id):
            return {'error': 'Usuario no existe'}
        hashed = bcrypt.hashpw(data_usuario['password'].encode('utf-8'), bcrypt.gensalt())
        data_usuario['password'] = hashed.decode('utf-8')
        usuarioNuevo = Usuario(**data_usuario)
        return self.repository.update_usuario(id, usuarioNuevo)
    
    def delete_usuario(self, id):
        return self.repository.delete_usuario(id)
    

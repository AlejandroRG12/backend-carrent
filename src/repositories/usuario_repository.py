from config.firebase_config import initialize_firebase
from models.usuario_model import Usuario

class UsuarioRepository:
    def __init__(self):
        self.db = initialize_firebase()
        self.collection = self.db.collection('usuarios')

    def get_all_usuarios(self):
        usuarios = [doc.to_dict() for doc in self.collection.stream()]
        return [Usuario.from_dict(usuario) for usuario in usuarios]
    
    def get_usuario_by_id(self, usuario_id):
        doc = self.collection.document(usuario_id).get()
        if doc.exists:
            return Usuario.from_dict(doc.to_dict())
        else:
            return None
    
    def get_by_user(self, usuario):
        query = self.collection.where('usuario', '==', usuario).stream()
        result = [doc.to_dict() for doc in query]
        return result[0] if result else None

    def create_usuario(self, data_usaurio):
        doc = self.collection.document()
        doc.set(data_usaurio.to_dict())
        return doc.id
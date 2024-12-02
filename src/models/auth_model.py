class AuthModel:
    def __init__(self, id=None, usuario='', contrasena=''):
        self.id = id
        self.usuario = usuario
        self.password = contrasena
    
    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return AuthModel(**data)


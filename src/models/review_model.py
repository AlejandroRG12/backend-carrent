class Review:
    def __init_(self, id_veiculo='', id_usuario='', puntuacion='', descripcion='', fecha=''):
        self.id_veiculo = id_veiculo
        self.id_usuario = id_usuario
        self.puntuacion = puntuacion
        self.descripcion = descripcion
        self.fecha = fecha

    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return Review(**data)
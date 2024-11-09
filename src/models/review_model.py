class Review:
    def __init__(self, id=None, id_vehiculo='', id_usuario='', puntuacion='', descripcion='', fecha=''):
        self.id = id
        self.id_vehiculo = id_vehiculo
        self.id_usuario = id_usuario
        self.puntuacion = puntuacion
        self.descripcion = descripcion
        self.fecha = fecha

    def to_dict(self):
            return self.__dict__
        
    @staticmethod
    def from_dict(data):
        return Review(**data)
    

"""
    MODEELO PARA POSTMAN

    {
        "id_veiculo": "string",
        "id_usuario": "string",
        "puntuacion": "string",
        "descripcion": "string",
        "fecha": "string"
    }

"""
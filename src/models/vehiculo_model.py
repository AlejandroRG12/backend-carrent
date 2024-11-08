class Vehiculo:
    def __init__(self, id=None, nombre='', modelo='', marca='', imgs=None, tamanioTanque='', tipoDeTransmision='', capacidad='', precioPorRenta='', descripcion=''):
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.marca = marca
        self.imgs = imgs if imgs is not None else []  # Asegúrate de que imgs sea una lista
        self.tamanioTanque = tamanioTanque
        self.tipoDeTransmision = tipoDeTransmision
        self.capacidad = capacidad
        self.precioPorRenta = precioPorRenta
        self.descripcion = descripcion

    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return Vehiculo(**data)
    

"""
    Modelo para postman
    {
    "nombre": "Vehiculo 1",
    "modelo": "Modelo 1",
    "marca": "Marca 1",
    "imgs": ["img1", "img2"],
    "tamanioTanque": "100",
    "tipoDeTransmision": "Manual",
    "capacidad": "5",
    "descripcion": "Descripcion 1"
    }
"""
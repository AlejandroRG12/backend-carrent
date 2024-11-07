class Veiculo:
    def __init__(self, id=None, nombre='', modelo='', marca='', imenes=[], tamanioTanque='', tipoDeTransmision='', capacidad='', precioPorRenta='', descripcion='' ):
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.marca = marca
        self.imenes = imenes
        self.tamanioTanque = tamanioTanque
        self.tipoDeTransmision = tipoDeTransmision
        self.capacidad = capacidad
        self.precioPorRenta = precioPorRenta
        self.descripcion = descripcion

    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return Veiculo(**data)
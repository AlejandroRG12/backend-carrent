class Renta:
    def __init__(self, id=None, idCliente='', idVehiculo='', nombre='', telefono='', direccionOrigen='', ciudadOrigen='', ciudad_pickUp='', fecha_pickUp='', tiempo_picUp='', ciudad_dropOff='', fecha_dropOff='', tiempo_dropOff=''):
        self.id = id
        self.idCliente = idCliente
        self.idVehiculo = idVehiculo
        self.nombre = nombre
        self.telefono = telefono
        self.direccionOrigen = direccionOrigen
        self.ciudadOrigen = ciudadOrigen
        self.ciudad_pickUp = ciudad_pickUp
        self.fecha_pickUp = fecha_pickUp
        self.tiempo_picUp = tiempo_picUp
        self.ciudad_dropOff = ciudad_dropOff
        self.fecha_dropOff = fecha_dropOff
        self.tiempo_dropOff = tiempo_dropOff

    def to_dict(self):
        return self.__dict__
        
    @staticmethod
    def from_dict(data):
        return Renta(**data)
        

"""
    MOdelo para postman

{
    "idCliente": "string",
    "idVehiculo": "string",
    "nombre": "string",
    "telefono": "string",
    "direccionOrigen": "string",
    "ciudadOrigen": "string",
    "ciudad_pickUp": "string",
    "fecha_pickUp": "string",
    "tiempo_picUp": "string",
    "ciudad_dropOff": "string",
    "fecha_dropOff": "string",
    "tiempo_dropOff": "string"
}

"""
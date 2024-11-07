class Usuario:
    def __init__(self, id=None, nombre='', aPaterno='', aMaterno='', ciudad='', direccion='', email='', password='', usuario='', rol='', fechaNacimiento=''):
        self.id = id
        self.nombre = nombre
        self.aPaterno = aPaterno
        self.aMaterno = aMaterno
        self.ciudad = ciudad
        self.direccion = direccion
        self.email = email
        self.password = password
        self.rol = rol
        self.fechaNacimiento = fechaNacimiento
        self.usuario = usuario

    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return Usuario(**data)
    


"""
    Objeto para postman

{
    "nombre": "Alejandro",
    "aPaterno": "Ramirez",
    "aMaterno": "Garcia",
    "email": "Garcia4312@hotmail.com",
    "password": "1234",
    "rol": "super admin",
    "usuario": "alejandro",
    "ciudad": "Gto",
    "direccion": "Calle 123",
    "fechaNacimiento": "1999-02-08"    
}

"""
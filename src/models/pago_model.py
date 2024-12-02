class Pago:
    def __init__(self, id=None, id_renta='', targeta_numero='', targeta_expiracion='', targeta_propietario='', targeta_cvc='', montoTotal='', fecha=''):
        self.id = id
        self.id_renta = id_renta
        self.targeta_numero = targeta_numero
        self.targeta_expiracion = targeta_expiracion
        self.targeta_propietario = targeta_propietario
        self.targeta_cvc = targeta_cvc
        self.montoTotal = montoTotal
        self.fecha = fecha

    def to_dict(self):
        return self.__dict__
        
    @staticmethod
    def from_dict(data):
        return Pago(**data)
    
"""
    Modelo postman

{
    "id_renta": "string",
    "targeta_numero": "string",
    "targeta_expiracion": "string",
    "targeta_propietario": "string",
    "targeta_cvc": "string",
    "paypal_correo": "string",
    "montoTotal": "string",
    "fecha": "string"
}
"""
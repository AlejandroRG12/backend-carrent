class Pago:
    def __init__(self, id=None, id_renta='', targeta_numero='', targeta_expiracion='', targeta_propietario='', targeta_cvc='', paypal_correo='', montoTotal='', fecha=''):
        self.id = id
        self.id_renta = id_renta
        self.targeta_numero = targeta_numero
        self.targeta_expiracion = targeta_expiracion
        self.targeta_propietario = targeta_propietario
        self.targeta_cvc = targeta_cvc
        self.paypal_correo = paypal_correo
        self.montoTotal = montoTotal
        self.fecha = fecha

    def to_dict(self):
        return self.__dict__
        
    @staticmethod
    def from_dict(data):
        return Pago(**data)
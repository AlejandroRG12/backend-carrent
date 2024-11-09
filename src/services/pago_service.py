from repositories.pago_repository import PagoRepository
from models.pago_model import Pago

class PagoService:
    
    def __init__(self):
        self.repository = PagoRepository()

    def get_all_pagos(self):
        return self.repository.get_all_pagos()
    
    def get_pago_by_id(self, id):
        return self.repository.get_pago_by_id(id)
    
    def create_pago(self, data_pago):
        pagoNuevo = Pago(**data_pago)
        return self.repository.create_pago(pagoNuevo)
    
    def update_pago(self, id, data_pago):
        pago = self.repository.get_pago_by_id(id)
        if pago:
            self.repository.update_pago(id, Pago(**data_pago))
            return id
        else:
            return None
    
    def delete_pago(self, id):
        pago = self.repository.get_pago_by_id(id)
        if pago:
            self.repository.delete_pago(id)
            return id
        else:
            return None
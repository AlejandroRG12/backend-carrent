from config.firebase_config import initialize_firebase
from models.pago_model import Pago

class PagoRepository:
    def __init__(self):
        self.db = initialize_firebase()
        self.collection = self.db.collection('pagos')

    def get_all_pagos(self):
        pagos = [doc.to_dict() for doc in self.collection.stream()]
        return [Pago.from_dict(pago) for pago in pagos]
    
    def get_pago_by_id(self, pago_id):
        doc = self.collection.document(pago_id).get()
        if doc.exists:
            return Pago.from_dict(doc.to_dict())
        else:
            return None
    
    def get_by_user(self, usuario):
        query = self.collection.where('usuario', '==', usuario).stream()
        result = [doc.to_dict() for doc in query]
        return result[0] if result else None

    def create_pago(self, data_pago):
        doc = self.collection.document()
        doc.set(data_pago.to_dict())
        return doc.id
    
    def update_pago(self, pago_id, data_pago):
        self.collection.document(pago_id).update(data_pago.to_dict())
        return pago_id
    
    def delete_pago(self, pago_id):
        self.collection.document(pago_id).delete()
        return pago_id